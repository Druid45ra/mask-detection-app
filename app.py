from flask import Flask, render_template, request, jsonify, Response
import cv2
import numpy as np
from mask_detector import MaskDetector

app = Flask(__name__)

# Creează o instanță a clasei MaskDetector
mask_detector = MaskDetector('models/mask_detector_model.h5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    # Citește fișierul imagine
    img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR)
    
    # Detectează masca
    result = mask_detector.detect_mask(img)
    
    return jsonify(result)

def generate_frames():
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # Detectează masca în fiecare cadru
            result = mask_detector.detect_mask(frame)
            label = "Mask" if result['mask'] else "No Mask"
            color = (0, 255, 0) if result['mask'] else (0, 0, 255)
            
            # Afișează rezultatul pe cadru
            cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
