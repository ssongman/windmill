# spped
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)   # BCM, BOARD

#gpio.setup( 7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)

#gpio.output( 7,True)
#gpio.output(11,True)

time.sleep(1)
print 'after sleep(1)'

pwmObject = gpio.PWM(11, 100)         # frequency = 100 Hz
pwmObject.start(70)                   # spped 0 to 100


for i in range(5):
   try :
      print 'i = ', i
      gpio.output(13,True)
      gpio.output(15,False)
      time.sleep(2)
      gpio.output(13,False)
      gpio.output(15,True)
      time.sleep(2)
      gpio.output(13,False)
      gpio.output(15,False)
      time.sleep(2)
   except :
      print "except error, GPIO.cleanup()"
      gpio.cleanup()
   

print 'gpio.cleanup()'
gpio.cleanup()

