###################################################
#
# file name  : ex621_progressbar.py
# executeoin : python3 ex621_progressbar.py
#
###################################################

##########[python 2.x]###########
##from Tkinter import *
#
##########[python 3.x]###########
#from tkinter import *

import tkinter
import tkinter.ttk

window=tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry("640x400+100+100")
window.resizable(False, False)

progressbar=tkinter.ttk.Progressbar(window, maximum=100, mode="indeterminate")
progressbar.pack()

progressbar.start(50)

window.mainloop()