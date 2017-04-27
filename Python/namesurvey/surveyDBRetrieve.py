import sqlite3

db = "Survey.db"
conn = sqlite3.connect(db)
print("opened database " + db)

#srcIn = input("what field do you want to search (id, name, age, or gender)?")
#srcQuery = input("what result do you want to find from the ", srcIn, " search?")
#srcOut = input("what field do you want to return (id, name, age, or gender) (has to be different than original query)?")

cursor = conn.execute('''SELECT id, name, age, gender FROM RESULTS''')
for row in cursor:
    print("ID: ", row[0], " NAME: ", row[1], " AGE: ", row[2], " GENDER ", row[3])

conn.close()
print("closed database " + db)
