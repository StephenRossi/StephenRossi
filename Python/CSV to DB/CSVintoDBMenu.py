import sqlite3, time, sys


csv = open("NamesTest.csv", "r")
db = sqlite3.connect('CSVDataTransfer.db')
print ("opened CSVDT database successfully")

q = ('''CREATE TABLE IF NOT EXISTS Data (
         Data TEXT PRIMARY KEY NOT NULL);''')


def mainMenu():
    csv = open("NamesTest.csv", "r")
    csv.open = open("NamesTest.csv", "r")
    
    print('''
             #############################
             #         MAIN MENU:        #
             #        1. View .csv       #
             #        2. View .db        #
             #       3. Insert to db     #
             #         4.Clear db        #
             #          5. Exit          #
             #                   -DuckZ  #
             #############################
                   What would you like to do? ''')
    choice = str(input("Please pick an option, 1-5:"))
    parseMenu(choice)

def parseMenu(choice):
    if choice == "1":
        print("Viewing the selected .csv file...")
        time.sleep(.6)
        viewCsv()
    elif choice == "2":
        print("Accessing the database...")
        print(" ")
        time.sleep(.6)
        viewDb()
    elif choice == "3":
        print("starting 'insertToDb()' function")
        time.sleep(.6)
        insertToDb()
    elif choice == "4":
        print("Proceding to 'clearDb()' funtion...")
        time.sleep(.3)
        clearDb()
    elif choice == "5":
        print("Thank you for using this Menu, cya layer boiiiiiii")
        time.sleep(.4)
        db.close
        csv.close
        print("Closed CSV-DT database successfully")
        time.sleep(.4)
        print("adios!")
        sys.exit()
    else:
        print("Error!")
        errorChoice()


def viewCsv():
    csv = open("NamesTest.csv", "r")
    print(" ")
    print(" ")
    print(csv.read())
    print(" ")
    print(" ")
    time.sleep(.3)
    print("Returning to menu")
    mainMenu()

def viewDb():
    cursor = db.execute("SELECT data FROM Data")
    print(" ")
    print("  ----------------------  ")
    print("| Table 'Data' in CSVDT: |")
    print("  ----------------------  ")
    for row in cursor:
        print (row[0])
        print (" ")
    print("X"*50)
    print(" ")
    print ("Table 'Data' successfull opened.")
    time.sleep(.4)
    print("Returning to menu..")
    time.sleep(.5)
    mainMenu()

def insertToDb():
    csv = open("NamesTest.csv", "r")
    data = csv.read()
    db.execute("INSERT INTO Data (Data) VALUES (?)",
             (data,))
    db.commit()
    print ("data inserted to table 'Data'")
    print ("Connection closed")
    time.sleep(.5)
    mainMenu()

def errorChoice():
    print("Obviously you didnt read the instructions correctly. This time try a number that is between 1 and 5 ^.^")
    time.sleep(.7)
    mainMenu()
def clearDb():
    confirm = str(input("Are you sure you want to clear your 'CSVDT.bd' database? y or n: "))
    
    if confirm == "y":
        print("proceding to clear 'CSVDT' database...")
        time.sleep(.5)
        db.execute(''' DROP TABLE Data ''')
        db.execute('''CREATE TABLE Data(
             Data TEXT PRIMARY KEY NOT NULL);''')
        print("Table cleared and reset")
        time.sleep(.3)
        print("Returning to menu")
        mainMenu()
    elif confirm == "n":
        print("That was close, returning to manu...")
        time.sleep(.4)
        mainMenu()
    else:
        print("Error! Lets try that again shal we?")
        time.sleep(.2)
        clearDb()
    

mainMenu()
