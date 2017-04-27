import sqlite3

conn = sqlite3.connect('test.db')
print ("opened database successfully")

conn.execute('''CREATE TABLE CRACK
        (ID INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        AGE  INT  NOT NULL);''')

print ("Table CRACK successfully created")
conn.close()
