#delte a row function
import sqlite3
def create_table():
    #1-connect to a database
    conn=sqlite3.connect("dat.db")

    #2-create a cousor object
    cur=conn.cursor()

    #3-write an SQL query
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quant INTEGER , price REAL)")
    #4-commit changes
    conn.commit()

    #5-close connection
    conn.close()


def insert(item,quant,price):

     #1-connect to a database
    conn=sqlite3.connect("dat.db")

    #2-create a cousor object
    cur=conn.cursor()

    #3-write an SQL query
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quant,price))
    #4-commit changes
    conn.commit()

    #5-close connection
    conn.close()

def view():
     #1-connect to a database
    conn=sqlite3.connect("dat.db")

    #2-create a cousor object
    cur=conn.cursor()

    #3-write an SQL query
    cur.execute("SELECT * FROM store")
    #4-fetch data
    rows=cur.fetchall()

    #5-close connection
    conn.close()
    return rows

def delete(item):

     #1-connect to a database
    conn=sqlite3.connect("dat.db")

    #2-create a cousor object
    cur=conn.cursor()

    #3-write an SQL query
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    #4-commit changes
    conn.commit()

    #5-close connection
    conn.close()
output=view()
print(output)
delete("coffee")
output=view()
print(output)
