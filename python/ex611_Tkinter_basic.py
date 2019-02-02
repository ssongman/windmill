###################################################
#
# File name  : ex611_Tkinter_basic.py
# Executeoin : python3 ex611_Tkinter_basic.py
# Description : 
#
###################################################

#########[python 2.x]###########
#from Tkinter import *

#########[python 3.x]###########
from tkinter import *


##############################################################
#[Tkinter Construtor]
##############################################################
window = Tk()
window.title('Tkinter test')
#window.configure(background="gray")



##############################################################
#[SET Button]
##############################################################
def mhello():
    print ("Hello222")
    return
mbutton = Button(window, text='OK', command = mhello, fg='red', bg='blue')


##############################################################
#[SET Frame]
##############################################################
frmRunBtn = Frame(window, border=1)
btnForward   = Button(frmRunBtn, width=10, height=3, text='Forward(W)'    , bd=4)
btnReverse   = Button(frmRunBtn, width=10, height=3, text='Reverse(X)'    , bd=4)
btnTurnLeft  = Button(frmRunBtn, width=10, height=3, text='Turn Left(A)'  , bd=4)
btnTurnRight = Button(frmRunBtn, width=10, height=3, text='Turn Right(D)' , bd=4)
btnPivotLeft = Button(frmRunBtn, width=10, height=3, text='Pivot Left(Q)' , bd=4)
btnPivotRight= Button(frmRunBtn, width=10, height=3, text='Pivot Right(E)', bd=4)
btnStop      = Button(frmRunBtn, width=10, height=3, text='Stop(S)'       , bd=4)

Label(frmRunBtn, text='[Drive]', fg='black', font=20).grid(row=0, column=0, sticky='W', columnspan=3)
btnPivotLeft .grid(row=1, column=0)
btnForward   .grid(row=1, column=1)
btnPivotRight.grid(row=1, column=2)
btnTurnLeft  .grid(row=2, column=0)
btnStop      .grid(row=2, column=1)
btnTurnRight .grid(row=2, column=2)
btnReverse   .grid(row=3, column=1)



##############################################################
#[SET Label]
##############################################################
frmTestlable = Frame(window, border=1)
#Label (frmTestlable, text="first value : " , bg="gray").grid(row=0, column=0, sticky=E)
#Label (frmTestlable, text="second value : ", bg="gray").grid(row=0, column=0, sticky=E)
#label1=Label(frmTestlable, text="first value : " , bg="gray").place(x=20, y=20)
#label2=Label(frmTestlable, text="second value : ", bg="gray").place(x=20, y=40)

label1=Label(frmTestlable, width=10, height=2, text="first value : " , bd=2).grid(row=0, column=0)
label2=Label(frmTestlable, width=10, height=2, text="second value : ", bd=2).grid(row=1, column=0)




##############################################################
#[SET List]
##############################################################
frmTestList = Frame(window, border=1)

# list
listbox = Listbox(frmTestList)
for item in ['red','green','yello','black','white']:
    listbox.insert(END, item)
listbox.grid(row=0, column=0, sticky=W+E+N+S)

# message
text = Text(frmTestList, relief=SUNKEN)
text.grid(row=0, column=1, sticky=W+E+N+S)
text.insert(END, 'word ' * 100)
frmTestList.columnconfigure(1, weight=1)
frmTestList.rowconfigure(0,weight=1)



##############################################################
#[window set]
##############################################################

mbutton     .grid(row=0, column=0, sticky='W')
frmRunBtn   .grid(row=1, column=0, sticky='W')
frmTestlable.grid(row=2, column=0, sticky='W')
frmTestList .grid(row=3, column=0, sticky='W')




##############################################################
#[Tkinter]
##############################################################
#window.geometry("400x300")
window.geometry("900x900+100+100")
window.mainloop()

