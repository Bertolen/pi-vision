import cv2
from flask import Flask, Response

# Initialisation de Flask
app = Flask(__name__)

# Initialisation de la webcam
camera = cv2.VideoCapture(0)  # 0 pour la webcam par défaut


def generate_frames():
    """
    Génère des frames depuis la webcam et les encode en MJPEG.
    """
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Encode l'image en format JPEG
            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Utilise le format MJPEG pour diffuser le flux
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """
    Route HTTP pour accéder au flux vidéo.
    """
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

