#############################
#                           #
#   Encrypted Messaging:    #
#     -by Stephen Rossi     #
#               ~ DuckZTV   #
#                           #
#############################
import sys, time


def mainMenu():
    print("#################################")
    print("#                               #")
    print("#     1. Encode a Message       #")
    print("#     2. Decode a Message       #")
    print("#     3. Exit                   #")
    print("#                  -DuckZTV     #")
    print("#                               #")
    print("#################################")
    c = str(input("What would you like to do?"))
    parseMenu(c)

def parseMenu(choice):
    if choice == "1":
        print("Proceding...")
        time.sleep(.3)
        encode()
    elif choice == "2":
        print("Proceding...")
        time.sleep(.3)
        decode()
    elif choice == "3":
        time.sleep(.3)
        print("Okay, Goodbye Fried!")
        time.sleep(.9)
        sys.exit()
    else:
        print("Error!")
        time.sleep(.3)
        error()
        
def encode():
    message = str(input("Please type the message you would like to encode below:"))
    print("Please wait while your message is being encoded...")
    if message 

def decode():
    print("not started!")
    mainMenu()

def error():
    print("Error, please choose a valid option!")
    c = str(input("What would you like to do?"))
    parseMenu(c)

mainMenu()


    
