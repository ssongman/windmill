import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)   # BCM, BOARD

gpio.setup( 7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)


#gpio.output( 7,True)
#gpio.output(11,True)

time.sleep(1)
print 'after sleep(1)'

try :
   for i in range(5):
      print 'i = ', i
      
      #forward
      print 'forward'
      gpio.output( 7,True)
      gpio.output(11,False)
      gpio.output(13,True)
      gpio.output(15,False)
      time.sleep(1)
      
      #reverse
      print 'reverse'
      gpio.output( 7,False)
      gpio.output(11,True)
      gpio.output(13,False)
      gpio.output(15,True)
      time.sleep(1)
      
      #stop
      print 'stop'
      gpio.output( 7,False)
      gpio.output(11,False)
      gpio.output(13,False)
      gpio.output(15,False)
      time.sleep(1)
      
      #pivot_left
      print 'pivot_left'
      gpio.output( 7,True)
      gpio.output(11,False)
      gpio.output(13,False)
      gpio.output(15,True)
      time.sleep(2)
      
      #pivot_right
      print 'pivot_right'
      gpio.output( 7,False)
      gpio.output(11,True)
      gpio.output(13,True)
      gpio.output(15,False)
      time.sleep(2)
      
      #left_turn
      print 'left_turn'
      gpio.output( 7,True)
      gpio.output(11,False)
      gpio.output(13,True)
      gpio.output(15,True)
      time.sleep(2)
      
      #right_turn
      print 'right_turn'
      gpio.output( 7,True)
      gpio.output(11,True)
      gpio.output(13,True)
      gpio.output(15,False)
      time.sleep(2)
      
   print 'gpio.cleanup()'
   gpio.cleanup()

except :
   print "except error, GPIO.cleanup()"
   gpio.cleanup()
   


