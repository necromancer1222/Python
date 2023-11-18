import sqlite3

connction = sqlite3.connect("file.db")

cursor = connction.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quant INTEGER, price REAL)")
cursor.execute("INSERT INTO store VALUES('suger',1,7.5)")

connction.commit()

connction.close()
