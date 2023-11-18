from tkinter import *

win = Tk()


l1=Label(win,text="Frist name")
l2=Label(win,text="Last name")
l3=Label(win,text="Term")
l4=Label(win,text="GPA")

e1=Entry(win)
e2=Entry(win)
e3=Entry(win)
e4=Entry(win)

b1=Button(win,text="View all")
b2=Button(win,text="Search")
b3=Button(win,text="Add New")
b4=Button(win,text="Update")
b5=Button(win,text="Delete")
b6=Button(win,text="Clear")
b7=Button(win,text="Exit")

l1.grid(row=0,column=0)
l2.grid(row=0,column=2)
l3.grid(row=1,column=0)
l4.grid(row=1,column=2)

e1.grid(row=0,column=1)
e2.grid(row=0,column=3)
e3.grid(row=1,column=1)
e4.grid(row=1,column=3)

b1.grid(row=2,column=3)
b2.grid(row=3,column=3)
b3.grid(row=4,column=3)
b4.grid(row=5,column=3)
b5.grid(row=6,column=3)
b6.grid(row=7,column=3)
b7.grid(row=8,column=3)


win.mainloop()
