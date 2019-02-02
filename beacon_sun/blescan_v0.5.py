###################################################
#
# File name   : blescan_v0.5.py
# Execution   : python3 blescan_v0.5.py
# Description : 
#         v0.5: GUI Setting
#
###################################################

#########[python 2.x]###########
#from Tkinter import *

#########[python 3.x]###########
from tkinter import *




class App:

   def __init__(self, master):
      ##############################################################
      #[Variable ]
      ##############################################################
      self.dBleMajor        = DoubleVar();   self.dBleMajor      .set(501)                     
      self.dBleMinor        = DoubleVar();   self.dBleMinor      .set(20781)                   
      self.dDisDepth        = DoubleVar();   self.dDisDepth      .set(10)      # queue         
      self.dMeasureFreq     = DoubleVar();   self.dMeasureFreq   .set(1)       # second        
      self.dAllowTolerance  = DoubleVar();   self.dAllowTolerance.set(10)      # percent
      self.intLimitRange    = IntVar()   ;   self.intLimitRange  .set(5)       # Limit Distance   
      self.dRealTx          = DoubleVar();   self.dRealTx        .set(0)       # 
      self.dRealRssi        = DoubleVar();   self.dRealRssi      .set(0)       #
      self.dRealDistance    = DoubleVar();   self.dRealDistance  .set(0)       #
      self.dAftDis          = DoubleVar();   self.dAftDis        .set(0)       #
      self.dAftQueue        = DoubleVar();   self.dAftQueue      .set(0)       #
      self.dAftAverDis      = DoubleVar();   self.dAftAverDis    .set(0)       #
      self.intResultRange   = DoubleVar();   self.intResultRange .set(0)       #
      


      ##############################################################
      #[Setting Frame]
      ##############################################################
      frmSetting = Frame(master, border=2)
      frmSetting .grid(row=0, column=0, sticky='W')
      #frmSetting.pack()

      #Label (frmTestlable, text="first value : " , bg="gray").grid(row=0, column=0, sticky=E)
      #Label (frmTestlable, text="second value : ", bg="gray").grid(row=0, column=0, sticky=E)
      #label1=Label(frmTestlable, text="first value : " , bg="gray").place(x=20, y=20)
      #label2=Label(frmTestlable, text="second value : ", bg="gray").place(x=20, y=40)
      #label1=Label(frmSetting, width=10, height=2, text="BLE infomation" , bd=2).grid(row=0, column=0)
      #label1=Label(frmSetting, width=10, height=2, text="BLE infomation" , bd=2).grid(row=0, column=0)

      Label(frmSetting, text="<< Setting >>"  , bd=2).grid(row=0, column=0)

      Label(frmSetting, text="BLE infomation" , bd=2).grid(row=1, column=0, sticky=W)
      Label(frmSetting, text="Major"          , bd=2).grid(row=1, column=1, sticky=E);  Entry(frmSetting, justify="center", textvariable=self.dBleMajor).grid(row=1, column=2, sticky=E)
      Label(frmSetting, text="Minor"          , bd=2).grid(row=1, column=3, sticky=E);  Entry(frmSetting, justify="center", textvariable=self.dBleMinor).grid(row=1, column=4, sticky=E)
      
      Label(frmSetting, text=" ", bd=2).grid(row=3, column=1, columnspan=5, sticky=W)

      # correction criterion
      Label(frmSetting, text="Correction Criterion" , bd=2).grid(row=4, column=0, sticky=W)
      Label(frmSetting, text="Dis. Depth"           , bd=2).grid(row=4, column=1, sticky=E);  Entry(frmSetting, justify="center", textvariable=self.dDisDepth      ).grid(row=4, column=2, sticky=E); Label(frmSetting, text="(queue)").grid(row=4, column=3, sticky=W, columnspan=2);
      Label(frmSetting, text="Measure Frequency"    , bd=2).grid(row=5, column=1, sticky=E);  Entry(frmSetting, justify="center", textvariable=self.dMeasureFreq   ).grid(row=5, column=2, sticky=E); Label(frmSetting, text="second" ).grid(row=5, column=3, sticky=W, columnspan=2);
      Label(frmSetting, text="Allowable Tolerance"  , bd=2).grid(row=6, column=1, sticky=E);  Entry(frmSetting, justify="center", textvariable=self.dAllowTolerance).grid(row=6, column=2, sticky=E); Label(frmSetting, text="percent").grid(row=6, column=3, sticky=W, columnspan=2);
      Label(frmSetting, text="this section is in order to reduce the error distance ").grid(row=7, column=1, sticky=W, columnspan=3)

      Label(frmSetting, text=" ", bd=2).grid(row=8, column=1, columnspan=5, sticky=W)

      # Limit distance
      Label(frmSetting, text="Limit distance", bd=2).grid(row=9, column=0, sticky=W)
      Label(frmSetting, text="Range"         , bd=2).grid(row=9, column=1, sticky=E);  Entry(frmSetting, justify="center", textvariable=self.intLimitRange).grid(row=9, column=2, sticky=E); Label(frmSetting, text="meter").grid(row=9, column=3, sticky=W, columnspan=2);

      # range : short, mid, long
      Radiobutton(frmSetting, text="short(2m)", value= 2, variable=self.intLimitRange).grid(row=10, column=2)
      Radiobutton(frmSetting, text="mid(3m)"  , value= 5, variable=self.intLimitRange).grid(row=10, column=3)
      Radiobutton(frmSetting, text="long(10m)", value=10, variable=self.intLimitRange).grid(row=10, column=4)
      
      Label(frmSetting, text=" ", bd=2).grid(row=15, column=1, columnspan=5, sticky=W)


      ##############################################################
      #[Measure Frame]
      ##############################################################
      frmMeasuer = Frame(master, border=2)
      frmMeasuer .grid(row=1, column=0, sticky='W')
      #frmSetting.pack()      
          
      Label(frmMeasuer, text="<< Measurement >>"  , bd=2).grid(row=3, column=0)
      Label(frmMeasuer, text=" ", bd=2).grid(row=5, column=1, columnspan=5, sticky=W)

      # Measurement button
      Button(frmMeasuer, text='Measurement Start', command = self.MeasureStart).grid(row=7, column=1);   Label(frmMeasuer, text=" ").grid(row=7, column=2); Button(frmMeasuer, text='Measurement Stop', command = self.MeasureStop).grid(row=7, column=3);


      # before Correct
      Label(frmMeasuer, text="Real Data(before Correct)").grid(row=10, column=0, columnspan=4, sticky=W)
      Label(frmMeasuer, text="Tx"       ).grid(row=11, column=1, sticky=E);  Entry(frmMeasuer, justify="center", textvariable=self.dRealTx      , state='disabled').grid(row=11, column=2, sticky=E)
      Label(frmMeasuer, text="RSSI"     ).grid(row=12, column=1, sticky=E);  Entry(frmMeasuer, justify="center", textvariable=self.dRealRssi    , state='disabled').grid(row=12, column=2, sticky=E)
      Label(frmMeasuer, text="Distance" ).grid(row=13, column=1, sticky=E);  Entry(frmMeasuer, justify="center", textvariable=self.dRealDistance, state='disabled').grid(row=13, column=2, sticky=E)
      

      # After Correct
      Label(frmMeasuer, text="After Correct").grid(row=15, column=0, columnspan=4, sticky=W)
      Label(frmMeasuer, text="Distance"     ).grid(row=16, column=1, sticky=E);  Entry(frmMeasuer, justify="center", textvariable=self.dAftDis    , state='disabled').grid(row=16, column=2, sticky=W)      
      Label(frmMeasuer, text="Queue"        ).grid(row=16, column=3, sticky=E);  Entry(frmMeasuer, justify="left"  , textvariable=self.dAftQueue  , state='disabled', width=30).grid(row=16, column=4, columnspan=2, sticky=W)
      Label(frmMeasuer, text="Average Dis"  ).grid(row=17, column=3, sticky=E);  Entry(frmMeasuer, justify="center", textvariable=self.dAftAverDis, state='disabled').grid(row=17, column=4, sticky=W)  
      

      # Result
      Label(frmMeasuer, text="Result").grid(row=21, column=0, columnspan=4, sticky=W)
      # range
      Radiobutton(frmMeasuer, text="inner range" , value= 1, variable=self.intResultRange).grid(row=22, column=1)
      Radiobutton(frmMeasuer, text="out of range", value= 2, variable=self.intResultRange).grid(row=22, column=2)
      Radiobutton(frmMeasuer, text="no signal"   , value= 3, variable=self.intResultRange).grid(row=22, column=3)
      


   # take a measurement
   def MeasureStart(self):
       print ("Measure Start")
       return
       
   def MeasureStop(self):
       print ("Measure Stop")
       return
      
      


##############################################################
#[SET List]
##############################################################
# frmTestList = Frame(window, border=1)
#
# # list
# listbox = Listbox(frmTestList)
# for item in ['red','green','yello','black','white']:
#     listbox.insert(END, item)
# listbox.grid(row=0, column=0, sticky=W+E+N+S)
#
# # scrollbar
# scrollbar = Scrollbar(window)
# scrollbar.pack(side=RIGHT, fill=Y)
#
# # message
# #text = Text(frmTestList, relief=SUNKEN)
# text = Text(frmTestList, yscrollcommand=scrollbar.set)
# text.grid(row=0, column=1, sticky=W+E+N+S)
# text.insert(END, 'word ' * 500)
# scrollbar.config(command=text.yview)
# frmTestList.columnconfigure(1, weight=1)
# frmTestList.rowconfigure(0,weight=1)



##############################################################
#[window set]
##############################################################

#frmSetting .grid(row=0, column=0, sticky='W')
#frmTestList .grid(row=1, column=0, sticky='W')
#frmTestList .pack(fill=BOTH,expand=1)



##############################################################
#[Tkinter Construtor]
##############################################################
window = Tk()
window.wm_title('Tkinter test')
#window.configure(background="gray")
app=App(window)
#window.geometry("400x300")
window.geometry("900x900+100+100")
window.mainloop()

