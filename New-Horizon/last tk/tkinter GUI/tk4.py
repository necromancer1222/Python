from tkinter import *


wind=Tk()
lab=Label(wind,text="hi python class", fg="red")
lab.pack()
b1=Button(wind,text="EXIT",command=wind.destroy)#new
b1.pack()
e1=Entry(wind)#e1 will work as input function
e1.pack()
wind.mainloop()
