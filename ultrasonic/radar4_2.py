from Tkinter import *
from math import cos, sin, pi
import time

CANVAS_WIDTH  = 1500
CANVAS_HEIGHT = 800


class Radar:
    def __init__(self, canvas, canvas_width):
        self.canvas = canvas
        self.indicator_angle = 0   # 0 ~ 180
        self.test_dir = "F"
        self.aft_angle = [0,0,0,0]
        self.rs_line = []
        self.rs_line_x = []
        self.rs_line_y = []

        FW = canvas_width    # FULL_WIDTH
        HW = FW / 2          # HALF_WIDTH
        AI = HW / 4          # ARC_INTERVAL

        self.X0 = HW
        self.Y0 = HW
        self.RADIAN = HW

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
        canvas.create_text(  20, HW+7, text="40cm", fill="yellow green")
        canvas.create_text(AI*1, HW+7, text="30cm", fill="yellow green")
        canvas.create_text(AI*2, HW+7, text="20cm", fill="yellow green")
        canvas.create_text(AI*3, HW+7, text="10cm", fill="yellow green")

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


    def indicator_test(self):
        if self.indicator_angle >= 179:     #0 ~ 179
            self.test_dir = "R"  # Reverse
        if self.indicator_angle < 0:
            self.test_dir = "F"  # Forward

        self.aft_angle[3] = self.aft_angle[2]
        self.aft_angle[2] = self.aft_angle[1]
        self.aft_angle[1] = self.aft_angle[0]
        self.aft_angle[0] = self.indicator_angle
        if self.test_dir == "F":
            self.indicator_angle = self.indicator_angle + 1
        elif self.test_dir == "R":
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
            if self.test_dir == "F":
                new_x1 = self.get_circum_find_x(self.indicator_angle, 0.2)
                new_y1 = self.get_circum_find_y(self.indicator_angle, 0.2)
                new_x2 = self.rs_line_x[self.indicator_angle]
                new_y2 = self.rs_line_y[self.indicator_angle]
                self.canvas.coords(self.rs_line[self.indicator_angle], (new_x1, new_y1, new_x2, new_y2))
                self.canvas.itemconfig(self.rs_line[self.indicator_angle], fill="red", state=NORMAL)
            elif self.test_dir == "R":
                self.canvas.itemconfig(self.rs_line[self.indicator_angle], fill="red", state=HIDDEN)
                #self.canvas.coords(self.rs_line[self.indicator_angle], (self.X0, self.Y0, self.get_circum_find_x[self.indicator_angle], self.get_circum_find_y[self.indicator_angle]))

        # indicator self move
        self.canvas.after(10, self.indicator_test)

# End Class

root = Tk()
root.title("Radar")
root.resizable(False,False)

C = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="black")
C.pack()


# create Radar objects
radar = Radar(C, CANVAS_WIDTH)
radar.indicator_test()

root.mainloop()

