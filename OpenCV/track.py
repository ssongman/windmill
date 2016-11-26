<<<<<<< HEAD
# track.py

=======
>>>>>>> 3038cde2de72fe91f50b0f689164c229490b09f4
import cv2
import numpy as np

cam=cv2.VideoCapture(0)
<<<<<<< HEAD
#kernel=np.ones((5,5), np.unit8)

    
=======
#kernel=np.ones((5,5), np.uint8)
>>>>>>> 3038cde2de72fe91f50b0f689164c229490b09f4

while (True):
    ret, frame = cam.read()
    #rangomax = np.array([50,255,50])
<<<<<<< HEAD
    #rangomin = np.array([0,51,0])
    
    
    rows,cols = frame.shape[:2]
    M = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
    frame = cv2.warpAffine(frame,M,(cols,rows))
    
    
    cv2.imshow('camera', frame)
    k=cv2.waitKey(1) & 0xff
    if k==27:
        pass
=======
    cv2.imshow('camera', frame)
    k=cv2.waitKey(1) & 0xFF
    if k==27:
        pass
>>>>>>> 3038cde2de72fe91f50b0f689164c229490b09f4
