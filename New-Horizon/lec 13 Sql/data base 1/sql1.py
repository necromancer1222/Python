import sqlite3
#1-connect to a database
conn=sqlite3.connect("dat.db")

#2-create a cousor object
cur=conn.cursor()

#3-write an SQL query
cur.execute("CREATE TABLE store (item TEXT, quant INTEGER , price REAL)")#execute WRITING OF THE CODE

#4-commit changes
#conn.commit()#RUN THIS CODE

#5-close connection
conn.close()

