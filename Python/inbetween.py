

def inbetween(x):
	if x > 0 and x < 6:
		return "ClassOne"
	elif x > 5 and x < 11:
		return "ClassTwo"
	elif x > 10 and x < 16:
		return "ClassThree"
	elif x > 15 and x < 21:
		return "ClassFour"
	elif x > 20 and x < 26:
		return "ClassFive"
	elif x > 26:
		return "tooBigOfANumberLooser"
	else:
		return False
	



def getClass(x):
    if inbetween(x) == "ClassOne":
        print("Its part of Class One inbetween 1 and 5")
    elif inbetween(x) == "ClassTwo":
        print("Its part of Class Two inbetween 6 and 10")
    elif inbetween(x) == "ClassThree":
        print("Its part of Class Three inbetween 11 and 15")
    elif inbetween(x) == "ClassFour":
        print("Its part of Class Three inbetween 16 and 20")
    elif inbetween(x) == "ClassFive":
        print("Its part of Class Three inbetween 21 and 25")
    elif inbetween(x) == "Class":
        print("This is out of my Class Range")
    else:
        print("Error!")
