from tkinter import *
def from_kg():
    gram=float(e1_value.get())*1000
    pound=float(e1_value.get())*2.20462
    ounce=float(e1_value.get())*35.274
    t1.delete(0.0,END)
    t2.delete(0.0,END)
    t3.delete(0.0,END)
    t1.insert(END,str(gram)+" gram")
    t2.insert(END,str(pound)+" pound")
    t3.insert(END,str(ounce)+" ounce")

window=Tk()
lab1=Label(window,text="Kg")
lab1.grid(row=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

b1=Button(window,text="Convert",command=from_kg)
b1.grid(row=0,column=2)

t1=Text(window,height=1,width=20)
t1.grid(row=1,column=0)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=1)

t3=Text(window,height=1,width=20)
t3.grid(row=1,column=2)

window.mainloop()
