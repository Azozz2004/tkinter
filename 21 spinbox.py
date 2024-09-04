from tkinter import *
from tkinter import ttk

pro = Tk()
pro.geometry('500x400')
################################
sp = Spinbox(pro, from_=0,to=100)
sp.pack()

sp1 = Spinbox(pro, from_=20,to=40)
sp1.pack()

ent = Entry(pro)
ent.pack()
################################
pro.mainloop()