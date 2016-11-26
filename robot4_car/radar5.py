from Tkinter import *
from math import cos, sin, pi
import time
import RPi.GPIO as gpio
import Adafruit_PCA9685


class Radar:
    def __init__(self, canvas, canvas_width):
        self.canvas = canvas
        self.indicator_angle = 0   # 0 ~ 180
        self.direction = "F"
        self.aft_angle = [0,0,0,0]
        self.rs_line = []
        self.rs_line_x = []
        self.rs_line_y = []

        FW = canvas_width    # FULL_WIDTH
        HW = FW / 2          # HALF_WIDTH
        AI = HW / 4          # ARC_INTERVAL
        
        self.HW = FW / 2          # HALF_WIDTH
        self.AI = HW / 4          # ARC_INTERVAL

        self.X0 = HW
        self.Y0 = HW
        self.RADIAN = HW
        

        ####################################################################################################
        # PCA9685 setting, Servo
        ####################################################################################################
        
        #Import the PCA9685 module.
        self.pwm = Adafruit_PCA9685.PCA9685()
        
        # Set frequency to 100 hz, good for servos.
        self.pwm.set_pwm_freq(100)      # between 40hz and 1000hz
        
        self.ULTR_PCA_PIN = 7
        
        # Configure min and max servo pulse lengths
        self.ULTR_PULSE_MIN =  210   # Min pulse length out of 4096
        self.ULTR_PULSE_MAX =  1100  # Max pulse length out of 4096
        self.ULTR_PULSE_MID =  610   # MID
    
        self.CurPulse_ultr = self.ULTR_PULSE_MIN
        self.pwm.set_pwm(self.ULTR_PCA_PIN, 0, self.CurPulse_ultr)
        time.sleep(1)
        


        ####################################################################################################
        # Ultra Sonic
        ####################################################################################################
        gpio.setmode(gpio.BOARD)   # BCM, BOARD
        self.TRIG_PIN = 18   #
        self.ECHO_PIN = 16   #
        gpio.setup(self.TRIG_PIN, gpio.OUT)
        gpio.setup(self.ECHO_PIN, gpio.IN)


        # Arc BackGround
        canvas.create_arc((4   , 4   , FW - 4   , FW - 4   ), start=0, extent=180, fill="black", outline="yellow green", width=1, tags="arc1")
        canvas.create_arc((AI*1, AI*1, FW - AI*1, FW - AI*1), start=0, extent=180, fill="black", outline="yellow green", width=1, tags="arc2")
        canvas.create_arc((AI*2, AI*2, FW - AI*2, FW - AI*2), start=0, extent=180, fill="black", outline="yellow green", width=1, tags="arc3")
        canvas.create_arc((AI*3, AI*3, FW - AI*3, FW - AI*3), start=0, extent=180, fill="black", outline="yellow green", width=1, tags="arc4")


        # result line
        for idx in range(180):
            self.rs_line_x.insert(idx, self.get_circum_x(idx))
            self.rs_line_y.insert(idx, self.get_circum_y(idx))
            self.rs_line.insert(idx, canvas.create_line(HW, HW, self.rs_line_x[idx], self.rs_line_y[idx], fill="red", width=3, state=HIDDEN))  # state=NORMAL, HIDDEN

        # Line BackGround
        canvas.create_line(HW, HW, self.get_circum_xy( 30), fill="yellow green", width=1, stipple="")  # 'gray75', 'gray50', 'gray25', 'gray12'
        canvas.create_line(HW, HW, self.get_circum_xy( 60), fill="yellow green")
        canvas.create_line(HW, HW, self.get_circum_xy( 90), fill="yellow green")
        canvas.create_line(HW, HW, self.get_circum_xy(120), fill="yellow green")
        canvas.create_line(HW, HW, self.get_circum_xy(150), fill="yellow green")

        # Text BackGround
        canvas.create_text(  20, HW+7, text="100cm", fill="yellow green")
        canvas.create_text(AI*1, HW+7, text= "75cm", fill="yellow green")
        canvas.create_text(AI*2, HW+7, text= "50cm", fill="yellow green")
        canvas.create_text(AI*3, HW+7, text= "25cm", fill="yellow green")
        
        self.t1=canvas.create_text(AI*5, HW+7, text= "Distance:  90cm", fill="yellow green", anchor=W)
        self.t2=canvas.create_text(AI*6, HW+7, text= "Angle: 150"     , fill="yellow green", anchor=W)

        # indicator
        self.indicator1 = self.canvas.create_line((HW, HW, self.get_circum_xy(130)), fill="green", width=3, stipple="")
        self.indicator2 = self.canvas.create_line((HW, HW, self.get_circum_xy(130)), fill="green", width=3, stipple="gray75")
        self.indicator3 = self.canvas.create_line((HW, HW, self.get_circum_xy(130)), fill="green", width=3, stipple="gray50")
        self.indicator4 = self.canvas.create_line((HW, HW, self.get_circum_xy(130)), fill="green", width=3, stipple="gray25")
        self.indicator5 = self.canvas.create_line((HW, HW, self.get_circum_xy(130)), fill="green", width=3, stipple="gray12")

    # get coordination circumference
    def get_circum_xy(self, angle):
        x = int(self.X0 + self.RADIAN * cos(angle * pi / 180))
        y = int(self.Y0 - self.RADIAN * sin(angle * pi / 180))
        return (x, y)
    def get_circum_x(self, angle):
        x = int(self.X0 + self.RADIAN * cos(angle * pi / 180))
        return x
    def get_circum_y(self, angle):
        y = int(self.Y0 - self.RADIAN * sin(angle * pi / 180))
        return y


    # get coordination circumference find thing
    def get_circum_find_x(self, angle, find_rate):
        x = int(self.X0 + self.RADIAN * find_rate * cos(angle * pi / 180))
        return (x)
    def get_circum_find_y(self, angle, find_rate):
        y = int(self.Y0 - self.RADIAN * find_rate * sin(angle * pi / 180))
        return (y)

    # Test
    def indicator_test(self):
        if self.indicator_angle >= 179:     #0 ~ 179
            self.direction = "R"  # Reverse
        if self.indicator_angle < 0:
            self.direction = "F"  # Forward

        # follow indigator
        self.aft_angle[3] = self.aft_angle[2]
        self.aft_angle[2] = self.aft_angle[1]
        self.aft_angle[1] = self.aft_angle[0]
        self.aft_angle[0] = self.indicator_angle
        if self.direction == "F":
            self.indicator_angle = self.indicator_angle + 1
        elif self.direction == "R":
            self.indicator_angle = self.indicator_angle - 1

        # indicator move
        new_x = self.rs_line_x[self.indicator_angle]
        new_y = self.rs_line_y[self.indicator_angle]
        self.canvas.coords(self.indicator1, (self.X0, self.Y0, new_x, new_y)) # change coordinates

        new_x = self.rs_line_x[self.aft_angle[0]]
        new_y = self.rs_line_y[self.aft_angle[0]]
        self.canvas.coords(self.indicator2, (self.X0, self.Y0, new_x, new_y))

        new_x = self.rs_line_x[self.aft_angle[1]]
        new_y = self.rs_line_y[self.aft_angle[1]]
        self.canvas.coords(self.indicator3, (self.X0, self.Y0, new_x, new_y))

        new_x = self.rs_line_x[self.aft_angle[2]]
        new_y = self.rs_line_y[self.aft_angle[2]]
        self.canvas.coords(self.indicator4, (self.X0, self.Y0, new_x, new_y))

        new_x = self.rs_line_x[self.aft_angle[3]]
        new_y = self.rs_line_y[self.aft_angle[3]]
        self.canvas.coords(self.indicator5, (self.X0, self.Y0, new_x, new_y))

        # find things
        if self.indicator_angle >= 110 and self.indicator_angle <= 150:
            if self.direction == "F":
                new_x1 = self.get_circum_find_x(self.indicator_angle, 0.2)
                new_y1 = self.get_circum_find_y(self.indicator_angle, 0.2)
                new_x2 = self.rs_line_x[self.indicator_angle]
                new_y2 = self.rs_line_y[self.indicator_angle]
                self.canvas.coords(self.rs_line[self.indicator_angle], (new_x1, new_y1, new_x2, new_y2))
                self.canvas.itemconfig(self.rs_line[self.indicator_angle], fill="red", state=NORMAL)
            elif self.direction == "R":
                self.canvas.itemconfig(self.rs_line[self.indicator_angle], fill="red", state=HIDDEN)
                #self.canvas.coords(self.rs_line[self.indicator_angle], (self.X0, self.Y0, self.get_circum_find_x[self.indicator_angle], self.get_circum_find_y[self.indicator_angle]))

        # indicator self move
        self.canvas.after(10, self.indicator_test)




    ##############################
    # serch
    ##############################
    def indicator_loop(self):        
        if self.indicator_angle >= 179:     #0 ~ 179
            self.direction = "R"  # Reverse
        if self.indicator_angle <= 0:
            self.direction = "F"  # Forward
        
        # follow indigator
        self.aft_angle[3] = self.aft_angle[2]
        self.aft_angle[2] = self.aft_angle[1]
        self.aft_angle[1] = self.aft_angle[0]
        self.aft_angle[0] = self.indicator_angle
        if self.direction == "F":
            self.indicator_angle = self.indicator_angle + 1
        elif self.direction == "R":
            self.indicator_angle = self.indicator_angle - 1
        
        # indicator move
        new_x = self.rs_line_x[self.indicator_angle]
        new_y = self.rs_line_y[self.indicator_angle]
        self.canvas.coords(self.indicator1, (self.X0, self.Y0, new_x, new_y)) # change coordinates
        
        new_x = self.rs_line_x[self.aft_angle[0]]
        new_y = self.rs_line_y[self.aft_angle[0]]
        self.canvas.coords(self.indicator2, (self.X0, self.Y0, new_x, new_y))
        
        new_x = self.rs_line_x[self.aft_angle[1]]
        new_y = self.rs_line_y[self.aft_angle[1]]
        self.canvas.coords(self.indicator3, (self.X0, self.Y0, new_x, new_y))
        
        new_x = self.rs_line_x[self.aft_angle[2]]
        new_y = self.rs_line_y[self.aft_angle[2]]
        self.canvas.coords(self.indicator4, (self.X0, self.Y0, new_x, new_y))
        
        new_x = self.rs_line_x[self.aft_angle[3]]
        new_y = self.rs_line_y[self.aft_angle[3]]
        self.canvas.coords(self.indicator5, (self.X0, self.Y0, new_x, new_y))
        
        
        # Servo move
        self.CurPulse_ultr = self.ULTR_PULSE_MIN + int((self.ULTR_PULSE_MAX - self.ULTR_PULSE_MIN) / 180 * self.indicator_angle)
        self.pwm.set_pwm(self.ULTR_PCA_PIN, 0, self.CurPulse_ultr)
        
        # get distance 
        distance=0
        distance = self.get_distance()
        print('[RadarWin] angle['+str(self.indicator_angle)+'], distance[' + str(distance) + '],   CurPulse_ultr: [' + str(self.CurPulse_ultr) + ']')


        # distance & angle text
        self.canvas.delete(self.t1)
        self.canvas.delete(self.t2)
        self.t1 = self.canvas.create_text(self.AI*5, self.HW+7, text= ("Distance: %3dcm" % distance)       , fill="yellow green", anchor=W)
        self.t2 = self.canvas.create_text(self.AI*6, self.HW+7, text= ("Angle: %3d" % self.indicator_angle), fill="yellow green", anchor=W)

        # find things
        self.canvas.itemconfig(self.rs_line[self.indicator_angle], fill="red", state=HIDDEN)   # find indicator init
        if distance <= 100:
            find_rate = distance * 0.01   # 100 percent rate
            new_x1 = self.get_circum_find_x(self.indicator_angle, find_rate)
            new_y1 = self.get_circum_find_y(self.indicator_angle, find_rate)
            new_x2 = self.rs_line_x[self.indicator_angle]
            new_y2 = self.rs_line_y[self.indicator_angle]
            self.canvas.coords(self.rs_line[self.indicator_angle], (new_x1, new_y1, new_x2, new_y2))
            self.canvas.itemconfig(self.rs_line[self.indicator_angle], fill="red", state=NORMAL)
            #if self.direction == "F":
            #elif self.direction == "R":
            #    self.canvas.itemconfig(self.rs_line[self.indicator_angle], fill="red", state=HIDDEN)
            #    #self.canvas.coords(self.rs_line[self.indicator_angle], (self.X0, self.Y0, self.get_circum_find_x[self.indicator_angle], self.get_circum_find_y[self.indicator_angle]))


        # indicator self move
        self.canvas.after(10, self.indicator_loop)
            
    
    def get_distance(self):
        pulse_start = 0
        pulse_end = 0
        pulse_duration = 0
        distance = 0
    
        gpio.output(self.TRIG_PIN, False)
        #time.sleep(1)
    
        gpio.output(self.TRIG_PIN, True)
        time.sleep(0.00001)
        gpio.output(self.TRIG_PIN, False)
    
        while gpio.input(self.ECHO_PIN) == 0 :
           pulse_start = time.time()
    
        while gpio.input(self.ECHO_PIN) == 1 :
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
    
    
    
# End Class



if __name__ == "__main__":
    root = Tk()
    root.title("Radar")
    root.resizable(False,False)

    CANVAS_WIDTH  = 1500
    CANVAS_HEIGHT = 800
    
    C = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="black")
    C.pack()
    
    
    # create Radar objects
    radar = Radar(C, CANVAS_WIDTH)
    
    # TEST
    #radar.indicator_test()
    
    # REAL
    radar.indicator_loop()
    
    
    root.mainloop()

