import cv2
import numpy as np

cam=cv2.VideoCapture(0)
#kernel=np.ones((5,5), np.uint8)

while (True):
    ret, frame = cam.read()
    #rangomax = np.array([50,255,50])
    cv2.imshow('camera', frame)
    k=cv2.waitKey(1) & 0xFF
    if k==27:
        pass
