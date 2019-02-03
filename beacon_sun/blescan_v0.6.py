###################################################
#
# File name   : blescan_v0.6.py
# Execution   : python3 blescan_v0.6.py
# Description :
#         v0.5: GUI Setting
#         v0.6: BLE Setting
#
###################################################

#########[python 2.x]###########
from Tkinter import *
import Queue
from ttk import Progressbar

#########[python 3.x]###########
#from tkinter import *
#import queue
#from tkinter.ttk import Progressbar


#########[BLE]###########
import blescan
import sys
import bluetooth._bluetooth as bluez


#########[ETC]###########
from threading import Thread
import time


class App:

   def __init__(self, master):
      ##############################################################
      #[Variable ]
      ##############################################################
      self.strBleUUID       = StringVar();   self.strBleUUID       .set("24ddf4118cf1440c87cde368daf9c93e")
      self.intBleMajor      = IntVar()   ;   self.intBleMajor      .set(501)
      self.intBleMinor      = IntVar()   ;   self.intBleMinor      .set(20781)
      self.dDisDepth        = DoubleVar();   self.dDisDepth      .set(5)       # queue
      self.dMeasureFreq     = DoubleVar();   self.dMeasureFreq   .set(0.5)     # second
      self.dAllowTolRate    = DoubleVar();   self.dAllowTolRate  .set(30)      # percent
      self.intLimitRange    = IntVar()   ;   self.intLimitRange  .set(5)       # Limit Distance
      self.dRealTx          = DoubleVar();   self.dRealTx        .set(0)       #
      self.dRealRssi        = DoubleVar();   self.dRealRssi      .set(0)       #
      self.dRealDistance    = DoubleVar();   self.dRealDistance  .set(0)       #
      self.dAftDis          = DoubleVar();   self.dAftDis        .set(0)       #
      self.dAftQueue        = DoubleVar();   self.dAftQueue      .set(0)       #
      self.dAftAverDis      = DoubleVar();   self.dAftAverDis    .set(0)       #
      self.intResultRange   = IntVar()   ;   self.intResultRange .set(3)       # 1:inner, 2: Outer,  3: no signal
      self.strResultOut     = StringVar();   self.strResultOut   .set("")
      

      self.q = Queue.Queue()
      #self.q = Queue.PriorityQueue()




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


      Label(frmSetting, text="[Setting]", fg='black', font=20).grid(row=0, column=0, sticky='W', columnspan=2)

      Label(frmSetting, text="BLE infomation" , bd=2).grid(row=1, column=0, sticky=W)
      Label(frmSetting, text="UUID"           , bd=2).grid(row=1, column=1, sticky=E);  Entry(frmSetting, justify="center", textvariable=self.strBleUUID , width=40).grid(row=1, column=2, sticky=W, columnspan=2)
      Label(frmSetting, text="Major"          , bd=2).grid(row=2, column=1, sticky=E);  Entry(frmSetting, justify="center", textvariable=self.intBleMajor).grid(row=2, column=2, sticky=W)
      Label(frmSetting, text="Minor"          , bd=2).grid(row=2, column=3, sticky=E);  Entry(frmSetting, justify="center", textvariable=self.intBleMinor).grid(row=2, column=4, sticky=W)

      Label(frmSetting, text=" ", bd=2).grid(row=3, column=1, columnspan=5, sticky=W)

      # correction criterion
      Label(frmSetting, text="Correction Criterion" , bd=2).grid(row=4, column=0, sticky=W)
      Label(frmSetting, text="Dis. Depth"           , bd=2).grid(row=4, column=1, sticky=E);  Entry(frmSetting, justify="center", textvariable=self.dDisDepth      ).grid(row=4, column=2, sticky=E); Label(frmSetting, text="(queue)").grid(row=4, column=3, sticky=W, columnspan=2);
      Label(frmSetting, text="Measure Frequency"    , bd=2).grid(row=5, column=1, sticky=E);  Entry(frmSetting, justify="center", textvariable=self.dMeasureFreq   ).grid(row=5, column=2, sticky=E); Label(frmSetting, text="second" ).grid(row=5, column=3, sticky=W, columnspan=2);
      Label(frmSetting, text="Allowable Tolerance"  , bd=2).grid(row=6, column=1, sticky=E);  Entry(frmSetting, justify="center", textvariable=self.dAllowTolRate  ).grid(row=6, column=2, sticky=E); Label(frmSetting, text="(%) percent").grid(row=6, column=3, sticky=W, columnspan=2);
      Label(frmSetting, text="this section is in order to reduce the error distance ").grid(row=7, column=1, sticky=W, columnspan=3)

      Label(frmSetting, text=" ", bd=2).grid(row=8, column=1, columnspan=5, sticky=W)

      # Limit distance
      Label(frmSetting, text="Limit distance", bd=2).grid(row=9, column=0, sticky=W)
      Label(frmSetting, text="Range"         , bd=2).grid(row=9, column=1, sticky=E);  Entry(frmSetting, justify="center", textvariable=self.intLimitRange).grid(row=9, column=2, sticky=E); Label(frmSetting, text="meter").grid(row=9, column=3, sticky=W, columnspan=2);

      # range : short, mid, long
      Radiobutton(frmSetting, text="short(2m)", value= 2, variable=self.intLimitRange).grid(row=10, column=2)
      Radiobutton(frmSetting, text="mid(5m)"  , value= 5, variable=self.intLimitRange).grid(row=10, column=3)
      Radiobutton(frmSetting, text="long(10m)", value=10, variable=self.intLimitRange).grid(row=10, column=4)

      Label(frmSetting, text=" ", bd=2).grid(row=15, column=1, columnspan=5, sticky=W)


      ##############################################################
      #[Measure Frame]
      ##############################################################
      frmMeasuer = Frame(master, border=2)
      frmMeasuer .grid(row=1, column=0, sticky='W')
      #frmSetting.pack()

      Label(frmMeasuer, text="[Measurement]", fg='black', font=20).grid(row=3, column=0, sticky='W', columnspan=2)
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
      Label(frmMeasuer, text="Queue"        ).grid(row=16, column=3, sticky=E);  Entry(frmMeasuer, justify="left"  , textvariable=self.dAftQueue  , state='disabled', width=50).grid(row=16, column=4, columnspan=2, sticky=W)
      Label(frmMeasuer, text="Average Dis"  ).grid(row=17, column=3, sticky=E);  Entry(frmMeasuer, justify="center", textvariable=self.dAftAverDis, state='disabled').grid(row=17, column=4, sticky=W)


      # Result
      Label(frmMeasuer, text="Result").grid(row=21, column=0, columnspan=4, sticky=W)
      # range
      Radiobutton(frmMeasuer, text="inner range" , value= 1, variable=self.intResultRange).grid(row=22, column=1)
      Radiobutton(frmMeasuer, text="out of range", value= 2, variable=self.intResultRange).grid(row=22, column=2)
      Radiobutton(frmMeasuer, text="no signal"   , value= 3, variable=self.intResultRange).grid(row=22, column=3)
      Label(frmMeasuer, text='Out of range', font=30, fg='red', textvariable=self.strResultOut,).grid(row=22, column=4, columnspan=3)


      ##############################################################
      #[Measure Log Frame]
      ##############################################################
      frmLog = Frame(master, border=2)
      frmLog .grid(row=2, column=0, sticky='W')
      #frmSetting.pack()

      self.strModetxt  =StringVar()
      self.strDirection=StringVar()

      Label(frmLog, text=" ", bd=2).grid(row=0, column=1, columnspan=5, sticky=W)
      Label(frmLog, text='[Measure Log]', fg='black', font=20).grid(row=3, column=0, sticky='W', columnspan=2)
      Label(frmLog, text='Measure Mode', font=30, fg='red', textvariable=self.strModetxt  ).grid(row=4, column=0, columnspan=2)



   # take a measurement
   def MeasureStart(self):
      print ("Measuring...")

      global MeasureMode
      self.q.maxsize= self.dDisDepth.get()
      self.strModetxt.set("Measure Starting...")

      MeasureMode=1
      thread1 = Thread( target=self.Measuring, args=() )
      thread1.start()
      #thread1.join()

      return


   def MeasureStop(self):
      print ("Measure Stop")
      global MeasureMode
      self.strModetxt.set("Measure ending...")

      MeasureMode=0
      thread1 = Thread( target=self.Measuring, args=() )
      thread1.start()
      #thread1.join()
      return


   def Measuring(self):
      global MeasureMode
      strBleUUID  =     self.strBleUUID.get()
      strBleMajor = str(self.intBleMajor.get())
      strBleMinor = str(self.intBleMinor.get())
      print("strBleUUID : ", strBleUUID )
      print("strBleMajor: ", strBleMajor)
      print("strBleMajor: ", strBleMajor)
      print("strBleMinor: ", strBleMinor)

      if (MeasureMode == 1):
          self.dev_id = 0
          try:
              sock = bluez.hci_open_dev(self.dev_id)
              print ("ble thread started")
          except:
              print ("error accessing bluetooth device...")
              sys.exit(1)

          blescan.hci_le_set_scan_parameters(sock)
          blescan.hci_enable_le_scan(sock)

      while (MeasureMode == 1):
          time.sleep(self.dMeasureFreq.get())
          returnedList = blescan.parse_events(sock, 10)
          print ("----------")
          for beacon in returnedList:
              split_beacon = beacon.split(',')
              # print (split_beacon)
              #print ("split_beacon[1]: ", split_beacon[1])
              #print ("split_beacon[2]: ", split_beacon[2])
              #print ("split_beacon[3]: ", split_beacon[3])

              dRealTx   = float(split_beacon[4])
              dRealRSSI = float(split_beacon[5])

              if (split_beacon[1] == strBleUUID  and
                  split_beacon[2] == strBleMajor and
                  split_beacon[3] == strBleMinor ):   # major,  major

                  print (beacon)

                  self.dRealTx  .set(dRealTx  )   # Tx
                  self.dRealRssi.set(dRealRSSI)   # RSSI

                  intRealN = 2                                                            # Real N (Constant depends on the Environmental factor. Range 2-4)
                  dRealDistance = round(10**((dRealTx - dRealRSSI)/(10 * intRealN)), 2)   # Real Distance Calc
                  self.dRealDistance.set(dRealDistance)                                   # Real Distance


                  ### Correct Distance
                  if (self.dAftAverDis.get() == 0):
                      dAllowTolerance = (dRealDistance * dRealDistance * 0.01)
                  else :
                      dAllowTolerance = (self.dAftAverDis.get() * self.dAllowTolRate.get() * 0.01)


                  ### tolerance_pass

                  if (self.dAllowTolRate.get() == 0):
                  	tolerance_pass = True

                  if (self.q.qsize() < self.dDisDepth.get() ):
                  	tolerance_pass = True

                  if (dRealDistance >= self.dAftAverDis.get() - dAllowTolerance and dRealDistance <= self.dAftAverDis.get() + dAllowTolerance ):
                  	tolerance_pass = True

                  if (tolerance_pass == True) :     ## tolerance pass

                      self.dAftDis.set(dRealDistance)

                      ## put queue
                      if (self.q.qsize() == self.dDisDepth.get()):
                          self.q.get()
                      self.q.put(dRealDistance)
                      self.dAftQueue.set(self.q.queue)   # queue

                      ## Average
                      self.dAftAverDis.set(  round(  sum(self.q.queue) / len(self.q.queue) , 2) )


                      ## Check Limit Range and Result Range
                      if (self.dAftAverDis.get() <= self.intLimitRange.get()):
                          self.intResultRange.set(1)
                          self.strResultOut.set("")
                      else:
                          self.intResultRange.set(2)
                          self.strResultOut.set("Out of range")

                  # end if - tolerance pass
              # end if
          # end for
      # end while

      self.intResultRange.set(3)   # no signal
      self.strResultOut.set("")
      while (self.q.qsize() > 0):  # queue remove
          self.q.get()
          self.dAftQueue.set(self.q.queue)

      self.strModetxt.set("Measuring END")
      return



# =============================================================================
# Tkinter Construtor
# =============================================================================
window = Tk()
window.wm_title('Tkinter test')
#window.configure(background="gray")


# =============================================================================
# window start
# =============================================================================
app=App(window)
#window.geometry("400x300")
window.geometry("900x700+100+100")
window.mainloop()


# =============================================================================
# Program Exit
# =============================================================================
print "Program Exit"

