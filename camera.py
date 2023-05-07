import cv2 as cv
import numpy as np


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, frame = self.video.read()

        # other code

        ret, jpeg = cv2.imencode('.jpg', frame)

        return jpeg.tobytes()


cap = cv.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('webcamera_output.avi', fourcc, 24.0, (640, 480))


if not cap.isOpened():
    print("Cannot open camera.\nRetrying...")
    cap.open()
    if not cap.isOpened():
        print("Failed to open camera again")
        exit()
else:
    print("All is fine")
    print("width x height: {}x{}".format(
        cap.get(cv.CAP_PROP_FRAME_WIDTH),
        cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    )
    print("Setting to 1200x900")
    # cap.set(cv.CAP_PROP_FRAME_WIDTH, 1200)
    # cap.set(cv.CAP_PROP_FRAME_HEIGHT, 900)


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret == True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # write the frame
    out.write(frame)
    cv.imwrite('o.jpeg', frame)
    ret, jpeg = cv.imencode('.jpg', frame)
    img = jpeg.tobytes()
    
    # Our operations on the frame come here
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break



# When everything done, release the capture
cap.release()
out.release()
cv.destroyAllWindows()
