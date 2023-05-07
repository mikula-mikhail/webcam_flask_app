from flask import Flask, render_template, Response, jsonify
# from camera import VideoCamera
import cv2 as cv

import time

class VideoCamera(object):
    
    def __init__(self):
        self.video = cv.VideoCapture(0)
        self.fourcc = cv.VideoWriter_fourcc(*'XVID')
        self.output = cv.VideoWriter('webcam_output.avi', self.fourcc, 24.0, (640, 480))


    def __del__(self):
        self.video.release()
        self.output.release()

    def get_frame(self):
        ret, frame = self.video.read()
        
        self.output.write(frame)

            


        # other code

        

        # ret, jpeg = cv.imencode('.jpg', frame)

        # return jpeg.tobytes()


app = Flask(__name__)

# video_stream = cv.VideoCapture(0)

def main():
    while True:
        video_stream.get_frame()

        if cv.waitKey(1) == ord('q'):
            break

cap = cv.VideoCapture('output.avi')

@app.route('/')
def index():
    return render_template('index.html')

def gen():
    while True:
        ret, frame = video_stream.read()
        # ret, jpeg = cv.imencode('.jpg', frame)
        # time.sleep(1/24)
        ret, jpeg = cv. imencode('.jpg', frame)
        frame = jpeg.tobytes()
        return (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    video_stream = cv.VideoCapture(0)
    app.run(host='127.0.0.1', debug=True, port="5000")
    # gen()
