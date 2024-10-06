import cv2
import smtplib
from flask import Flask, Response
from ultralytics import YOLO
import torch
import threading
from threading import Thread

from flask import Flask, Response


class EndpointAction(object):

    def __init__(self, video_capture):
        self.video_capture = video_capture

    def __call__(self, *args):
        return Response(self.generate_frames(),
                        mimetype='multipart/x-mixed-replace; boundary=frame')
    def generate_frames(self):
        while True:
            success, frame = self.video_capture.read()
            if not success:
                break
            else:
                # Codifica il frame in formato JPEG
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                # Genera un frame come parte di un flusso multipart
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


class FlaskAppWrapper(object):

    def __init__(self, name):
        self.app = Flask(name)
        self.video_capture = cv2.VideoCapture(0)

    def run(self):
        self.app.run()

    def clear_endpoints(self):
        self.app.view_functions.clear()

    def add_endpoint(self, endpoint=None, endpoint_name=None):
        self.app.add_url_rule(endpoint, endpoint_name, EndpointAction(self.video_capture))


class DetectionModel(Thread):
    def __init__(self, model_path, emergency_email):
        super().__init__()
        self.model = YOLO(model_path)
        self.flaskapp = FlaskAppWrapper('fall_detection')
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.emergency_email = emergency_email
        self.pred_to_text = {1: "Standing",
                    0: "Fall"}
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()
        self.flaskapp.clear_endpoints()

    def run(self):
        self._stop_event.clear()
        self.model.to(self.device)
        consecutive_frames=0
        sent=False
        while True:
            if self._stop_event.is_set():
                break
            _, frame = self.flaskapp.video_capture.read()

            result = self.model(frame, save=False)

            if result:
                res = result[0]
                if res.boxes:
                    consecutive_frames += 1
            else:
                consecutive_frames = 0
            if consecutive_frames==1 and sent==False:
                # Invia l'e-mail con il link allo stream
                self.send_email()
                sent = True
                print("Alert email sent!!!")
                # Avvia il server Flask in un thread separato per lo streaming video
                self.flaskapp.add_endpoint('/video_feed', 'video_feed')
                self.flaskapp.run()

    def send_email(self):
        # Configurazione e-mail
        sender_email = "polibatest@outlook.it"
        password = "TestExam"

        # Contenuto dell'e-mail
        subject = "Alert: Fall Detected"
        body = "A fall has been detected by the system. Please check immediately at: http://localhost:5000/video_feed"

        message = f"Subject: {subject}\n\n{body}"

        try:
            # Connessione al server SMTP di Outlook
            with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:
                server.starttls()  # Attiva la modalità TLS
                server.login(sender_email, password)
                server.sendmail(sender_email, self.emergency_email, message)
            print("E-mail inviata con successo!")
        except Exception as e:
            print(f"Errore durante l'invio dell'e-mail: {e}")
