from tkinter import *
fen1 = Tk()
e1 = Entry(fen1)
b1=Button(fen1,text="Enter1")
t1=Text(fen1,height=1,width=20)#new for output
b1.grid(row =0)
e1.grid(row =0, column =1)
t1.grid(row=0,column=2)
fen1.mainloop()
