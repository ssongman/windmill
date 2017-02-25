# simple_servo_pca.py
# use the circuit from "simple_servo.png"

from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()


PANS_PCA_PIN = 0
TILT_PCA_PIN = 3


# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

try :
    while True:
        #strAngle = raw_input("enter desired angle (0 to 180): ")
        strAngle = raw_input("enter desired angle (400 to 1000): ")
        intAngle = int(strAngle)
        #dutyCycle = ((float(intAngle) * 0.01) + 0.5) * 10
        #pwmObject.ChangeDutyCycle(dutyCycle)
        pwm.set_pwm(PANS_PCA_PIN, 0, intAngle)
    # end while

except :
   print "program Exit"

