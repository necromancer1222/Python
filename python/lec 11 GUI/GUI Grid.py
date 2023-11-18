from tkinter import *

window = Tk() # enter loop

text = Label(window,text="this is weird",fg="gray") #Label for text
button1 = Button(window, text="EXIT!!!",command = window.destroy) #Button for well buttons, .destroy to close the loop like break
e1 = Entry(window) #to have a place to write in, but wont actually save whats written
button2 = Button(window, text="ENTER NUMBER!!!",) 
e2 = Entry(window)
button3 = Button(window, text="ENTER TEXT!!!",)
text1 = Label(window,text="Enter1 :")
text2 = Label(window,text="Enter2 :")

text.grid(row=0,column=1)
button1.grid(row=1,column=1)
button2.grid(row=2,column=1)
e1.grid(row=2,column=2)
button3.grid(row=3,column=1)
e2.grid(row=3,column=2)
text1.grid(row=2)
text2.grid(row=3)

window.mainloop() #exit loop
