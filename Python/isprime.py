isItPrimeNum = 0
halfTotalz = 0


def getIsItPrimeNum():
    global isItPrimeNum
    isItPrimeNum = int(input("Insert a number to check if its prime \n     >>>"))
    return isItPrimeNum
def getHalfPrimeNum():
    global halfTotalz
    halfTotalz = isItPrimeNum/2
    return halfTotalz
def isPrime():
    startLoop = 2
    print(startLoop, halfTotalz)
    while startLoop <= halfTotalz:
        check = isItPrimeNum/startLoop
        startLoop += 1
        print(startLoop, isItPrimeNum, check)
        if float(check).is_integer() == True:
            return False
    return True
     
def otherThing():
    if isPrime() == False:
        print("This is not a prime number!")
        print("")
        print("X~","-"*50,"~X")
        print("")
    else:
        print("Hey, its prime!")
        print("")
        print("X~","-"*50,"~X")
        print("")
def clearCache():
    global isItPrimeNum
    global halfTotalz
    isItPrimeNum = 0
    halfTotalz = 0
    return isItPrimeNum
    return halfTotalz
def doAll():
    i=1
    while i <10:
        getIsItPrimeNum()
        getHalfPrimeNum()
        otherThing()
        i +=1

doAll()


