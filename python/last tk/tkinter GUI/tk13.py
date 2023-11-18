from tkinter import *

def x():
    t1.delete(0.0,END)
    miles=float(y.get())/1.6#miles=float("20")/1.6=12.5 as float
    t1.insert(END,str(miles) + " miles")#"12.5" +" miles"="12.5 miles"
fen1 = Tk()
y=StringVar()
e1 = Entry(fen1,textvariable=y)
b1=Button(fen1,text="Enter1",command=x)
t1=Text(fen1,height=1,width=20)
b1.grid(row =0)
e1.grid(row =0, column =1)
t1.grid(row=0,column=2)
fen1.mainloop()
