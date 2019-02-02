###################################################
#
# File name  : ex612_Tkinter_basic.py
# Executeoin : python3 ex612_Tkinter_basic.py
# Description : Listbox, Scrollbar
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
#[SET List]
##############################################################
frmTestList = Frame(window, border=1)

# list
listbox = Listbox(frmTestList)
for item in ['red','green','yello','black','white']:
    listbox.insert(END, item)
listbox.grid(row=0, column=0, sticky=W+E+N+S)

# scrollbar
scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)

# message
#text = Text(frmTestList, relief=SUNKEN)
text = Text(frmTestList, yscrollcommand=scrollbar.set)
text.grid(row=0, column=1, sticky=W+E+N+S)
text.insert(END, 'word ' * 500)
scrollbar.config(command=text.yview)
frmTestList.columnconfigure(1, weight=1)
frmTestList.rowconfigure(0,weight=1)



##############################################################
#[window set]
##############################################################

#frmTestList .grid(row=3, column=0, sticky='W')
frmTestList .pack(fill=BOTH,expand=1)



##############################################################
#[Tkinter]
##############################################################
#window.geometry("400x300")
window.geometry("900x900+100+100")
window.mainloop()

