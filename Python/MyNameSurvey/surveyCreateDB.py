import sqlite3

conn = sqlite3.connect('Survey.db')
print ("opened Survey database successfully")

#conn.execute('''DROP TABLE Input''')

conn.execute('''CREATE TABLE Input
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,
        AGE INTEGER NOT NULL,
        GENDER TEXT NOT NULL);''')

print ("Table Input successfully created")
conn.close()


