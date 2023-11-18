from tkinter import *


wind=Tk()
lab=Label(wind,text="hi python class", fg="red")
lab.pack()
b1=Button(wind,text="EXIT",command=wind.destroy)
b1.pack()
b2=Button(wind,text="Enter1")
b2.pack(side=RIGHT)
b3=Button(wind,text="Enter2")
b3.pack(side=LEFT)
wind.mainloop()
