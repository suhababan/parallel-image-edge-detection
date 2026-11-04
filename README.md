Parallel Image Edge Detection and Performance Analysis

A web-based application that demonstrates and compares sequential and parallel image edge detection. The project uses parallel processing to improve execution time and provides a visual comparison of the results.

🚀 Features

- Upload images for edge detection.
- Perform sequential and parallel processing.
- Compare edge detection results side by side.
- Display execution time for both methods.
- Calculate speedup to analyse performance.
- Simple and user-friendly web interface.

🛠️ Technologies Used

- Python – Application backend
- Flask – Web framework
- C++ – Image processing program
- OpenCV – Image processing
- OpenMP – Parallel processing
- HTML & CSS – Frontend development

⚙️ How It Works

1. The user uploads an image through the web interface.
2. The application processes the image using sequential and parallel approaches.
3. Edge detection results are generated.
4. Execution times are measured for both approaches.
5. The results are displayed for visual and performance comparison.

📊 Performance Analysis

The application compares sequential and parallel execution times and calculates the speedup achieved through parallel processing.

Speedup = Sequential Execution Time / Parallel Execution Time

📁 Project Structure

- "app.py" – Flask application
- "index.html" – Main web interface
- "index (2).html" – Additional HTML file
- "nyc.webp" – Sample image
- "parallel_edges.png" – Parallel processing output
- "sequential_edges.png" – Sequential processing output

🎯 Project Objective

To understand parallel computing concepts and analyse how parallel processing can improve image processing performance compared to sequential execution.

---

Developed as an academic project.
