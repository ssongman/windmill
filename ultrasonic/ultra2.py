#ultra.py
import RPi.GPIO as gpio
import time

# use BCM pin without pin's location
gpio.setmode(gpio.BOARD)   # BCM, BOARD

TRIG_PIN = 8    # 4th  BCM 14, BOARD : 8
ECHO_PIN = 10   # 5th  BCM 15, BOARD :10

#TRIG_PIN = 16 
#ECHO_PIN = 18 

print "start"


gpio.setup(TRIG_PIN, gpio.OUT)
gpio.setup(ECHO_PIN, gpio.IN)


def get_distance():
    gpio.output(TRIG_PIN, False)
    time.sleep(1)
    
    gpio.output(TRIG_PIN, True)
    time.sleep(0.00001)
    gpio.output(TRIG_PIN, False)
    
    while gpio.input(ECHO_PIN) == 0 :
       pulse_start = time.time()
    
    while gpio.input(ECHO_PIN) == 1 :
       pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 36000
    distance = distance / 2
    distance = round(distance, 2)
    
    return distance
     

try :
   while True :
      distance = get_distance()
      print "Distance : ", distance, "cm"

except :
   print "except error, GPIO.cleanup()"
   gpio.cleanup()
          