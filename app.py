from flask import Flask, request, jsonify, send_from_directory
import os
import subprocess

app = Flask(__name__)

PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))

# C++ program compiled in MSYS2 UCRT64
CPP_PROGRAM = r"C:\msys64\home\suhab\edge_detection.exe"

# Allow OpenCV and OpenMP DLLs to be found
environment = os.environ.copy()
environment["PATH"] = (
    r"C:\msys64\ucrt64\bin"
    + os.pathsep
    + environment.get("PATH", "")
)


@app.route("/")
def home():
    return send_from_directory(PROJECT_FOLDER, "index.html")


@app.route("/upload", methods=["POST"])
def upload_image():
    uploaded_file = request.files.get("image")

    if not uploaded_file or uploaded_file.filename == "":
        return jsonify({"error": "Please select an image."}), 400

    extension = os.path.splitext(uploaded_file.filename)[1].lower()

    if extension not in [".png", ".jpg", ".jpeg", ".webp", ".bmp"]:
        return jsonify({"error": "Unsupported image format."}), 400

    input_path = os.path.join(PROJECT_FOLDER, "uploaded_image" + extension)

    uploaded_file.save(input_path)

    try:
        result = subprocess.run(
            [CPP_PROGRAM, input_path, PROJECT_FOLDER],
            capture_output=True,
            text=True,
            timeout=120,
            env=environment
        )

        if result.returncode != 0:
            return jsonify({
                "error": "C++ processing failed.",
                "details": result.stderr or result.stdout
            }), 500

        output = result.stdout

        sequential_time = None
        parallel_time = None
        speedup = None

        for line in output.splitlines():
            if line.startswith("Sequential Time:"):
                sequential_time = line.split(":", 1)[1].strip()
            elif line.startswith("Parallel Time:"):
                parallel_time = line.split(":", 1)[1].strip()
            elif line.startswith("Speedup:"):
                speedup = line.split(":", 1)[1].strip()

        return jsonify({
            "success": True,
            "original": "/images/" + os.path.basename(input_path),
            "sequential": "/images/sequential_edges.png",
            "detected": "/images/parallel_edges.png",
            "sequentialTime": sequential_time,
            "parallelTime": parallel_time,
            "speedup": speedup
        })

    except subprocess.TimeoutExpired:
        return jsonify({"error": "Image processing timed out."}), 500

    except Exception as error:
        return jsonify({"error": str(error)}), 500


@app.route("/images/<path:filename>")
def serve_image(filename):
    return send_from_directory(PROJECT_FOLDER, filename)


if __name__ == "__main__":
    app.run(debug=True)