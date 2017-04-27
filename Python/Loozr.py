import sqlite3

conn = sqlite3.connect('test.db')
print ("Database 'test.db' succesfully connected")
cursor = conn.execute("SELECT ID, NAME, AGE FROM CRACK")

for row in cursor:
    print ("ID = ", row[0])
    print ("NAME = ", row[1])
    print ("AGE = ", row[2])

print ("Table CRACK successfull select")
conn.close()
