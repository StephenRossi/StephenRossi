import sqlite3

conn = sqlite3.connect('test.db')
print ("opened database successfully")

conn.execute("DROP table CRACK")

print ("Table CRACK successfully dropped")
conn.close()
