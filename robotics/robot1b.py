import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)   # BCM, BOARD

gpio.setup(31, gpio.OUT)
gpio.setup(33, gpio.OUT)
gpio.setup(35, gpio.OUT)
gpio.setup(37, gpio.OUT)


gpio.output(31,True)
gpio.output(33,True)

time.sleep(1)
print 'after sleep(1)'

for i in range(5):
   try :
      print 'i = ', i
      gpio.output(35,True)
      gpio.output(37,False)
      time.sleep(2)
      gpio.output(35,False)
      gpio.output(37,True)
      time.sleep(2)
      gpio.output(35,False)
      gpio.output(37,False)
      time.sleep(2)
   except :
      print "except error, GPIO.cleanup()"
      gpio.cleanup()
   

print 'gpio.cleanup()'
gpio.cleanup()

