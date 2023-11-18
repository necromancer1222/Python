from tkinter import *


win = Tk()

# DEFINITION SECTION

l1=Label(win,text="Frist name")
l2=Label(win,text="Last name")
l3=Label(win,text="Term")
l4=Label(win,text="GPA")

E1=StringVar()
E2=StringVar()
E3=StringVar()
E4=StringVar()

e1=Entry(win, textvariable = E1)
e2=Entry(win, textvariable = E2)
e3=Entry(win, textvariable = E3)
e4=Entry(win, textvariable = E4)

b1=Button(win,text="View all",width=18)#,command = ??
b2=Button(win,text="Search",width=18)
b3=Button(win,text="Add New",width=18)
b4=Button(win,text="Update",width=18)
b5=Button(win,text="Delete",width=18)
b6=Button(win,text="Clear",width=18)
b7=Button(win,text="Exit",width=18)

list_box = Listbox(win, height=6, width=35)

sc = Scrollbar(win)

# LAYOUT SECTION

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

list_box.grid(row=2,column=0,rowspan=6,columnspan=2)

sc.grid(row=2,column=2,rowspan=6)

#connecting listbox and scrollbar

list_box.configure(yscrollcommand = sc.set)

sc.configure(command = list_box.yview)

win.mainloop()
