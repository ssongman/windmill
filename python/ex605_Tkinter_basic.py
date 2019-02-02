###################################################
#
# File name  : ex605_Tkinter_basic.py
# Executeoin : python3 ex605_Tkinter_basic.py
# Description : lable, entry, radio box, button
#
###################################################

#########[python 2.x]###########
#from Tkinter import *

#########[python 3.x]###########
from tkinter import *



##############################################################
#[Tkinter Construtor]
##############################################################
mGui = Tk()
mGui.title('Tkinter test')


##############################################################
#[Button]
##############################################################
def mhello():
    print ("Hello")
    return
mbutton = Button(mGui, text='OK', command = mhello, fg='red', bg='blue').pack()



##############################################################
#[Messagebox]
##############################################################
def msgbox():
    messagebox.showinfo("info", "message is : " + "message")
    messagebox.showwarning("info", "message is abcd ")
    messagebox.askquestion("info", "message is abcd ")
    messagebox.askokcancel("info", "message is abcd ")
    messagebox.askyesno("info", "message is abcd ")
    messagebox.askretrycancel("info", "message is abcd ")

##############################################################
#[Label and Entry and RadioButton]
##############################################################

def operation():
    fval = txtval.get()
    if rbval.get() == 1:
        total = fval * 10
    elif rbval.get() == 2:
        total = fval * 20
    elif rbval.get() == 3:
        total = fval * 30
    elif rbval.get() == 4:
        total = fval * 40
    elif rbval.get() == 5:
        total = fval * 50
    else:
        total = fval * fval
    print("result : " + str(total))
    
    


txtval=IntVar()
fvalue    = Label(mGui, text="first value : ").place(x=20, y=20)
et_fvalue = Entry(mGui, textvariable=txtval).place(x=130,y=20)
express   = Label(mGui, text="Express : ").place(x=20, y=50)


rbval=IntVar()
x10 = Radiobutton(mGui, text="x10", value=1, variable=rbval).place(x= 20,y=80)
x20 = Radiobutton(mGui, text="x20", value=2, variable=rbval).place(x= 70,y=80)
x30 = Radiobutton(mGui, text="x30", value=3, variable=rbval).place(x=120,y=80)
x40 = Radiobutton(mGui, text="x40", value=4, variable=rbval).place(x= 20,y=110)
x50 = Radiobutton(mGui, text="x50", value=5, variable=rbval).place(x= 70,y=110)
cuadrado = Radiobutton(mGui, text="Cuadrao", value=6, variable=rbval).place(x=120, y=110)
boton = Button(mGui, text="Calulator", command=operation).place(x=20, y=140)


##############################################################
#[Menu]
##############################################################
def mNew():
    print("mNew")
    return
def mOPen():
    print("mOPen")
    return
def mColour():
    print("mColour")
    return
def mQuit():
    print("mQuit")
    return
def mAbout():
    print("mAbout")
    return

# Menu Construction
menubar=Menu(mGui)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="new", command = mNew)
filemenu.add_command(label="Open", command = mOPen)
filemenu.add_command(label="Save As..")
filemenu.add_command(label="Colour", command = mColour)
filemenu.add_command(label="Close", command = mQuit)
menubar.add_cascade(label="File", menu = filemenu)

# SetUp
setupmenu = Menu(menubar, tearoff = 0)
setupmenu.add_checkbutton(label = "Auto")
menubar.add_cascade(label="Setup", menu=setupmenu)

# Help Menu
helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label="Help Docs")
helpmenu.add_command(label="About", command = mAbout)
menubar.add_cascade(label="Help", menu=helpmenu)






##############################################################
#[Tkinter]
##############################################################
#mGui.geometry("400x300")
mGui.geometry("450x450+500+300")
mGui.mainloop()
