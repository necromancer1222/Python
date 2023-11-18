from tkinter import *
import sqlite3

def connect(): #create table only
    conn=sqlite3.connect("students.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS data1 (id INTEGER PRIMARY KEY, fn TEXT, ln TEXT, term INTEGER, gpa REAL)")
    conn.commit()
    conn.close()


def insert(fn,ln,term,gpa): #insert the stds 
    conn=sqlite3.connect("students.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO data1 VALUES (NULL,?,?,?,?)",(fn,ln,term,gpa))
    conn.commit()
    conn.close()

def view(): #need an extranl var to print it from
    conn=sqlite3.connect("students.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM data1")
    rows=cur.fetchall()
    conn.close()
    list_box.insert(END,str(rows))
    return rows

def delete(id): #delete using the id
    conn=sqlite3.connect("students.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM data1 WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(fn,ln,term,gpa,id): #update using the id
    conn=sqlite3.connect("students.db")
    cur=conn.cursor()
    cur.execute("UPDATE data1 SET fn=?, ln=?, term=?, gpa=? WHERE id=?",(fn,ln,term,gpa,id))
    conn.commit()

def search(id="",fn="",ln=""): # search using id or fn or ln
    conn=sqlite3.connect("students.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM data1 where id=? OR fn=? Or ln=?",(id,fn,ln))
    rows=cur.fetchall()
    conn.close()
    return rows

def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    list_box.delete(0,END)
    e5.delete(0,END)
    

win = Tk()

# DEFINITION SECTION
connect()

l1=Label(win,text="Frist name")
l2=Label(win,text="Last name")
l3=Label(win,text="Term")
l4=Label(win,text="GPA")
l5=Label(win,text="ID")

fn=StringVar()
ln=StringVar()
term=StringVar()
gpa=StringVar()
id=StringVar()

e1=Entry(win, textvariable = fn)
e2=Entry(win, textvariable = ln)
e3=Entry(win, textvariable = term)
e4=Entry(win, textvariable = gpa)
e5=Entry(win, textvariable = id)

b1=Button(win,text="View all",width=18,command = view)
b2=Button(win,text="Search",width=18,  command = search)
b3=Button(win,text="Add New",width=18, command = insert)
b4=Button(win,text="Update",width=18,  command = update)
b5=Button(win,text="Delete",width=18,  command = delete)
b6=Button(win,text="Clear",width=18,   command = clear)
b7=Button(win,text="Exit",width=18,    command = win.destroy)

list_box = Listbox(win, height=6, width=35)

sc = Scrollbar(win)

# LAYOUT SECTION

l1.grid(row=0,column=0)
l2.grid(row=0,column=2)
l3.grid(row=1,column=0)
l4.grid(row=1,column=2)
l5.grid(row=9,column=0)

e1.grid(row=0,column=1)
e2.grid(row=0,column=3)
e3.grid(row=1,column=1)
e4.grid(row=1,column=3)
e5.grid(row=9,column=1,columnspan=2)

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
