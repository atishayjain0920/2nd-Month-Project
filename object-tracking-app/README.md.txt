🎯 Real-Time Object Tracking Web App
This project is a Flask-based real-time object tracking web application that allows users to drag a bounding box over a live webcam feed to track any object using OpenCV's tracking algorithms (e.g., CSRT).
🚀 Features
- Live webcam feed rendered on the frontend using Flask.
- Canvas-based drag-and-select UI to choose the object.
- Object tracking powered by OpenCV trackers (e.g., CSRT).
- Flask API endpoint to set the selected bounding box.
- Responsive and visually appealing dark UI with CSS.
- Real-time frame streaming via Flask's `Response`.
📂 Project Structure
object-tracking-app/
│
├── app.py                  # Flask backend (runs the server)
├── camera.py               # Video capture & tracking logic using OpenCV
├── templates/
│   └── index.html          # Main frontend page with video + canvas
├── static/
│   ├── css/
│   │   └── styles.css      # Stylesheet for UI (optional, can be inline)
│   └── js/
│       └── script.js       # JS for canvas drawing and POST request
├── venv/                   # Python virtual environment (not committed)
└── README.md               # You're reading it!
🔧 Requirements
- Python 3.10 or lower (Python 3.12 has issues with OpenCV & NumPy compatibility)
- pip (Python package manager)
Python Libraries:
- Flask
- opencv-python
- numpy
⚙️ Setup Instructions
1. Clone the Repo
git clone https://github.com/yourusername/object-tracking-app.git
cd object-tracking-app
2. Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate     # On Windows
# OR
source venv/bin/activate  # On Mac/Linux
3. Install Dependencies
pip install flask opencv-python numpy
If you face NumPy ABI errors, downgrade NumPy:
pip install numpy==1.26.4
🖥️ Run the App
python app.py
Then open your browser and visit:
http://127.0.0.1:5000/
🧠 How It Works
1. Webcam is accessed via OpenCV in `camera.py`.
2. The live feed is streamed as an MJPEG stream using Flask.
3. A transparent HTML5 canvas is placed over the video.
4. Users can draw a rectangle to mark the object to track.
5. JavaScript sends the bounding box (`x, y, w, h`) to the Flask server.
6. OpenCV CSRT tracker tracks the object in real-time.
🐛 Troubleshooting
- ❗ No rectangle appears when dragging → Check JavaScript errors in browser console.
- ❗ Tracking not starting → Make sure the tracker is properly initialized.
- ❗ cv2.error about `cv::dft` or dtype → Ensure frame is `uint8` or convert to `float32`.
- ❗ ModuleNotFoundError → Install missing packages in virtual environment.
- ❗ PermissionError when activating venv → Run PowerShell as Administrator:
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
🎯 Tracker Notes
Uses `cv2.TrackerCSRT_create()` by default.
Can be swapped with other trackers:
- `cv2.TrackerKCF_create()`
- `cv2.TrackerMOSSE_create()` (faster but less accurate)
📄 License
MIT License © 2025 YourName
