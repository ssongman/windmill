# simple_servo.py
# use the circuit from "simple_servo.png"

import RPi.GPIO as GPIO



####################################################################################################
#def main():
#    GPIO.setmode(GPIO.BOARD)      # BCM, BOARD  use GPIO pin numbering, not physical pin numbering
#
#    pan_gpio_pin = 16
#
#    GPIO.setup(pan_gpio_pin, GPIO.OUT)
#
#    pwmObject = GPIO.PWM(pan_gpio_pin, 100)         # frequency = 100 Hz
#
#    pwmObject.start(14)             # initial duty cycle = 14%
#
#    while True:
#        strAngle = raw_input("enter desired angle (0 to 180): ")
#        intAngle = int(strAngle)
#        dutyCycle = ((float(intAngle) * 0.01) + 0.5) * 10
#        pwmObject.ChangeDutyCycle(dutyCycle)
#    # end while
#
#    return
#
####################################################################################################
#if __name__ == "__main__":
#    main()



GPIO.setmode(GPIO.BOARD)      # BCM, BOARD  use GPIO pin numbering, not physical pin numbering

pan_gpio_pin = 12
GPIO.setup(pan_gpio_pin, GPIO.OUT)
pwmObject = GPIO.PWM(pan_gpio_pin, 100)         # frequency = 100 Hz
pwmObject.start(14)             # initial duty cycle = 14%

try :
    while True:
        strAngle = raw_input("enter desired angle (0 to 180): ")
        intAngle = int(strAngle)
        dutyCycle = ((float(intAngle) * 0.01) + 0.5) * 10
        pwmObject.ChangeDutyCycle(dutyCycle)
    # end while

except :
   print "except error, GPIO.cleanup()"
   GPIO.cleanup()

