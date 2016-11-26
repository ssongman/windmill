# pan_tilt_control.py
import RPi.GPIO as GPIO
import sys
from Tkinter import *

GPIO.setmode(GPIO.BOARD)      # BCM, BOARD  use GPIO pin numbering, not physical pin numbering

#led_gpio_pin = 18
pans_gpio_pin = 16
tilt_gpio_pin = 18

#GPIO.setup(led_gpio_pin, GPIO.OUT)
GPIO.setup(pans_gpio_pin, GPIO.OUT)
GPIO.setup(tilt_gpio_pin, GPIO.OUT)

pwmObject_pans = GPIO.PWM(pans_gpio_pin, 100)         # frequency = 100 Hz
pwmObject_tilt = GPIO.PWM(tilt_gpio_pin, 100)         # frequency = 100 Hz

pwmObject_pans.start(14)             # initial duty cycle = 14%
pwmObject_tilt.start(14)             # initial duty cycle = 14%

CurAngle_pans = 85
CurAngle_tilt = 45


##############################################################
# create top window
top = Tk()
top.title('pan tilt control test')


def angleToduty(angle):
    dutyCycle = ((float(angle) * 0.01) + 0.5) * 10
    return dutyCycle


def AngleUp(event):
    global CurAngle_tilt, CurAngle_pans
    CurAngle_tilt -= 10
    pwmObject_tilt.ChangeDutyCycle(angleToduty(CurAngle_tilt))
    print 'Key: ', event.char, ', angle(pan,tilt) : ', CurAngle_pans, CurAngle_tilt

def AngleDown(event):
    global CurAngle_tilt, CurAngle_pans
    CurAngle_tilt += 10
    pwmObject_tilt.ChangeDutyCycle(angleToduty(CurAngle_tilt))
    print 'Key: ', event.char, ', angle(pan,tilt) : ', CurAngle_pans, CurAngle_tilt

def AngleLeft(event):
    global CurAngle_tilt, CurAngle_pans
    CurAngle_pans += 10
    pwmObject_pans.ChangeDutyCycle(angleToduty(CurAngle_pans))
    print 'Key: ', event.char, ', angle(pan,tilt) : ', CurAngle_pans, CurAngle_tilt

def AngleRight(event):
    global CurAngle_tilt, CurAngle_pans
    CurAngle_pans -= 10
    pwmObject_pans.ChangeDutyCycle(angleToduty(CurAngle_pans))
    print 'Key: ', event.char, ', angle(pan,tilt) : ', CurAngle_pans, CurAngle_tilt

def AngleCenter(event):
    global CurAngle_tilt, CurAngle_pans
    CurAngle_pans = 85
    CurAngle_tilt = 45
    pwmObject_pans.ChangeDutyCycle(angleToduty(CurAngle_pans))
    pwmObject_tilt.ChangeDutyCycle(angleToduty(CurAngle_tilt))
    print 'Key: ', event.char, ', angle(pan,tilt) : ', CurAngle_pans, CurAngle_tilt

#def key_input(event):
#    global CurAngle_tilt, CurAngle_pans
#    key_press = event.char
#
#    if key_press.lower() == 'i':
#        CurAngle_tilt -= 10
#        pwmObject_tilt.ChangeDutyCycle(angleToduty(CurAngle_tilt))
#    elif key_press.lower() == 'k':
#        CurAngle_tilt += 10
#        pwmObject_tilt.ChangeDutyCycle(angleToduty(CurAngle_tilt))
#    elif key_press.lower() == 'j':
#        CurAngle_pans += 10
#        pwmObject_pans.ChangeDutyCycle(angleToduty(CurAngle_pans))
#    elif key_press.lower() == 'l':
#        CurAngle_pans -= 10
#        pwmObject_pans.ChangeDutyCycle(angleToduty(CurAngle_pans))
#    # end if
#    print 'Key: ', event.char, ', angle(pan,tilt) : ', CurAngle_pans, CurAngle_tilt



def main():
    pwmObject_tilt.ChangeDutyCycle(angleToduty(CurAngle_tilt))
    pwmObject_pans.ChangeDutyCycle(angleToduty(CurAngle_pans))

    #add widgets
    fButtons = Frame(top, border=1)
    btnUp    = Button(fButtons, width=7, height=3, text='Up(I)'    )
    btnDown  = Button(fButtons, width=7, height=3, text='Down(K)'  )
    btnLeft  = Button(fButtons, width=7, height=3, text='Left(J)'  )
    btnRight = Button(fButtons, width=7, height=3, text='Right(L)' )
    btnCenter= Button(fButtons, width=7, height=3, text='Center(M)')

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

    btnUp    .grid(row=0, column=1)
    btnDown  .grid(row=2, column=1)
    btnRight .grid(row=1, column=2)
    btnLeft  .grid(row=1, column=0)
    btnCenter.grid(row=1, column=1)
    
    fButtons.pack()

    #top.bind('<KeyPress>', key_input)
    top.bind('<KeyPress-i>', AngleUp    )
    top.bind('<KeyPress-k>', AngleDown  )
    top.bind('<KeyPress-j>', AngleLeft  )
    top.bind('<KeyPress-l>', AngleRight )
    top.bind('<KeyPress-m>', AngleCenter)
    
    # label
    lb_angle_value = Label(top, width=15, text='angle value :')
    # frame with text entry
    fEntry = Frame(top, border='1', width=15)
    en_angle_value = Entry(fEntry)
    
    lb_angle_value.pack()
    fEntry.pack()
    en_angle_value.pack()
    
    
    #mainloop
    top.mainloop()

    pwmObject_pans.stop()
    pwmObject_tilt.stop()
    print "except GPIO.cleanup()"
    GPIO.cleanup()

if __name__ == '__main__':
    main()




'''
###################################################################################################
def main():

    try:

    except KeyboardInterrupt:
       pwmObject_pans.stop()
       pwmObject_tilt.stop()
       print "except GPIO.cleanup()"
       GPIO.cleanup()


    return

###################################################################################################
if __name__ == "__main__":
    global CurAngle_tilt, CurAngle_pans
    pwmObject_pans.ChangeDutyCycle(angleToduty(CurAngle_pans))
    pwmObject_tilt.ChangeDutyCycle(angleToduty(CurAngle_tilt))

    main()
    pwmObject_pans.stop()
    pwmObject_tilt.stop()
    print "main GPIO.cleanup()"
    GPIO.cleanup()
'''





