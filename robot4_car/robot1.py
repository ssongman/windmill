import RPi.GPIO as gpio
import time
import sys
#import Tkinter as tk
from Tkinter import *
import Adafruit_PCA9685
#from threading import Thread
import thread



####################################################################################################
# PCA9685 setting, Servo 
####################################################################################################

#Import the PCA9685 module.
pwm = Adafruit_PCA9685.PCA9685()

# Set frequency to 100 hz, good for servos.
pwm.set_pwm_freq(100)      # between 40hz and 1000hz

#led_gpio_pin = 18
PANS_PCA_PIN = 0
TILT_PCA_PIN = 3

# Configure min and max servo pulse lengths
SPAN_PULSE_MIN =  650  # Min pulse length out of 4096
SPAN_PULSE_MAX = 1000  # Max pulse length out of 4096
TILT_PULSE_MIN =  400  # Min pulse length out of 4096
TILT_PULSE_MAX = 1000  # Max pulse length out of 4096

MOVING_PULSE = 50

#MID_PULSE_PANS = (SPAN_PULSE_MIN + SPAN_PULSE_MAX) / 2
#MID_PULSE_TILT = (TILT_PULSE_MIN + TILT_PULSE_MAX) / 2
MID_PULSE_PANS = 850
MID_PULSE_TILT = 800

CurPulse_pans = MID_PULSE_PANS
CurPulse_tilt = MID_PULSE_TILT


#def AngleUp(event):
#    global CurPulse_tilt, CurPulse_pans
#    CurPulse_tilt -= MOVING_PULSE
#    if CurPulse_tilt < TILT_PULSE_MIN: CurPulse_tilt = TILT_PULSE_MIN
#    pwm.set_pwm(TILT_PCA_PIN, 0, CurPulse_tilt)
#    print 'Key: ', event.char, ', angle(pan,tilt) : ', CurPulse_pans, CurPulse_tilt
#
#def AngleDown(event):
#    global CurPulse_tilt, CurPulse_pans
#    CurPulse_tilt += MOVING_PULSE
#    if CurPulse_tilt > TILT_PULSE_MAX: CurPulse_tilt = TILT_PULSE_MAX
#    pwm.set_pwm(TILT_PCA_PIN, 0, CurPulse_tilt)
#    print 'Key: ', event.char, ', angle(pan,tilt) : ', CurPulse_pans, CurPulse_tilt
#
#def AngleLeft(event):
#    global CurPulse_tilt, CurPulse_pans
#    CurPulse_pans += MOVING_PULSE
#    if CurPulse_pans > SPAN_PULSE_MAX: CurPulse_pans = SPAN_PULSE_MAX
#    pwm.set_pwm(PANS_PCA_PIN, 0, CurPulse_pans)
#    print 'Key: ', event.char, ', angle(pan,tilt) : ', CurPulse_pans, CurPulse_tilt
#
#def AngleRight(event):
#    global CurPulse_tilt, CurPulse_pans
#    CurPulse_pans -= MOVING_PULSE
#    if CurPulse_pans < SPAN_PULSE_MIN: CurPulse_pans = SPAN_PULSE_MIN
#    pwm.set_pwm(PANS_PCA_PIN, 0, CurPulse_pans)
#    print 'Key: ', event.char, ', angle(pan,tilt) : ', CurPulse_pans, CurPulse_tilt
#
#def AngleCenter(event):
#    global CurPulse_tilt, CurPulse_pans
#    CurPulse_pans = MID_PULSE_PANS
#    CurPulse_tilt = MID_PULSE_TILT
#    pwm.set_pwm(PANS_PCA_PIN, 0, CurPulse_pans)
#    pwm.set_pwm(TILT_PCA_PIN, 0, CurPulse_tilt)
#    print 'Key: ', event.char, ', angle(pan,tilt) : ', CurPulse_pans, CurPulse_tilt







####################################################################################################
# Motor setting 
####################################################################################################
gpio.setmode(gpio.BOARD)   # BCM, BOARD

gpio.setup( 7, gpio.OUT)   # right
gpio.setup(11, gpio.OUT)   # right
gpio.setup(13, gpio.OUT)   #left
gpio.setup(15, gpio.OUT)   #left

pwm_RA = gpio.PWM( 7, 100)         # frequency = 100 Hz  # Right - A
pwm_RB = gpio.PWM(11, 100)         # frequency = 100 Hz  # Left  - B
pwm_LA = gpio.PWM(13, 100)         # frequency = 100 Hz  # Right - A
pwm_LB = gpio.PWM(15, 100)         # frequency = 100 Hz  # Left  - B
pwm_RA.start(0)
pwm_RB.start(0)
pwm_LA.start(0)
pwm_LB.start(0)

speed_cur = 100   # 0 to 100
run_direct = 'STOP'   # STOP,FORWARD,REVERSE,TURN_LEFT,TURN_RIGHT,PIVOT_LEFT,PIVOT_RIGHT



def KeyPress_S(event):
    print 'stop ', event.char
    stop()
    
def stop():
    global run_direct
    run_direct = 'STOP'
    pwm_RA.ChangeDutyCycle(0)                   # spped 0 to 100             #pwm_r.ChangeDutyCycle(100)
    pwm_RB.ChangeDutyCycle(0)                   # spped 0 to 100             #pwm_r.ChangeDutyCycle(100)
    pwm_LA.ChangeDutyCycle(0)                   # spped 0 to 100             #pwm_r.ChangeDutyCycle(100)
    pwm_LB.ChangeDutyCycle(0)                   # spped 0 to 100             #pwm_r.ChangeDutyCycle(100)



def KeyPress_W(event):
    print 'forward', event.char
    forward()

def forward():
    global run_direct
    print 'speed: ' + str(speed_cur)
    stop()
    run_direct = 'FORWARD'
    pwm_RA.ChangeDutyCycle(speed_cur)
    pwm_LA.ChangeDutyCycle(speed_cur)
    
    # when the car is forwarding, checking the distance using thread.
    #print 'thread is started to check the distance'
    #thread.start_new_thread(thread_forward_distance, ("Thread-1",))  
    
    #t1 = Thread( target=thread_forward_distance, args=("Thread-1", ) )    
    #t1.start()
    #t1.join()


def KeyPress_X(event):
    print 'reverse', event.char
    reverse()
    
def reverse():
    global run_direct
    print 'speed: ' + str(speed_cur)
    stop()
    run_direct = 'REVERSE'
    pwm_RB.ChangeDutyCycle(speed_cur)
    pwm_LB.ChangeDutyCycle(speed_cur)



def KeyPress_A(event):
    print 'turn_left', event.char
    turn_left()
    
def turn_left():
    global run_direct
    print 'speed: ' + str(speed_cur)
    stop()
    run_direct = 'TURN_LEFT'
    pwm_RA.ChangeDutyCycle(100)
    pwm_RB.ChangeDutyCycle(100)
    pwm_LA.ChangeDutyCycle(speed_cur)   
    pwm_LB.ChangeDutyCycle(0)  


def KeyPress_D(event):
    print 'turn_right', event.char
    turn_right()
    
def turn_right():
    global run_direct
    print 'speed: ' + str(speed_cur)
    stop()
    run_direct = 'TURN_RIGHT'
    pwm_RA.ChangeDutyCycle(speed_cur)  
    pwm_RB.ChangeDutyCycle(0)      
    pwm_LA.ChangeDutyCycle(100)
    pwm_LB.ChangeDutyCycle(100)



def KeyPress_Q(event):
    print 'pivot_left', event.char
    pivot_left()
    
def pivot_left():
    global run_direct
    print 'speed: ' + str(speed_cur)
    stop()
    run_direct = 'PIVOT_LEFT'
    pwm_RB.ChangeDutyCycle(speed_cur)
    pwm_LA.ChangeDutyCycle(speed_cur)



def KeyPress_E(event):
    print 'pivot_right', event.char
    pivot_right()
    
def pivot_right():
    global run_direct
    print 'speed: ' + str(speed_cur)
    stop()
    run_direct = 'PIVOT_RIGHT'
    pwm_RA.ChangeDutyCycle(speed_cur)
    pwm_LB.ChangeDutyCycle(speed_cur)



def thread_forward_distance(threadname):
    #global run_direct
    print '[thread_forward_distance] starting....'
    while True:
        if run_direct <> 'FORWARD':
            print '[thread_forward_distance] exit due to not forward... run_direct: ', run_direct
            break
            
        distance = get_distance()
        if distance == 0:
            pass   # skip because of ultra sonic error
        elif distance < 20:
            print '[thread_forward_distance] speed: 0, stop'
            stop()
            break
        elif distance < 40:
            print '[thread_forward_distance] speed: 40'
            pwm_RA.ChangeDutyCycle(40)
            pwm_LA.ChangeDutyCycle(40)
        elif distance < 60:
            print '[thread_forward_distance] speed : 60'
            pwm_RA.ChangeDutyCycle(60)
            pwm_LA.ChangeDutyCycle(60)
        elif distance < 80:
            print '[thread_forward_distance] speed : 80'
            pwm_RA.ChangeDutyCycle(80)
            pwm_LA.ChangeDutyCycle(80)
        elif distance >= 80:
            print '[thread_forward_distance] speed : 100'
            pwm_RA.ChangeDutyCycle(100)
            pwm_LA.ChangeDutyCycle(100)
        #end if
        
        time.sleep(0.2)
    #end wile
    


####################################################################################################
# Ultra Sonic
####################################################################################################
TRIG_PIN = 8    # 4th  BCM 14, BOARD : 8
ECHO_PIN = 10   # 5th  BCM 15, BOARD :10
gpio.setup(TRIG_PIN, gpio.OUT)
gpio.setup(ECHO_PIN, gpio.IN)

def KeyPress_T(event):
    get_distance()
     
def get_distance():
    pulse_start = 0
    pulse_end = 0
    pulse_duration = 0
    distance = 0
    
    gpio.output(TRIG_PIN, False)
    #time.sleep(1)
    
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
    
    print "Distance : ", distance, "cm"
    return distance
     


####################################################################################################
# Program Start
####################################################################################################
top = Tk()
top.title('robot test')

# =============================================================================
#add widgets RunBtn
# =============================================================================
frmRunBtn = Frame(top, border=1)
btnForward   = Button(frmRunBtn, width=10, height=3, text='Forward(W)'    )
btnReverse   = Button(frmRunBtn, width=10, height=3, text='Reverse(X)'    )
btnTurnLeft  = Button(frmRunBtn, width=10, height=3, text='Turn Left(A)'  )
btnTurnRight = Button(frmRunBtn, width=10, height=3, text='Turn Right(D)' )
btnPivotLeft = Button(frmRunBtn, width=10, height=3, text='Pivot Left(Q)' )
btnPivotRight= Button(frmRunBtn, width=10, height=3, text='Pivot Right(E)')
btnStop      = Button(frmRunBtn, width=10, height=3, text='Stop(S)'    )

# Bind the buttons with the corresponding callback function.
btnForward   .bind('<ButtonPress-1>', KeyPress_W )
btnReverse   .bind('<ButtonPress-1>', KeyPress_X )
btnTurnLeft  .bind('<ButtonPress-1>', KeyPress_A )
btnTurnRight .bind('<ButtonPress-1>', KeyPress_D )
btnPivotLeft .bind('<ButtonPress-1>', KeyPress_Q )
btnPivotRight.bind('<ButtonPress-1>', KeyPress_E )
btnStop      .bind('<ButtonPress-1>', KeyPress_S )
btnForward   .bind('<ButtonRelease-1>', KeyPress_S)   # When button0 is released, call the function stop_fun().
btnReverse   .bind('<ButtonRelease-1>', KeyPress_S)
btnTurnLeft  .bind('<ButtonRelease-1>', KeyPress_S)
btnTurnRight .bind('<ButtonRelease-1>', KeyPress_S)
btnPivotLeft .bind('<ButtonRelease-1>', KeyPress_S)
btnPivotRight.bind('<ButtonRelease-1>', KeyPress_S)

#use grid instead of pack
#btnUp   .pack()
#btnDown .pack()
#btnRight.pack()
#btnLeft .pack()

btnPivotLeft .grid(row=0, column=0)
btnForward   .grid(row=0, column=1)
btnPivotRight.grid(row=0, column=2)
btnTurnLeft  .grid(row=1, column=0)
btnStop      .grid(row=1, column=1)
btnTurnRight .grid(row=1, column=2)
btnReverse   .grid(row=2, column=1)

frmRunBtn.pack()

top.bind('<KeyPress-w>', KeyPress_W )
top.bind('<KeyPress-x>', KeyPress_X )
top.bind('<KeyPress-a>', KeyPress_A )
top.bind('<KeyPress-d>', KeyPress_D )
top.bind('<KeyPress-q>', KeyPress_Q )
top.bind('<KeyPress-e>', KeyPress_E )
top.bind('<KeyPress-s>', KeyPress_S )
#top.bind('<KeyRelease-w>', stop)
#top.bind('<KeyRelease-s>', stop)
#top.bind('<KeyRelease-a>', stop)
#top.bind('<KeyRelease-d>', stop)
#top.bind('<KeyRelease-q>', stop)
#top.bind('<KeyRelease-e>', stop)



# =============================================================================
#add widgets Speed
# =============================================================================
#speed_cur = 50

def changeSpeed(ev=None):
	tmp = 'speed'
	global speed_cur
	speed_cur = speed_scale.get()
	data = tmp + str(speed_cur)  # Change the integers into strings and combine them with the string 'speed'. 
	print 'sendData = %s' % data

label = Label(top, text='Speed:', fg='red')  # Create a label
#label.grid(row=3, column=0)                  # Label layout
label.pack()

speed_scale = Scale(top, from_=0, to=100, orient=HORIZONTAL, command=changeSpeed)  # Create a scale
speed_scale.set(50)
#speed.grid(row=3, column=1)
speed_scale.pack()



# =============================================================================
#add widgets angle value
# =============================================================================

# label
lb_angle_value = Label(top, width=15, text='angle value :')
# frame with text entry
fEntry = Frame(top, border='1', width=15)
en_angle_value = Entry(fEntry)

lb_angle_value.pack()
fEntry.pack()
en_angle_value.pack()



## =============================================================================
##add widgets Servo
## =============================================================================
#frmServoBtn = Frame(top, border=1)
#btnUp    = Button(frmServoBtn, width=7, height=3, text='Up(I)'    )
#btnDown  = Button(frmServoBtn, width=7, height=3, text='Down(K)'  )
#btnLeft  = Button(frmServoBtn, width=7, height=3, text='Left(J)'  )
#btnRight = Button(frmServoBtn, width=7, height=3, text='Right(L)' )
#btnCenter= Button(frmServoBtn, width=7, height=3, text='Center(M)')
#
#btnUp    .bind('<ButtonPress-1>', AngleUp    )
#btnDown  .bind('<ButtonPress-1>', AngleDown  )
#btnLeft  .bind('<ButtonPress-1>', AngleLeft  )
#btnRight .bind('<ButtonPress-1>', AngleRight )
#btnCenter.bind('<ButtonPress-1>', AngleCenter)
#
##use grid instead of pack
##btnUp   .pack()
##btnDown .pack()
##btnRight.pack()
##btnLeft .pack()
#
#btnUp    .grid(row=0, column=1)
#btnDown  .grid(row=2, column=1)
#btnRight .grid(row=1, column=2)
#btnLeft  .grid(row=1, column=0)
#btnCenter.grid(row=1, column=1)
#
#frmServoBtn.pack()
#
##top.bind('<KeyPress>', key_input)
#top.bind('<KeyPress-i>', AngleUp    )
#top.bind('<KeyPress-k>', AngleDown  )
#top.bind('<KeyPress-j>', AngleLeft  )
#top.bind('<KeyPress-l>', AngleRight )
#top.bind('<KeyPress-m>', AngleCenter)
#
#
#
## =============================================================================
##add widgets UltraSonic
## =============================================================================
#frmUltraSonicBtn = Frame(top, border=2)
#btnGetDis = Button(frmUltraSonicBtn, width=15, height=3, text='get_distance(T)'    )
#
#btnGetDis.bind('<ButtonPress-1>', KeyPress_T    )
#
##use grid instead of pack
##btnUp   .pack()
##btnDown .pack()
##btnRight.pack()
##btnLeft .pack()
#
#btnGetDis.grid(row=0, column=0)
#
#frmUltraSonicBtn.pack()
#
#top.bind('<KeyPress-t>', KeyPress_T)



top.mainloop()


# =============================================================================
# Program Start
# =============================================================================
print "Program Exit"
print "GPIO.cleanup()"
gpio.cleanup()



#forward(2)
#reverse(2)
#turn_left(2)
#turn_right(2)
#pivot_left(2)
#pivot_right(2)



#try:
#except :
#    print "except error, GPIO.cleanup()"
#    gpio.cleanup()
