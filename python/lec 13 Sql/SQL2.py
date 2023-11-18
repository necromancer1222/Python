import sqlite3

def create_table():
    connction = sqlite3.connect("file.db")

    cursor = connction.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quant INTEGER, price REAL)")

    connction.commit()

    connction.close()

def insert(item,quant,price):
    connction = sqlite3.connect("file.db")

    cursor = connction.cursor()

    cursor.execute("INSERT INTO store VALUES(?,?,?)",(item,quant,price))

    connction.commit()

    connction.close()

def view():
    connction = sqlite3.connect("file.db")

    cursor = connction.cursor()

    cursor.execute("SELECT * FROM store")#select all
    
    rows = cursor.fetchall() # copy the selected

    connction.close()

    return rows 

#create_table()
#insert("coffee",10,2.5)

output = view()
print(output)


