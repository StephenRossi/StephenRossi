import sqlite3

conn = sqlite3.connect('classes.db')
print ("opened database successfully")

conn.execute("INSERT INTO Teachers (ID, NAME, AGE) VALUES (2, 'Krug', 31)")
conn.commit()
conn.close()
print ("data inserted to table 'Teachers'")
print ("Connection closed")
