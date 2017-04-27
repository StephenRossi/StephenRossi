import sqlite3

db = "Survey.db"
conn = sqlite3.connect(db)
print("opened database " + db)

name = input("What is your name?")
print(name, "is your name. Thank you.")

print("----------------------------------")

age = input("How old are you? Please just input a number. ")
print(age, "is", name, "'s age.")

print("----------------------------------")

gender = input("Are you male or female?")
print("Okay. So you're a", gender, ".")


conn.execute('''INSERT INTO RESULTS (name, age, gender) VALUES (?, ?, ?)''', (name, age, gender))
print("results inserted")

conn.commit()
print(db + " committed")

conn.close()
print("closed database " + db)
