import cv2
import numpy as np


# w = 1280
# h = 720
w = 640
h = 480

capture = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)
#capture = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, w)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
# capture.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
# capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1440)

while cv2.waitKey(33)< 0:
    ret,frame = capture.read()
    cv2.imshow("VideoFrame", frame)

capture.release()
cv2.destroyAllWindows()


