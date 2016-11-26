#ultra.py
import RPi.GPIO as gpio
import time

# use BCM pin without pin's location
gpio.setmode(gpio.BOARD)   # BCM, BOARD

trig = 8    # 4th  BCM 14, BOARD : 8
echo = 10   # 5th  BCM 15, BOARD :10

#trig = 16 
#echo = 18 

print "start"


gpio.setup(trig, gpio.OUT)
gpio.setup(echo, gpio.IN)

try :
   while True :
      gpio.output(trig, False)
      time.sleep(1)

      gpio.output(trig, True)
      time.sleep(0.00001)
      gpio.output(trig, False)

      while gpio.input(echo) == 0 :
         pulse_start = time.time()

      while gpio.input(echo) == 1 :
         pulse_end = time.time()

      pulse_duration = pulse_end - pulse_start
      distance = pulse_duration * 36000
      distance = distance / 2
      distance = round(distance, 2)

      print "Distance : ", distance, "cm"

except :
   print "except error, GPIO.cleanup()"
   gpio.cleanup()
          