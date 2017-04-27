import sqlite3

conn = sqlite3.connect('survey.db')
print ("Database 'survey.db' succesfully connected")
cursor = conn.execute("SELECT ID, NAME, AGE, GENDER FROM input")
print ("-" *18)

for row in cursor:
    print ("|NAME = ", row[0])
    print ("|ID = ", row[1])
    print ("|AGE = ", row[2])
    print ("|GENDER = ", row[3])
    print ("-" * 18)

print ("Table 'input' successfull opened")
conn.close()
