
from tkinter import *
fen1 = Tk()
lab1 = Label(fen1, text = 'enter1 :')
lab2 = Label(fen1, text = 'enter2 :')
e1 = Entry(fen1)
e2 = Entry(fen1)
lab1.grid(row =0)
lab2.grid(row =1)
e1.grid(row =0, column =2)
e2.grid(row =1, column =2)

b1=Button(fen1,text="Enter1")
b2=Button(fen1,text="Enter2")
b1.grid(row=0,column =1)
b2.grid(row=1,column =1)
fen1.mainloop()
