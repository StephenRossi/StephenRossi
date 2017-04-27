import sqlite3
import sys

def printMenu():
    print("*******************************************")
    print("*******************************************")
    print("**                                       **")
    print("**            1) Input data              **")
    print("**            2) Select data             **")
    print("**            3) Delete Table            **")
    print("**              4) Exit                  **")
    print("**                                       **")
    print("*******************************************")
    print("*******************************************")
    x = str(input("Select what you want to do."))
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
        print("exiting...")
        exitMenu()
    else:
        print("error!!")
        printMenu()

def inputData():
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
    printMenu()

def selectData():
    conn = sqlite3.connect('survey.db')
    print ("Database 'survey.db' succesfully connected")
    cursor = conn.execute("SELECT ID, NAME, AGE, GENDER FROM Input")
    print ("-" *18)
    for row in cursor:
        print ("|NAME = ", row[0])
        print ("|ID = ", row[1])
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

def exitMenu():
    print("*******************************************")
    print("*******************************************")
    print("**                                       **")
    print("**                GOODBYE!               **")
    print("**                                       **")
    print("*******************************************")
    print("*******************************************")
    sys.exit()
    

printMenu()
