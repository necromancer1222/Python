from tkinter import *

def x():
    t1.delete(0.0,END)#new
    t1.insert(END,y.get())
    e1.delete(0,END)#new
    
fen1 = Tk()
y=StringVar()
e1 = Entry(fen1,textvariable=y)
b1=Button(fen1,text="Enter1",command=x)
t1=Text(fen1,height=1,width=20)
b1.grid(row =0)
e1.grid(row =0, column =1)
t1.grid(row=0,column=2)
fen1.mainloop()
