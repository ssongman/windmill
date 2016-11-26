import RPi.GPIO as gpio
import time
import sys
#import Tkinter as tk
from Tkinter import *

gpio.setmode(gpio.BOARD)   # BCM, BOARD

# right
gpio.setup( 7, gpio.OUT)
gpio.setup(11, gpio.OUT)    # speed
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)

# left
gpio.setup(31, gpio.OUT)
gpio.setup(33, gpio.OUT)    # speed
gpio.setup(35, gpio.OUT)
gpio.setup(37, gpio.OUT)



def forward(event):
    print 'forward:', event.char
    gpio.output( 7, True)
    gpio.output(11, True)
    gpio.output(31, True)
    gpio.output(33, True)
    #pwm_r = gpio.PWM(11, 100)         # frequency = 100 Hz
    #pwm_l = gpio.PWM(33, 100)         # frequency = 100 Hz
    #pwm_r.start(70)                   # spped 0 to 100             #pwm_r.ChangeDutyCycle(100)
    #pwm_l.start(70)                   # spped 0 to 100             #pwm_r.ChangeDutyCycle(100)

    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(35, True)
    gpio.output(37, False)

def reverse(event):
    print 'reverse', event.char
    gpio.output( 7, True)
    gpio.output(11, True)
    gpio.output(31, True)
    gpio.output(33, True)

    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(35, False)
    gpio.output(37, True)

def turn_left(event):
    print 'turn_left', event.char
    gpio.output( 7, True)
    gpio.output(11, True)
    gpio.output(31, True)
    gpio.output(33, True)

    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(35, False)
    gpio.output(37, False)

def turn_right(event):
    print 'turn_right', event.char
    gpio.output( 7, True)
    gpio.output(11, True)
    gpio.output(31, True)
    gpio.output(33, True)

    gpio.output(13, False)
    gpio.output(15, False)
    gpio.output(35, True)
    gpio.output(37, False)

def pivot_left(event):
    print 'pivot_left', event.char
    gpio.output( 7, True)
    gpio.output(11, True)
    gpio.output(31, True)
    gpio.output(33, True)

    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(35, False)
    gpio.output(37, True)

def pivot_right(event):
    print 'pivot_right', event.char
    gpio.output( 7, True)
    gpio.output(11, True)
    gpio.output(31, True)
    gpio.output(33, True)

    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(35, True)
    gpio.output(37, False)
    
def stop(event):
    print 'stop', event.char
    gpio.output( 7, True)
    gpio.output(11, True)
    gpio.output(31, True)
    gpio.output(33, True)

    gpio.output(13, False)
    gpio.output(15, False)
    gpio.output(35, False)
    gpio.output(37, False)


# =============================================================================
# Program Start
# =============================================================================
top = Tk()
top.title('robot test')

#add widgets
fButtons = Frame(top, border=1)
btnForward   = Button(fButtons, width=10, height=3, text='Forward(W)'    )
btnReverse   = Button(fButtons, width=10, height=3, text='Reverse(S)'    )
btnTurnLeft  = Button(fButtons, width=10, height=3, text='Turn Left(A)'  )
btnTurnRight = Button(fButtons, width=10, height=3, text='Turn Right(D)' )
btnPivotLeft = Button(fButtons, width=10, height=3, text='Pivot Left(Q)' )
btnPivotRight= Button(fButtons, width=10, height=3, text='Pivot Right(E)')

# =============================================================================
# Bind the buttons with the corresponding callback function.
# =============================================================================
btnForward   .bind('<ButtonPress-1>', forward    )
btnReverse   .bind('<ButtonPress-1>', reverse    )
btnTurnLeft  .bind('<ButtonPress-1>', turn_left  )
btnTurnRight .bind('<ButtonPress-1>', turn_right )
btnPivotLeft .bind('<ButtonPress-1>', pivot_left )
btnPivotRight.bind('<ButtonPress-1>', pivot_right)
btnForward   .bind('<ButtonRelease-1>', stop)   # When button0 is released, call the function stop_fun().
btnReverse   .bind('<ButtonRelease-1>', stop)
btnTurnLeft  .bind('<ButtonRelease-1>', stop)
btnTurnRight .bind('<ButtonRelease-1>', stop)
btnPivotLeft .bind('<ButtonRelease-1>', stop)
btnPivotRight.bind('<ButtonRelease-1>', stop)

#use grid instead of pack
#btnUp   .pack()
#btnDown .pack()
#btnRight.pack()
#btnLeft .pack()

btnPivotLeft .grid(row=0, column=0)
btnForward   .grid(row=0, column=1)
btnPivotRight.grid(row=0, column=2)
btnTurnLeft  .grid(row=1, column=0)
btnReverse   .grid(row=1, column=1)
btnTurnRight .grid(row=1, column=2)

fButtons.pack()

top.bind('<KeyPress-w>', forward    )
top.bind('<KeyPress-x>', reverse    )
top.bind('<KeyPress-a>', turn_left  )
top.bind('<KeyPress-d>', turn_right )
top.bind('<KeyPress-q>', pivot_left )
top.bind('<KeyPress-e>', pivot_right)
top.bind('<KeyPress-s>', stop)
#top.bind('<KeyRelease-w>', stop)
#top.bind('<KeyRelease-s>', stop)
#top.bind('<KeyRelease-a>', stop)
#top.bind('<KeyRelease-d>', stop)
#top.bind('<KeyRelease-q>', stop)
#top.bind('<KeyRelease-e>', stop)

# label
lb_angle_value = Label(top, width=15, text='angle value :')
# frame with text entry
fEntry = Frame(top, border='1', width=15)
en_angle_value = Entry(fEntry)

lb_angle_value.pack()
fEntry.pack()
en_angle_value.pack()
    
top.mainloop()


# =============================================================================
# Program Start
# =============================================================================
print "Program Exit - GPIO.cleanup()"
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
