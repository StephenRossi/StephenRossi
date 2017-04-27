halfSum = 0
length = 0
firstValue = 0
listOfVariable = []
listSum = 0

total = 0
inpt = 0
def getInputFromUser():
    global inpt
    inpt = int(input("Pick a year/number boi >>"))
    return inpt
def halfSum():
    global halfSum
    halfSum = inpt/2
    return halfSum
def calcTotal():
    global listSum
    listSum = sum(listOfVariable)
    return listSum
def tryAgain():
    global listSum
    global listOfVariable
    listSum = 0
    listOfVariable = []

def getIt():
    getInputFromUser()
    for i in range (1, halfSum):
        global total
        global listOfVariable
        c = i
        while (c < halfSum) and (listSum < inpt):
            listOfVariable.append(c)
            c +=1
        calcTotal()
        if listSum == inpt:
            global length
            global firstValue
            length = len(listOfVariable)
            firstValue = listOfVariable[0]
            return length
            return firstValue
            displayAll()
        else:
            tryAgain()

def displayAll():
    print("First Value of the string is:", firstValue)
    print("Lengthof the string is: ", firstValue)
    print("The entire string is:", listOfVariable)

    
        
            
getIt()

