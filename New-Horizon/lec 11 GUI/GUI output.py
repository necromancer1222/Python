from tkinter import *
win = Tk()

e1=Entry(win)
b1=Button(win,text="Enter input :")
t1= Text(win,height=1,width=20)# height for lines, width for letters in line, TEXT is for the output

b1.grid(row=0)
e1.grid(row=0,column=1)
t1.grid(row=0,column=2)

win.mainloop()
