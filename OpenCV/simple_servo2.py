# simple_servo2.py

# use the circuit from "simple_servo2.png"

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)      # use GPIO pin numbering, not physical pin numbering

led_gpio_pin = 18
pans_gpio_pin = 24
tilt_gpio_pin = 25 

GPIO.setup(led_gpio_pin, GPIO.OUT)
GPIO.setup(pans_gpio_pin, GPIO.OUT)
GPIO.setup(tilt_gpio_pin, GPIO.OUT)

pwmObject_pans = GPIO.PWM(pans_gpio_pin, 100)         # frequency = 100 Hz
pwmObject_tilt = GPIO.PWM(tilt_gpio_pin, 100)         # frequency = 100 Hz

pwmObject_pans.start(14)             # initial duty cycle = 14%
pwmObject_tilt.start(14)             # initial duty cycle = 14%

def angleToduty(angle):
    dutyCycle = ((float(angle) * 0.01) + 0.5) * 10
    return dutyCycle


###################################################################################################
def main():

    try:
       while True:
           GPIO.output(led_gpio_pin, True)
           strAngle = raw_input("enter desired pans angle (0 to 180): ")
           if strAngle == '':
              return
           intAngle = int(strAngle)
           #dutyCycle = ((float(intAngle) * 0.01) + 0.5) * 10
           pwmObject_pans.ChangeDutyCycle(angleToduty(intAngle))
           
           GPIO.output(led_gpio_pin, False)
           strAngle = raw_input("enter desired tilt angle (0 to 180): ")
           if strAngle == '':
              return
           intAngle = int(strAngle)
           #dutyCycle = ((float(intAngle) * 0.01) + 0.5) * 10
           pwmObject_tilt.ChangeDutyCycle(angleToduty(intAngle))
       # end while
    
    except KeyboardInterrupt:
       pwmObject_pans.stop()
       pwmObject_tilt.stop()
       print "except GPIO.cleanup()"
       GPIO.cleanup()


    return

###################################################################################################
if __name__ == "__main__":
    pwmObject_pans.ChangeDutyCycle(angleToduty(85))
    pwmObject_tilt.ChangeDutyCycle(angleToduty(45))
    
    main()
    pwmObject_pans.stop()
    pwmObject_tilt.stop()
    print "main GPIO.cleanup()"
    GPIO.cleanup()

