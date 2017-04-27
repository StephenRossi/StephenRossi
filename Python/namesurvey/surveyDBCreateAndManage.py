import sqlite3

db = "Survey.db"
conn = sqlite3.connect(db)
print("opened database " + db)

conn.execute('''DROP TABLE RESULTS''')

conn.execute('''CREATE TABLE RESULTS(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	age TEXT NOT NULL,
	gender TEXT NOT NULL);''')
print("results table created")

conn.close()
print("closed database " + db)
