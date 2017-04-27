import time, sys, math

                                                        #########################################
                                                        #                                       #
                                                        #           - Stephen Rossi -           #
                                                        #              :~DuckZTV~:              #
                                                        #        ~~~~~~~~~~~~~~~~~~~~~~~~       #
                                                        #                2/15/17                #
                                                        #                                       #
                                                        #########################################
                                                        
                    # This project will take a users input(problem set) and will calculate mean, median, mode, range, probability dist., etc.
                    
problemSet1 = []

def mathMenu():
    print( '''
                    _____________________________________
                   |------------ Math Menu 1 ------------|
                   |                                     |
                   |         1. Problem Set Math         |
                   |            2. Exit Menu             |
                   |                                     |
                   |_____________________________________|

    ''')
    getChoice()
    
def getChoice():
    choice = str(input("Please choice your choice[1-2]:"))
    choiceMenu(choice)
    
def choiceMenu(x):
    if x == "1":
        print("good stuff friend")
        getProbSet()
    elif x == "2":
        print("Come back soon friend!")
        time.sleep(.3)
        sys.exit()
    else:
        print("Error, please try again")
        y = str(input("Please chosee your choice[1-2]:"))
        choiceMenu(y)

def getProbSet():
    print('''
                    _____________________________________
                   |------------ Math Menu 2 ------------|
                   |                                     |
                   |        1. Add Another Value         |
                   |          2. Do Some Math!           |
                   |        3. Clear Problem Set         |
                   |      4. Return To Main Menu 1       |
                   |                                     |
                   |_____________________________________|

        Your current problem set is :''')
    print(problemSet1)

    choice2 = str(input("What would you like to do? Please chose form the menu above[1-4]:"))
    choiceMenu2(choice2)

def choiceMenu2(x):
    if x == "1":
        addValue()
    elif x == "2":
        doMath()
    elif x == "3":
        clearSet()
    elif x == "4":
        print("returning to Math Menu 1...")
        time.sleep(.4)
        mathMenu()
    else:
        print("Error! Please try again...")
        time.sleep(.2)
        choice2 = str(input("What would you like to do? Please chose form the menu above[1-4]:"))
        choiceMenu2(choice2)

problemSet1 = []
def addValue():
    arr = int(input("What is the next value in the problem set?"))
    problemSet1.append(arr)
    print("returning to Math Menu 2...")
    time.sleep(.4)
    getProbSet()

def clearSet():
    print('''
                    _____________________________________
                   |------------ Math Menu 3 ------------|
                   |                                     |
                   |      1. Clear Entire Prob. Set      |
                   |         2. Clear One Value          |
                   |       3. Return to Math Menu 2      |
                   |                                     |
                   |_____________________________________|

    ''')
    clearChoice1()
    
def clearChoice1():
    clearChoice = str(input("What would you like to do? Please chose form the menu above[1-4]:")) 
    choice3(clearChoice)

def choice3(x):
    if x == "1":
        confirm = str(input("Are you sure you would like to clear the entire problem set? Y/N"))
        if confirm == "y":
            clearAll()
        elif confirm == "n":
            print("Returning to Math Menu 3...")
            clearSet()
        else:
            print("Error! Please try again...")
            time.sleep(.2)
            choice = str(input("What would you like to do? Please chose form the menu above[1-4]:"))
            choice3(choice)
        
    elif x == "2":
        clearValue()
    elif x == "3":
        print("Returning to Math Menu 2...")
        getProbSet()
    else:
        print("Error! Please try again...")
        time.sleep(.2)
        choseAgain = str(input("What would you like to do? Please chose form the menu above[1-4]:"))
        choice3(choseAgain)

def clearValue():
    print("k")
    clearSet()

def clearAll():            
    print("tryClearAll")
    global problemSet1
    problemSet1 = []
    clearSet()

def doMath():
    print(" ")
    print(" ** ")
    print("     Lets do the math!")
    print(" ** ")
    print(" ")
    print(" ")
    putInOrder()
    getMean()
    getMedian()
    getMode()
    getRange()
    getSum()
    getVarianceStandDev()
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    time.sleep(.8)
    getProbSet()
    

def putInOrder():
    problemSet1.sort()
    print("             This is your sorted Problem Set:",problemSet1,)

def getMean():
    length = len(problemSet1) 
    x = length
    y = problemSet1
    mean = sum(y) / x
    print("           Mean:",mean,)

def getMedian():
    length = len(problemSet1) -1
    median = length / 2
    x = round(median)
    print("           Median:",problemSet1[x],)
def getMode():
    a = outcomes
    
def getRange():
    length = len(problemSet1)
    x = problemSet1[length -1]
    Range = x - problemSet1[0]
    print("           Range:",Range,)

def getSum():
    x = sum(problemSet1)
    print("           Sum:",x,)

def getStandardDeviation():
    print("x")

def getVarianceStandDev():
    length = len(problemSet1) 
    l = length
    y = problemSet1
    mean = sum(y) / l
    var = []
    x = len(problemSet1) -1
    for i in (problemSet1):
        h = i - mean
        z = h ** 2
        var.append(z)
        i += 1
        
    s = sum(var)
    finalVar = s/length
    standardDev = math.sqrt(finalVar)
    print("           Variance(σ2):",finalVar)
    print("           Standard Deviation(σ):",standardDev)
        


        
mathMenu()
