import sqlite3

conn = sqlite3.connect('survey.db')
print ("opened survey database successfully")

conn.execute('''CREATE TABLE USERS
        (ID INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        AGE  INT  NOT NULL,
        GENDER INT NOT NULL);''')

print ("Table USERS successfully created")
