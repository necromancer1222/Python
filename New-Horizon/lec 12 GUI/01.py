from tkinter import *
def x():
    t1.delete(0.0,END)
    miles = float(y.get())/1.6
    t1.insert(END,str(miles)+ " miles")
    #t1.insert(0.0,y.get())
    e1.delete(0,END)

win = Tk()

y=StringVar()

b1=Button(win,text="Enter",command = x)
e1=Entry(win, textvariable = y)
t1= Text(win,height=1,width=20)

b1.grid(row=0,column=0)
e1.grid(row=0,column=1)
t1.grid(row=0,column=2)

win.mainloop()
