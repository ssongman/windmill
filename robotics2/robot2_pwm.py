import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)   # BCM, BOARD
gpio.setup( 7, gpio.OUT)   # right
gpio.setup(11, gpio.OUT)   # right
gpio.setup(13, gpio.OUT)   #left
gpio.setup(15, gpio.OUT)   #left

pwm_RA = gpio.PWM( 7, 100)         # frequency = 100 Hz
pwm_RB = gpio.PWM(11, 100)         # frequency = 100 Hz
pwm_LA = gpio.PWM(13, 100)         # frequency = 100 Hz
pwm_LB = gpio.PWM(15, 100)         # frequency = 100 Hz
pwm_RA.start(0)
pwm_RB.start(0)
pwm_LA.start(0)
pwm_LB.start(0)


speed = 0   # 0 to 100



def stop():
    print 'stop'
    pwm_RA.ChangeDutyCycle(0)                   # spped 0 to 100             #pwm_r.ChangeDutyCycle(100)
    pwm_RB.ChangeDutyCycle(0)                   # spped 0 to 100             #pwm_r.ChangeDutyCycle(100)
    pwm_LA.ChangeDutyCycle(0)                   # spped 0 to 100             #pwm_r.ChangeDutyCycle(100)
    pwm_LB.ChangeDutyCycle(0)                   # spped 0 to 100             #pwm_r.ChangeDutyCycle(100)


time.sleep(1)
print 'after sleep(1)'

try :
   for i in range(5):
      print 'i = ', i

      #forward
      speed = 100
      print 'forward - speed: ' + str(speed)
      pwm_RA.ChangeDutyCycle(speed)
      pwm_LA.ChangeDutyCycle(speed)
      time.sleep(1)
      stop()
      time.sleep(1)
      
      #reverse
      speed = 100
      print 'reverse - speed: ' + str(speed)
      pwm_RB.ChangeDutyCycle(speed)
      pwm_LB.ChangeDutyCycle(speed)
      time.sleep(1)
      stop()
      time.sleep(1)
      
      #forward
      speed = 50
      print 'forward - speed: ' + str(speed)
      pwm_RA.ChangeDutyCycle(speed)
      pwm_LA.ChangeDutyCycle(speed)
      time.sleep(1)
      stop()
      time.sleep(1)
      
      #reverse
      speed = 50
      print 'reverse - speed: ' + str(speed)
      pwm_RB.ChangeDutyCycle(speed)
      pwm_LB.ChangeDutyCycle(speed)
      time.sleep(1)
      stop()
      time.sleep(1)
      
      #pivot_left
      speed = 50
      print 'pivot_left - speed: ' + str(speed)
      pwm_RA.ChangeDutyCycle(speed)
      pwm_LB.ChangeDutyCycle(speed)
      time.sleep(1)
      stop()
      time.sleep(1)
      
      #pivot_right
      speed = 50
      print 'pivot_right - speed: ' + str(speed)
      pwm_RB.ChangeDutyCycle(speed)
      pwm_LA.ChangeDutyCycle(speed)
      time.sleep(1)
      stop()
      time.sleep(1)
      
      
      #left_turn
      speed = 50
      print 'left_turn - speed: ' + str(speed)
      pwm_RA.ChangeDutyCycle(speed)
      pwm_RB.ChangeDutyCycle(0)
      pwm_LA.ChangeDutyCycle(100)
      pwm_LB.ChangeDutyCycle(100)
      time.sleep(1)
      stop()
      time.sleep(1)
      
      #right_turn
      speed = 50
      print 'right_turn - speed: ' + str(speed)
      pwm_RA.ChangeDutyCycle(100)
      pwm_RB.ChangeDutyCycle(100)
      pwm_LA.ChangeDutyCycle(speed)
      pwm_LB.ChangeDutyCycle(0)
      time.sleep(1)
      stop()
      time.sleep(1)
      


   print 'gpio.cleanup()'
   gpio.cleanup()

except :
   print "except error, GPIO.cleanup()"
   gpio.cleanup()



