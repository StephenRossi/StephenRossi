import sys, time, sqlite3

def mainMenu():
    print(" ______________________________________________________________________________")
    print("|     ___  ___       ___   _   __   _       ___  ___   _____   __   _   _   _  |")
    print("|    /   |/   |     /   | | | |  \ | |     /   |/   | | ____| |  \ | | | | | | |")
    print("|   / /|   /| |    / /| | | | |   \| |    / /|   /| | | |__   |   \| | | | | | |")
    print("|  / / |__/ | |   / /_| | | | | |\   |   / / |__/ | | |  __|  | |\   | | | | | |")
    print("| / /       | |  / /  | | | | | | \  |  / /       | | | |___  | | \  | | |_| | |")
    print("|/_/        |_| /_/   |_| |_| |_|  \_| /_/        |_| |_____| |_|  \_| \_____/ |")
    print("|______________________________________________________________________________|")
    print("                   |                                        |                   ")
    print("                   |                                        |                   ")
    print("                   |                1.Diet                  |                   ")
    print("                   |                2.Workout               |   Chose what      ")
    print("                   |                3.View DB               |   section you     ")
    print("                   |                4.Exit DB               |   would like to   ")
    print("                   |                                        |   go into below:  ")
    print("                   |                         - By: DuckZ    |                   ")
    print("                   |________________________________________|                   ")
    choice = str(input("                                  ----> :               "))
    parseMenu(choice)

def parseMenu(choice):
    if choice == "1":
        print("go into diet")
        dietMenu()
    elif choice == "2":
        print("go into workout")
        workoutMenu()
    elif choice == "3":
        print("view DB")
        viewDB()
    elif choice == "4":
        print("Exit DB")
        sys.exit()
    else:
        print("Error!!", choice,", is not a valid choice.")
        time.sleep(.4)
        mainMenu()

def dietMenu():
        print('''
         _____ _      _     __  __                 
        |  _  |(_)   | |   |  \/  |                 
        | | | |_  ___| |_  | .  . | ___ _ __  _   _ 
        | | | | |/ _ \ __| | |\/| |/ _ \ '_ \| | | |
        | |/ /| |  __/ |_  | |  | |  __/ | | | |_| |
        |___/ |_|\___|\__| \_|  |_/\___|_| |_|\__,_|
      /|______________________________________________|\
                   |                      |
                   |                      |
                   |                      |
                   |                      |
                   |                      |
                   |                      |
                   |______________________|
                   
    ''')        

def workout():
    print("hi")
mainMenu() 
