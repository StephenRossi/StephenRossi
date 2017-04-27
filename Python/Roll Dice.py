import random, sys, math, statistics

#Rolling Dice
sides = 6
start = 0
dice = 0
outcomes = []
def getAmountOfDice():
    global dice
    ammount = int(input("How many Dice would you like to roll? \n >>>"))
    print("")
    dice = ammount
    return dice
def rollDice():
    i = 1
    while i <= dice:
        x = random.randint(1, sides)
        #print(x)
        outcomes.append(x)
        i += 1
    print("Your rolled",outcomes)
    print("")

def doMath():
    print("Calculating the math for your", dice, "dice rolls...")
    print("")
    displayMath()
    
def displayMath():
    putInOrder()
    getMean()
    getMedian()
    getMode()
    getVarianceStandDev()
    getRange()

def putInOrder():
    outcomes.sort()
    print("           This is your sorted list of outcomes:",outcomes,)

def getMean():
    length = len(outcomes) 
    x = length
    y = outcomes
    mean = sum(y) / x
    print("           Mean:",mean,)

def getMedian():
    length = len(outcomes) -1
    median = length / 2
    x = round(median)
    if x % 2 == 0:
        y = x-1
        median = (outcomes[x]+outcomes[y])/2
        print("           Median:", median)
    else:
        print("           Median:",outcomes[x],)
        
def getMode():
    a = outcomes
    counter = [0,0,0,0,0,0]
    for i in a:
        if i == 1:
            x = counter[0]
            var = x+1
            counter[0] = var
        elif i == 2:
            x = counter[1]
            var = x+1
            counter[1] = var
        elif i == 3:
            x = counter[2]
            var = x+1
            counter[2] = var
        elif i == 4:
            x = counter[3]
            var = x+1
            counter[3] = var
        elif i == 5:
            x = counter[4]
            var = x+1
            counter[4] = var
        elif i == 6:
            x = counter[5]
            var = x+1
            counter[5] = var
        else:
            print("what, howd I get here.")
    number = max(counter) #This counts the max number in array counter
    print("           Mode Counter:",counter)
    print("           Mode:",mode)
            
def getRange():
    length = len(outcomes)
    x = outcomes[length -1]
    Range = x - outcomes[0]
    print("           Range:",Range,)

def getSum():
    x = sum(outcomes)
    print("           Sum:",x,)

def getVarianceStandDev():
    length = len(outcomes) 
    l = length
    y = outcomes
    mean = sum(y) / l
    var = []
    x = len(outcomes) -1
    for i in (outcomes):
        h = i - mean
        z = h ** 2
        var.append(z)
        
    s = sum(var)
    finalVar = s/l
    standardDev = math.sqrt(finalVar)
    print("           Variance(σ2):",finalVar)
    print("           Standard Deviation(σ):",standardDev)

def doIt():
    getAmountOfDice()
    rollDice()
    doMath()
doIt()
        
