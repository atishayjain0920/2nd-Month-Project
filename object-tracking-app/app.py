from flask import Flask, render_template, Response, request, jsonify
from camera import VideoCamera

app = Flask(__name__)
camera = VideoCamera()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    def gen(camera):
        while True:
            frame = camera.get_frame()
            if frame:
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    return Response(gen(camera), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/set_bbox', methods=['POST'])
def set_bbox():
    try:
        data = request.get_json()
        bbox_data = data.get('bbox', [])
        
        if len(bbox_data) == 4:
            x, y, w, h = map(int, bbox_data)
            camera.set_bbox(x, y, w, h)
            return jsonify({'status': 'success'})
        else:
            return jsonify({'status': 'error', 'message': 'Invalid bounding box format'}), 400

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
