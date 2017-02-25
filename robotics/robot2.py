import RPi.GPIO as gpio
import time



def init():
    gpio.setmode(gpio.BOARD)   # BCM, BOARD
    
    # right
    gpio.setup( 7, gpio.OUT)
    gpio.setup(11, gpio.OUT)    # speed
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

    #left
    gpio.setup(31, gpio.OUT)
    gpio.setup(33, gpio.OUT)    # speed
    gpio.setup(35, gpio.OUT)
    gpio.setup(37, gpio.OUT)
    
def forward(tf):
    init()
    print 'forward'
    gpio.output( 7, True)
    gpio.output(33, True)
    #pwm_r = gpio.PWM(11, 100)         # frequency = 100 Hz
    #pwm_l = gpio.PWM(33, 100)         # frequency = 100 Hz
    #pwm_r.start(70)                   # spped 0 to 100             #pwm_r.ChangeDutyCycle(100)
    #pwm_l.start(70)                   # spped 0 to 100             #pwm_r.ChangeDutyCycle(100)
    
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(35, True)
    gpio.output(37, False)
    time.sleep(tf)
    gpio.cleanup()

def reverse(tf):
    init()
    print 'reverse'
    gpio.output( 7, True)
    gpio.output(33, True)
    
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(35, False)
    gpio.output(37, True)
    time.sleep(tf)
    gpio.cleanup()

def turn_left(tf):
    init()
    print 'turn_left'
    gpio.output( 7, True)
    gpio.output(33, True)
    
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(35, False)
    gpio.output(37, False)
    time.sleep(tf)
    gpio.cleanup()

def turn_right(tf):
    init()
    print 'turn_right'
    gpio.output( 7, True)
    gpio.output(33, True)
    
    gpio.output(13, False)
    gpio.output(15, False)
    gpio.output(35, True)
    gpio.output(37, False)
    time.sleep(tf)
    gpio.cleanup()

def pivot_left(tf):
    init()
    print 'pivot_left'
    gpio.output( 7, True)
    gpio.output(33, True)
    
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(35, False)
    gpio.output(37, True)
    time.sleep(tf)
    gpio.cleanup()

def pivot_right(tf):
    init()
    print 'pivot_right'
    gpio.output( 7, True)
    gpio.output(33, True)
    
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(35, True)
    gpio.output(37, False)
    time.sleep(tf)
    gpio.cleanup()


#forward(2)
#reverse(2)
#turn_left(2)
#turn_right(2)
pivot_left(2)
pivot_right(2)



#try:
#except :
#    print "except error, GPIO.cleanup()"
#    gpio.cleanup()
