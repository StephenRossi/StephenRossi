import sqlite3
import sys
import time

def printMenu():
    print("*******************************************")
    print("*******************************************")
    print("**                  Menu                 **")
    print("**                 ------                **")
    print("**         1) Input data                 **")
    print("**         2) Select data                **")
    print("**         3) Delete data                **")
    print("**         4) Clear entire table         **")
    print("**         5) Exit                       **")
    print("**                                       **")
    print("*******************************************")
    print("*******************************************")
    x = str(input("Select what you want to do. >"))
    parseMenu(x)

def parseMenu(x):
    if x == "1" :
        print("Input Data:")
        inputData()
    elif x == "2":
        print("Select Data:")
        selectData()
    elif x == "3":
        print("Delte Data:")
        deleteData()
    elif x == "4":
        print("Clear Entire Table:")
        clearTable()
    elif x == "5":
        print("exiting...")
        exitMenu()
    else:
        print("error!!")
        printMenu()

def inputData():
    time.sleep(.2)
    name = str(input("What is the name of the person being inputed? >"))
    print(name, "is the name. Thank you.")

    print("----------------------------------")

    age = int(input("How old are they? Please just input a number. >"))
    print(age, "is", name, "'s age.")

    print("----------------------------------")

    gender = str(input("Are they male or female? >"))
    print("Okay. So",name,"is a", gender, ".")

    print("----------------------------------")

    print("So", name, "is a", age, "year old", gender, ". Is this information correct?")
    confirm = str(input("Please answer with yes or no."))
    print("Okay, Thank you", name, ", that will be all!")

    print("----------------------------------")
    time.sleep(.4)
    
    conn = sqlite3.connect('survey.db')
    print ("Database 'survey.db' succesfully connected")

    conn.execute("INSERT INTO Input (NAME, AGE, GENDER) VALUES (?, ?, ?)",
             (name, age, gender))
    conn.commit()
    conn.close()
    print ("data inserted to table 'Input'")
    print ("Connection closed")
    time.sleep(.5)
    printMenu()

def selectData():
    time.sleep(.2)
    conn = sqlite3.connect('survey.db')
    print ("Database 'survey.db' succesfully connected")
    cursor = conn.execute("SELECT ID, NAME, AGE, GENDER FROM Input")
    print ("-" *18)
    for row in cursor:
        print ("|ID = ", row[0])
        print ("|NAME = ", row[1])
        print ("|AGE = ", row[2])
        print ("|GENDER = ", row[3])
        print ("-" * 18)
    print ("Table 'Input' successfull opened")
    conn.close()
    printMenu()

def deleteData():
    getid = str(input("What is the id of the set of data you want to delete?"))
    print(getid, "is the id.?")
    input("please respond with yes or no after you have confidrmed this is the correct id")
    print("thank you, continuing to delte record")
    
    conn = sqlite3.connect('survey.db')
    print ("opened database 'survey.db' successfully")

    conn.execute("DELETE FROM Input WHERE ID=?", (getid))
    conn.commit()
    conn.close()
    print ("Record Delted")
    print ("Connection closed")
    printMenu()

def clearTable():
    conn.execute('''DROP TABLE Input''')
    conn.execute('''CREATE TABLE Input(
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NAME TEXT NOT NULL,
	AGE INTEGER NOT NULL,
	GENDER TEXT NOT NULL);''')
    print("Table has been reset and cleared.")
    time.sleep(.5)
    printMenu()

def exitMenu():
    print("*******************************************")
    print("*******************************************")
    print("**                                       **")
    print("**                GOODBYE!               **")
    print("**                                       **")
    print("*******************************************")
    print("*******************************************")
    time.sleep(1)
    sys.exit()
    
conn = sqlite3.connect('survey.db')
print ("opened survey database successfully")
printMenu()
