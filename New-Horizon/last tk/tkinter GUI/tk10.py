from tkinter import *

def x():
    print("hiii")
fen1 = Tk()

e1 = Entry(fen1)
b1=Button(fen1,text="Enter1",command=x)#new x isa function
t1=Text(fen1,height=1,width=20)
b1.grid(row =0)
e1.grid(row =0, column =1)
t1.grid(row=0,column=2)
fen1.mainloop()
