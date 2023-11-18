from tkinter import *
win = Tk()

l1=Label(win,text="Kg")
e1=Entry(win)
b1=Button(win,text="Convert")
t1= Text(win,height=1,width=20)
t2= Text(win,height=1,width=20)
t3= Text(win,height=1,width=20)

l1.grid(row=0,column=0)
e1.grid(row=0,column=1)
b1.grid(row=0,column=2)

t1.grid(row=1,column=0)
t2.grid(row=1,column=1)
t3.grid(row=1,column=2)

win.mainloop()
