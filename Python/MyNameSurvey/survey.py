import sqlite3
import sys

name = str(input("What's your name?"))
print(name, "is your name. Thank you.")

print("----------------------------------")

age = int(input("How old are you? Please just input a number. >"))
print(age, "is", name, "'s age.")

print("----------------------------------")

gender = str(input("Are you male or female? >"))
print("Okay. So you're a", gender, ".")

print("----------------------------------")

print("So", name, "is a", age, "year old", gender, ". Is this information correct?")
confirm = str(input("Please answer with yes or no."))
print("Okay, Thank you", name, ", that will be all!")

print("----------------------------------")


conn = sqlite3.connect('survey.db')
print ("opened survey database successfully")


conn.execute("INSERT INTO Input (NAME, AGE, GENDER) VALUES (?, ?, ?)",
             (name, age, gender))
conn.commit()
conn.close()
print ("data inserted to table 'Input'")
print ("Connection closed")








