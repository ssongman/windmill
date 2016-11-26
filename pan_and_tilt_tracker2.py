# pan_and_tilt_tracker.py
# git test

# to run this program, type:
# sudo python pan_and_tilt_tracker.py headed          (GUI)
# sudo python pan_and_tilt_tracker.py headless        (no GUI (for embedded use))

# this program pans/tilts two servos so a mounted webcam tracks a red ball

# use the circuit from "pan_and_tilt_tracker.png"

import RPi.GPIO as GPIO
import cv2
import numpy as np
import os
import sys
from operator import itemgetter
import Adafruit_PCA9685
import time



'''
#####################################################
def AngleUp(event):
    global CurPulse_tilt, CurPulse_pans
    CurPulse_tilt -= MOVING_PULSE
    if CurPulse_tilt < TILT_PULSE_MIN: CurPulse_tilt = TILT_PULSE_MIN
    pwm.set_pwm(TILT_PCA_PIN, 0, CurPulse_tilt)
    print 'Key: ', event.char, ', angle(pan,tilt) : ', CurPulse_pans, CurPulse_tilt
#####################################################
'''



####################################################################################################
# PCA9685 setting, Servo 
####################################################################################################

# Import the PCA9685 module.
pwm = Adafruit_PCA9685.PCA9685()

# Set frequency to 100 hz, good for servos.
pwm.set_pwm_freq(100)      # between 40hz and 1000hz

#led_gpio_pin = 18
PANS_PCA_PIN = 0
TILT_PCA_PIN = 3

# Configure min and max servo pulse lengths
SPAN_PULSE_MIN =  650  # Min pulse length out of 4096
SPAN_PULSE_MAX = 1000  # Max pulse length out of 4096
TILT_PULSE_MIN =  400  # Min pulse length out of 4096
TILT_PULSE_MAX = 1000  # Max pulse length out of 4096

MOVING_PULSE = 50

MID_PULSE_PANS = 850
MID_PULSE_TILT = 800
       
        
        
        

###################################################################################################
def main():
    headed_or_headless = ""

    if len(sys.argv) == 2 and str(sys.argv[1]) == "headed":
        headed_or_headless = "headed"
        print "entering headed mode"
    elif len(sys.argv) == 2 and str(sys.argv[1]) == "headless":
        headed_or_headless = "headless"
        print "entering headless mode"
    else:
        headed_or_headless = "headless"
        print "entering headless mode"
    #else:
    #    print "\nprogram usage:\n"
    #    print "for headed mode (GUI interface) @command prompt type: sudo python pan_and_tilt_tracker.py headed\n"
    #    print "for headless mode (no GUI interface, i.e. embedded mode) @ command prompt type: sudo python pan_and_tilt_tracker.py headless\n"
    #    return
    # end if else


    
    
    CurPulse_pans = MID_PULSE_PANS  # pans servo position in degrees
    CurPulse_tilt = MID_PULSE_TILT  # tilt servo position in degrees





    ####################################################################################################
    # capWebcam
    ####################################################################################################
    
    capWebcam = cv2.VideoCapture(0)                     # declare a VideoCapture object and associate to webcam, 0 => use 1st webcam

    print "default resolution = " + str(capWebcam.get(cv2.CAP_PROP_FRAME_WIDTH)) + "x" + str(capWebcam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    #capWebcam.set(cv2.CAP_PROP_FRAME_WIDTH, 320.0)
    #capWebcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240.0)

    print "updated resolution = " + str(capWebcam.get(cv2.CAP_PROP_FRAME_WIDTH)) + "x" + str(capWebcam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    if capWebcam.isOpened() == False:                           # check if VideoCapture object was associated to webcam successfully
        print "error: capWebcam not accessed successfully\n\n"          # if not, print error message to std out
        os.system("pause")                                              # pause until user presses a key so user can see error message
        return                                                          # and exit function (which exits program)
    # end if

    intXFrameCenter = int(float(capWebcam.get(cv2.CAP_PROP_FRAME_WIDTH)) / 2.0)
    intYFrameCenter = int(float(capWebcam.get(cv2.CAP_PROP_FRAME_HEIGHT)) / 2.0)
    
    print 'capWebcam.get(cv2.CAP_PROP_FRAME_WIDTH)  : ', capWebcam.get(cv2.CAP_PROP_FRAME_WIDTH)
    print 'capWebcam.get(cv2.CAP_PROP_FRAME_HEIGHT) : ', capWebcam.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print 'intXFrameCenter : ', intXFrameCenter
    print 'intYFrameCenter : ', intYFrameCenter

    updateServoMotorPositions(pwm, CurPulse_pans, CurPulse_tilt)

    while cv2.waitKey(1) != 27 and capWebcam.isOpened():                # until the Esc key is pressed or webcam connection is lost
        blnFrameReadSuccessfully, imgOriginal = capWebcam.read()            # read next frame

        if not blnFrameReadSuccessfully or imgOriginal is None:             # if frame was not read successfully
            print "error: frame not read from webcam\n"                     # print error message to std out
            os.system("pause")                                              # pause until user presses a key so user can see error message
            break                                                           # exit while loop (which exits program)
        # end if

        imgHSV = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2HSV)

        imgThreshLow = cv2.inRange(imgHSV, np.array([0, 135, 135]), np.array([19, 255, 255]))
        imgThreshHigh = cv2.inRange(imgHSV, np.array([168, 135, 135]), np.array([179, 255, 255]))

        imgThresh = cv2.add(imgThreshLow, imgThreshHigh)

        imgThresh = cv2.GaussianBlur(imgThresh, (3, 3), 2)

        imgThresh = cv2.dilate(imgThresh, np.ones((5,5),np.uint8))
        imgThresh = cv2.erode(imgThresh, np.ones((5,5),np.uint8))

        intRows, intColumns = imgThresh.shape

        circles = cv2.HoughCircles(imgThresh, cv2.HOUGH_GRADIENT, 3, intRows / 4)      # fill variable circles with all circles in the processed image

        #GPIO.output(led_gpio_pin, GPIO.LOW)

        if circles is not None:                     # this line is necessary to keep program from crashing on next line if no circles were found
            #GPIO.output(led_gpio_pin, GPIO.HIGH)

            sortedCircles = sorted(circles[0], key = itemgetter(2), reverse = True)

            largestCircle = sortedCircles[0]

            x, y, radius = largestCircle                                                                       # break out x, y, and radius
            print "ball position x = " + str(x) + ", y = " + str(y) + ", radius = " + str(radius)       # print ball position and radius

            if x < intXFrameCenter:
                CurPulse_pans = CurPulse_pans + 10
                if CurPulse_pans > SPAN_PULSE_MAX: CurPulse_pans = SPAN_PULSE_MAX
                direct_x = 'x+'
            elif x > intXFrameCenter:
                CurPulse_pans = CurPulse_pans - 10
                if CurPulse_pans < SPAN_PULSE_MIN: CurPulse_pans = SPAN_PULSE_MIN
                direct_x = 'x-'
            else:
                direct_x = 'x='
            # end if else                                                                     # break out x, y, and radius

            if y < intYFrameCenter:
                CurPulse_tilt = CurPulse_tilt - 10
                if CurPulse_tilt < TILT_PULSE_MIN: CurPulse_tilt = TILT_PULSE_MIN
                direct_y = 'y-'
            elif y > intYFrameCenter:
                CurPulse_tilt = CurPulse_tilt + 10
                if CurPulse_tilt > TILT_PULSE_MAX: CurPulse_tilt = TILT_PULSE_MAX
                direct_y = 'y+'
            else:
                direct_y = 'y='
            # end if else
            
            print "CurPulse_pans = " + str(CurPulse_pans) + ",  CurPulse_tilt = " + str(CurPulse_tilt) + " " + direct_x + direct_y
            updateServoMotorPositions(pwm, CurPulse_pans, CurPulse_tilt)

            if headed_or_headless == "headed":
                cv2.circle(imgOriginal, (x, y), 3, (0, 255, 0), -1)           # draw small green circle at center of detected object
                cv2.circle(imgOriginal, (x, y), radius, (0, 0, 255), 3)                     # draw red circle around the detected object
            # end if

        # end if

        if headed_or_headless == "headed":
            cv2.imshow("imgOriginal", imgOriginal)                 # show windows
            cv2.imshow("imgThresh", imgThresh)
        # end if
        #time.sleep(0.3)
    # end while

    cv2.destroyAllWindows()                     # remove windows from memory

    return
# end main


def updateServoMotorPositions(pwm, CurPulse_pans, CurPulse_tilt):
    pwm.set_pwm(PANS_PCA_PIN, 0, CurPulse_pans)
    pwm.set_pwm(TILT_PCA_PIN, 0, CurPulse_tilt)
# end function

###################################################################################################
if __name__ == "__main__":
    main()


