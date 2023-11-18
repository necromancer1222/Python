from tkinter import *

window = Tk() # enter loop

text = Label(window,text="this is weird",fg="gray") #Label for text
text.pack() #.pack() gives the text in the middel of window like print

button1 = Button(window, text="EXIT!!!",command = window.destroy) #Button for well buttons, .destroy to close the loop like break
button1.pack()

e1 = Entry(window) #to have a place to write in, but wont actually save whats written
e1.pack()# default will go to a next line

button2 = Button(window, text="ENTER NUMBER!!!",) 
button2.pack(side=LEFT)

e2 = Entry(window)
e2.pack(side=LEFT)

button3 = Button(window, text="ENTER TEXT!!!",) 
button3.pack(side=LEFT)

e3 = Entry(window)
e3.pack(side=LEFT)

window.mainloop() #exit loop
