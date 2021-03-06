####################################################################################################
# robot5.py
#
####################################################################################################

import RPi.GPIO as gpio
import time
import sys
import os    
#import Tkinter as tk
from Tkinter import *
import Adafruit_PCA9685
from threading import Thread
from opencv_camera import camera_view
#import thread



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


def AngleUp(event):
    global CurPulse_tilt, CurPulse_pans
    CurPulse_tilt -= MOVING_PULSE
    if CurPulse_tilt < TILT_PULSE_MIN: CurPulse_tilt = TILT_PULSE_MIN
    pwm.set_pwm(TILT_PCA_PIN, 0, CurPulse_tilt)
    print 'Key: ', event.char, ', angle(pan,tilt) : ', CurPulse_pans, CurPulse_tilt

def AngleDown(event):
    global CurPulse_tilt, CurPulse_pans
    CurPulse_tilt += MOVING_PULSE
    if CurPulse_tilt > TILT_PULSE_MAX: CurPulse_tilt = TILT_PULSE_MAX
    pwm.set_pwm(TILT_PCA_PIN, 0, CurPulse_tilt)
    print 'Key: ', event.char, ', angle(pan,tilt) : ', CurPulse_pans, CurPulse_tilt

def AngleLeft(event):
    global CurPulse_tilt, CurPulse_pans
    CurPulse_pans += MOVING_PULSE
    if CurPulse_pans > SPAN_PULSE_MAX: CurPulse_pans = SPAN_PULSE_MAX
    pwm.set_pwm(PANS_PCA_PIN, 0, CurPulse_pans)
    print 'Key: ', event.char, ', angle(pan,tilt) : ', CurPulse_pans, CurPulse_tilt

def AngleRight(event):
    global CurPulse_tilt, CurPulse_pans
    CurPulse_pans -= MOVING_PULSE
    if CurPulse_pans < SPAN_PULSE_MIN: CurPulse_pans = SPAN_PULSE_MIN
    pwm.set_pwm(PANS_PCA_PIN, 0, CurPulse_pans)
    print 'Key: ', event.char, ', angle(pan,tilt) : ', CurPulse_pans, CurPulse_tilt

def AngleCenter(event):
    global CurPulse_tilt, CurPulse_pans
    CurPulse_pans = MID_PULSE_PANS
    CurPulse_tilt = MID_PULSE_TILT
    pwm.set_pwm(PANS_PCA_PIN, 0, CurPulse_pans)
    pwm.set_pwm(TILT_PCA_PIN, 0, CurPulse_tilt)
    print 'Key: ', event.char, ', angle(pan,tilt) : ', CurPulse_pans, CurPulse_tilt




def CameraStream():
    
    # mode1 : opencv camera view                  # simple control, too slowly
    #print('opencv camera')
    #from opencv_camera import camera_view
    #camera_view()    
    
    # mode2 : opencv camera view using thread     # thread control but too slowly
    #from opencv_camera import camera_view
    #print('opencv camera')
    #t1 = Thread( target=camera_view, args=( ) )
    #t1.start()
    ##t1.join()
    
    # mode3 : gstream server open                 # simple control, so fast
    #gstream_server_respcam = "raspivid -fps 25 -h 720 -w 1080  -n -t 0 -b 200000 -o - | gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host=192.168.0.48 port=5000"
    #gstream_server_webcam  = "gst-launch-1.0 v4l2src device=/dev/video0 ! video/x-raw, framerate=15/1, width=640, height=480 ! omxh264enc ! rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host=192.168.0.48 port=5000"
    #
    #os.system(gstream_server_webcam)
    
    
    # mode4 : gstream server open, fork()         # thread control, so fast
    pid = os.fork()
    
    if pid == 0:   # child process
        print("[CameraWin] Child process pidx: [%s]    START" % os.getpid() )
        
        #gstream_server_respcam = "raspivid -fps 25 -h 720 -w 1080  -n -t 0 -b 200000 -o - | gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host=192.168.0.48 port=5000"
        gstream_server_webcam  = "gst-launch-1.0 v4l2src device=/dev/video0 ! video/x-raw, framerate=15/1, width=640, height=480 ! omxh264enc ! rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host=192.168.0.48 port=5000"
        
        os.system(gstream_server_webcam)
        
        print("Child process pidx: [%s]     END" % os.getpid() )
    
    else :
        #print("[CameraWin] before os.wait()")
        #os.wait()
        print("[CameraWin] Parent process pidx: [%s]" % pid )
        
        strCamSvr.set("process parent["+str(os.getpid())+"] child["+str(pid)+"]")

    
    return
#End CameraStream()



####################################################################################################
# Motor setting
####################################################################################################
gpio.setmode(gpio.BOARD)   # BCM, BOARD

gpio.setup(16, gpio.OUT)   # right
gpio.setup(11, gpio.OUT)   # right
gpio.setup(13, gpio.OUT)   #left
gpio.setup(15, gpio.OUT)   #left

pwm_RA = gpio.PWM(16, 100)         # frequency = 100 Hz  # Right - A
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

    #t1 = Thread( target=forward_distance_chk, args=( ) )
    #t1.start()
    ##t1.join()

def forward():
    global run_direct
    print 'speed: ' + str(speed_cur)
    stop()
    run_direct = 'FORWARD'
    pwm_RA.ChangeDutyCycle(speed_cur)
    pwm_LA.ChangeDutyCycle(speed_cur)


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




#def auto_pivot_left_180():
#    global run_direct
#    stop()
#    run_direct = 'AUTO_PIVOT_LEFT_90'
#    pwm_RB.ChangeDutyCycle(50)
#    pwm_LA.ChangeDutyCycle(50)
#    time.sleep(2.4)
#    stop()
#
#
#def auto_pivot_left_90():
#    global run_direct
#    stop()
#    run_direct = 'AUTO_PIVOT_LEFT_90'
#    pwm_RB.ChangeDutyCycle(50)
#    pwm_LA.ChangeDutyCycle(50)
#    time.sleep(1.2)
#    stop()
#
#def auto_pivot_left_45():
#    global run_direct
#    stop()
#    run_direct = 'AUTO_PIVOT_LEFT_45'
#    pwm_RB.ChangeDutyCycle(50)
#    pwm_LA.ChangeDutyCycle(50)
#    time.sleep(0.6)
#    stop()
#
#def auto_pivot_right_90():
#    global run_direct
#    stop()
#    run_direct = 'AUTO_PIVOT_RIGHT_90'
#    pwm_RA.ChangeDutyCycle(50)
#    pwm_LB.ChangeDutyCycle(50)
#    time.sleep(1.2)
#    stop()
#
#def auto_pivot_right_45():
#    global run_direct
#    stop()
#    run_direct = 'AUTO_PIVOT_RIGHT_45'
#    pwm_RA.ChangeDutyCycle(50)
#    pwm_LB.ChangeDutyCycle(50)
#    time.sleep(0.6)
#    stop()
#
#def auto_reverse():
#    global run_direct
#    stop()
#    run_direct = 'AUTO_REVERSE'
#    pwm_RB.ChangeDutyCycle(50)
#    pwm_LB.ChangeDutyCycle(50)
#    time.sleep(0.6)
#    stop()


####################################################################################################
# Ultra Sonic
####################################################################################################
TRIG_PIN = 8    # 4th  BCM 14, BOARD : 8
ECHO_PIN = 10   # 5th  BCM 15, BOARD :10
gpio.setup(TRIG_PIN, gpio.OUT)
gpio.setup(ECHO_PIN, gpio.IN)

def KeyPress_T(event):
    distance   = 0
    distance_f = 0
    distance_b = 0

    distance = get_distance()
    strDist = "D[" + str(distance) + "]cm"
    print(strDist)
    strDis.set(strDist)

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

    if distance <= 0:
        # Ultra Sonic error
        distance = 0
    elif distance >= 3000:
        # Ultra Sonic error
        distance = 3000

    return distance





####################################################################################################
# Program Start
####################################################################################################
top = Tk()
top.title('robot test')





# =============================================================================
# Drive
# =============================================================================
frmRunBtn = Frame(top, border=1)
btnForward   = Button(frmRunBtn, width=10, height=3, text='Forward(W)'    , bd=4)
btnReverse   = Button(frmRunBtn, width=10, height=3, text='Reverse(X)'    , bd=4)
btnTurnLeft  = Button(frmRunBtn, width=10, height=3, text='Turn Left(A)'  , bd=4)
btnTurnRight = Button(frmRunBtn, width=10, height=3, text='Turn Right(D)' , bd=4)
btnPivotLeft = Button(frmRunBtn, width=10, height=3, text='Pivot Left(Q)' , bd=4)
btnPivotRight= Button(frmRunBtn, width=10, height=3, text='Pivot Right(E)', bd=4)
btnStop      = Button(frmRunBtn, width=10, height=3, text='Stop(S)'       , bd=4)

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

Label(frmRunBtn, text='[Drive]', fg='black', font=20).grid(row=0, column=0, sticky='W', columnspan=3)
btnPivotLeft .grid(row=1, column=0)
btnForward   .grid(row=1, column=1)
btnPivotRight.grid(row=1, column=2)
btnTurnLeft  .grid(row=2, column=0)
btnStop      .grid(row=2, column=1)
btnTurnRight .grid(row=2, column=2)
btnReverse   .grid(row=3, column=1)

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


#frmRunBtn.pack()




# =============================================================================
# Camera Angle (Servo)
# =============================================================================
frmServoBtn = Frame(top, border=1)
btnUp    = Button(frmServoBtn, width=7, height=3, text='Up(I)'    , bd=4)
btnDown  = Button(frmServoBtn, width=7, height=3, text='Down(K)'  , bd=4)
btnLeft  = Button(frmServoBtn, width=7, height=3, text='Left(J)'  , bd=4)
btnRight = Button(frmServoBtn, width=7, height=3, text='Right(L)' , bd=4)
btnCenter= Button(frmServoBtn, width=7, height=3, text='Center(M)', bd=4)

btnUp    .bind('<ButtonPress-1>', AngleUp    )
btnDown  .bind('<ButtonPress-1>', AngleDown  )
btnLeft  .bind('<ButtonPress-1>', AngleLeft  )
btnRight .bind('<ButtonPress-1>', AngleRight )
btnCenter.bind('<ButtonPress-1>', AngleCenter)

#use grid instead of pack
#btnUp   .pack()
#btnDown .pack()
#btnRight.pack()
#btnLeft .pack()

Label(frmServoBtn, text='[Camera Angle]', fg='black', font=20).grid(row=0, column=0, sticky='W', columnspan=3)
btnUp    .grid(row=1, column=1)
btnLeft  .grid(row=2, column=0)
btnCenter.grid(row=2, column=1)
btnRight .grid(row=2, column=2)
btnDown  .grid(row=3, column=1)

#top.bind('<KeyPress>', key_inpuT)
top.bind('<KeyPress-i>', AngleUp    )
top.bind('<KeyPress-k>', AngleDown  )
top.bind('<KeyPress-j>', AngleLeft  )
top.bind('<KeyPress-l>', AngleRight )
top.bind('<KeyPress-m>', AngleCenter)

#frmServoBtn.pack(side=RIGHT)



# =============================================================================
# Speed
# =============================================================================
#speed_cur = 50

frmSpeed = Frame(top, border=1)
def changeSpeed(ev=None):
    tmp = 'speed'
    global speed_cur
    speed_cur = speed_scale.get()
    data = tmp + str(speed_cur)  # Change the integers into strings and combine them with the string 'speed'.
    print 'sendData = %s' % data
    if run_direct == 'FORWARD':
        forward()
    elif run_direct == 'REVERSE':
        reverse()

label = Label(frmSpeed, text='Speed:', fg='red')  # Create a label
#label.grid(row=3, column=0)                  # Label layout
label.pack()

speed_scale = Scale(frmSpeed, length=300, width=20, from_=0, to=100, orient=HORIZONTAL, tickinterval=20, command=changeSpeed)  # Create a scale  # , sliderlength=10
speed_scale.set(50)
#speed.grid(row=3, column=1)
speed_scale.pack()




# =============================================================================
# angle value
# =============================================================================
frmAngleValue = Frame(top, border=1)

angleVal=IntVar()
#txtval=StringVar()

# label
lb_angle_value = Label(frmAngleValue, width=15, text='angle value :')
# frame with text entry
en_angle_value = Entry(frmAngleValue, textvariable=angleVal, border='1', width=15, bd=20, insertwidth=1, font=30)

lb_angle_value.pack()
en_angle_value.pack()




# =============================================================================
# Auto Drive Mode
# =============================================================================
fromAutoPilot = Frame(top)  # bd=3, relief=RAISED, width= 150, height=100)
DriveMode=0                 # 0:MenualMode,  1: AutoMode

def AutoPilot():
    global DriveMode
    while (DriveMode == 1):
        intDirection = 0
        while (DriveMode == 1 and intDirection <> 2 ):
            ## SerchDirection
            #intDirection = SerchDirection()
            intDirection = 2
            if DriveMode <> 1: break

            if   intDirection == 0 :  # RIGHT
                strDir.set("Direction : RIGHT")
                auto_pivot_right_90()
            elif intDirection == 1 :  # MID-RIGHT
                strDir.set("Direction : MID-RIGHT")
                auto_pivot_right_45()
            elif intDirection == 2 :  # MIDDLE
                strDir.set("Direction : MIDDLE")
                #forward()
            elif intDirection == 3 :  # LEFT-MID
                strDir.set("Direction : LEFT-MID")
                auto_pivot_left_45()
            elif intDirection == 4 :  # LEFT
                strDir.set("Direction : LEFT")
                auto_pivot_left_90()
            elif intDirection == 5 :  # REVERSE
                strDir.set("Direction : REVERSE")

                #auto_reverse()
                reverse()
                reverse_distance_chk()

            elif intDirection == 6 :  # LEFT_180
                strDir.set("Direction : LEFT_180")
                auto_pivot_left_180()
            #End if
            time.sleep(1)
        # End while

        if DriveMode <> 1: break

        forward()
        forward_distance_chk()

        if DriveMode <> 1: break

        print("[AutoPilot] auto dirve ")
        time.sleep(1)

    # End while
    print("[AutoPilot] AutoPilot END ")
    strModetxt.set("AutoPilot END")



def AutoStart():
    global DriveMode
    if  DriveMode == 1:
        strModetxt.set("AutoPilot Starting....")
        return

    strModetxt.set("AutoPilot Starting...")

    DriveMode=1
    thread1 = Thread( target=AutoPilot, args=() )
    thread1.start()
    #thread1.join()


def AutoStop():
    global DriveMode
    strModetxt.set("AutoPilot ending...")

    DriveMode=0
    thread1 = Thread( target=AutoPilot, args=() )
    thread1.start()
    #thread1.join()
    #auto_pivot_left_45()   # test

strModetxt  =StringVar()
strDirection=StringVar()
Label (fromAutoPilot, text='[AutoPilot Mode]', fg='black', font=20).grid(row=0, column=0, sticky='W', columnspan=2)
Button(fromAutoPilot, text="Start", font=20, width=10, height=3, command=AutoStart).grid(row=1, column=0, sticky=W+E+N+S, padx=5, pady=5)
Button(fromAutoPilot, text="Stop" , font=20, width=10, height=3, command=AutoStop ).grid(row=1, column=1, sticky=W+E+N+S, padx=5, pady=5)
lbAuto = Label(fromAutoPilot, text='Drive Mode : Menual', font=30, fg='red', textvariable=strModetxt  ).grid(row=2, column=0, columnspan=2)
lbDire = Label(fromAutoPilot, text='Direction: forward' , font=10, fg='red', textvariable=strDirection).grid(row=3, column=0, columnspan=2)




# =============================================================================
# UltraSonic
# =============================================================================
frmUltraSonicBtn = Frame(top) #, bd=3, relief=RAISED)

#def changeUltSer(ev=None):
#    scUltSer_val = scUltSer.get()
#    print('UltraServo Angle Value : ' + str(scUltSer_val) )
#    pwm.set_pwm(ULTR_PCA_PIN, 0, scUltSer_val)

strDis=StringVar()
strDir=StringVar()
strCamSvr=StringVar()

lbTitle   = Label (frmUltraSonicBtn, text='[UltraSonic]'      , fg='black', font=20) #, width=30, justify=LEFT)
#scUltSer  = Scale (frmUltraSonicBtn, length=300, width=20, from_=200, to=1050, orient=HORIZONTAL, tickinterval=200, command=changeUltSer)  # Create a scale  # sliderlength=10,
btnGetDis = Button(frmUltraSonicBtn, text='get_distance(T)'   , fg="black", bd=3, height=2, width=15)
lbDis     = Label (frmUltraSonicBtn, text='Distance : 9999cm' , fg="red"  , font=5, justify=LEFT, textvariable=strDis )
#btnSerch  = Button(frmUltraSonicBtn, text="SerchDirection"   , fg="black", bd=3, height=2, width=15, command=SerchDirection)
lbDir     = Label (frmUltraSonicBtn, text='Dircection : MID'  , fg="red"  , font=20, justify=LEFT, bd=3, textvariable=strDir)
btnCamSvr  = Button(frmUltraSonicBtn, text="Camera Stream"    , fg="black", bd=3, height=2, width=15, command=CameraStream)
lbCamSvr   = Label (frmUltraSonicBtn, text=''                 , fg="red"  , font=20, justify=LEFT, bd=3, textvariable=strCamSvr )
#btnRadar  = Button(frmUltraSonicBtn, text="Radar"            , fg="black", bd=3, height=2, width=15, command=RadarWin)
#lbRadar   = Label (frmUltraSonicBtn, text=''                 , fg="red"  , font=20, justify=LEFT, bd=3)

btnGetDis.bind('<ButtonPress-1>', KeyPress_T    )
top.bind('<KeyPress-t>', KeyPress_T)
#scUltSer.set(ULTR_PULSE_MID)

lbTitle  .grid(row=0, column=0, sticky='W')
#scUltSer .grid(row=1, column=0, sticky='W', columnspan=2)
btnGetDis.grid(row=2, column=0) #, sticky='W')
lbDis    .grid(row=2, column=1) #, sticky='W')
#btnSerch .grid(row=3, column=0, padx=5, pady=5) #, sticky='W')
lbDir    .grid(row=3, column=1) #, sticky='W')
btnCamSvr .grid(row=4, column=0) #, sticky='W')
lbCamSvr  .grid(row=4, column=1) #, sticky='W')
#btnRadar .grid(row=4, column=0) #, sticky='W')
#lbRadar  .grid(row=4, column=1) #, sticky='W')


strDis.set("Distance : ____cm")
strCamSvr.set("process parent[] child[] ")

#frmUltraSonicBtn.pack()








# =============================================================================
# window start
# =============================================================================
lbTemp=Label(top, text='', width=10)

frmRunBtn       .grid(row=0, column=0, sticky='W')
lbTemp          .grid(row=0, column=1, sticky='W')
frmServoBtn     .grid(row=0, column=2, sticky='W')

frmSpeed        .grid(row=2, column=0, sticky='W')
frmAngleValue   .grid(row=2, column=2, sticky='W')

Label(top, width=10).grid(row=3, column=0)

fromAutoPilot        .grid(row=4, column=0, sticky='W')
frmUltraSonicBtn.grid(row=4, column=2, sticky='W')

#top.geometry("1000x500")
top.geometry("900x600+400+50")
top.mainloop()


# =============================================================================
# Program Exit
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
