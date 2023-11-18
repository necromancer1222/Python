from tkinter import *

def x():
    t1.delete(0.0,END)
    gram = float(y.get()) * 1000
    t1.insert(END,str(gram)+ " gram")
    pound = float(y.get()) * 2.20462
    t2.insert(END,str(pound)+ " pound")
    ounce = float(y.get()) * 35.274
    t3.insert(END,str(ounce)+ " ounce")
    e1.delete(0,END)


win = Tk()

y=StringVar()#NEW

l1=Label(win,text="Kg")
e1=Entry(win,textvariable = y)#new
b1=Button(win,text="Convert",command = x)#new
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
