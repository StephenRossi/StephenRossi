import math, sys, random
easyArray = ["House", "Car", "Fish", "Dog", "People", "Math", "Memes", "Dank", "Sweg", "Looser", "DuckZ", "Duck", "Moose", "Animal", "Pizza", "Can", "Worms"]
mediumArray = ["Burrito", "Relationship", "Christmas", "Cytoskeleton", "Champion", "Baseball", "Students", "Teacher", "Community"]
wordLen = 0
word = ""
wrongCount = 0
userGuess = 0
#
# emk
# if you access global variables (global wordList)   <x>
# they need to be defined globally
#
wordList = []

def startDisplay():
    print("")
    print("           ____________")
    print("          |            |")
    print("          |            |")
    print("          |           ___")
    print("          |          /. .\                +~=+~=+~=+~=+~=+~=+~=+~=+~=+~=+~=+~=+~=+~=+~=+~=+~=+")
    print("          |         |   > |               x    1. Easy - 1 Word, 6 characters max            x")
    print("          |         | \__/|               +    2. Medium - 1 Word, 12 characters max         +")
    print("          |          \___/                +    3. Hard - 1 or 2 Words, 18 characters max     +")
    print("          |        \__ | __/              x    4. Impossible - No character or word limit    x")
    print("          |           \|/                 +~=+~=+~=+~=+~=+~=+~=+~=+~=+~=+~=+~=+~=+~=+~=+~=+~=+")
    print("          |            |")
    print("          |           / \ ")
    print("          |         _/   \_")
    print("    --------------")
    print("")
    print("                              H A N G M A N   |   G A M E")
    print("                              _ _ _ _ _ _ _       _ _ _ _")
    print("")
    pickWordDifficulty()

def pickWordDifficulty():
    x = input("       Chose the difficulty you would like to play: \n         >>>")
    dificultChoice(x)
def dificultChoice(x):
    #
    # param x is coming in as an int, but you are comparing it
    # to a "string" - i.e. x == "1" - change it to a string first!   <x>
    #
    x = str(x)
    if x == "1":
        setDifficultyEasy()
    elif x == "2":
        setDifficultyMedium()
    elif x == "3":
        setDifficultyHard()
    elif x == "4":
        setDifficultyImpossible()
    else:
        print("retry boi")
        x = input("Chose the difficulty you would like to play \n >>>")
        dificultChoice(x)

def setDifficultyEasy():
    print("")
    print("                    Starting game with easy difficulty!")
    print("")
    global wordLen, word, easyArrLen, pos, wordList, wrongCount
    wrongCount = 0
    easyArrLen = len(easyArray) -1
    pos = random.randint(0,easyArrLen)
    word = easyArray[pos]
    #
    # emk
    # you don't need a list here... just an array of strings...  <X >
    #
    wordList.append(word)
    wordLen = len(word)
    startGame()

def setDifficultyMedium():
    print("")
    print("                    Starting game with medium difficulty!")
    print("")
    global wordLen, word, easyArrLen, pos, wordList, wrongCount
    wrongCount = 0
    mediumArrLen = len(mediumArray) -1
    pos = random.randint(0,mediumArrLen)
    word = mediumArray[pos]
    wordList = list(word)
    wordLen = len(wordList)
    startGame()
    
def setDifficultyHard():
    print("This difficulty has not been set up, try easy!")
def setDifficultyImpossible():
    print("This difficulty has not been set up, try easy!")


def startGame():
    print("")
    print("           ____________")
    print("          |            |")
    print("          |            |")
    print("          |      ")
    print("          |      ")
    print("          |      ")
    print("          |      ")
    print("          |      ")
    print("          |      ")
    print("          |      ")
    print("          |      ")
    print("          |      ")
    print("          |      ")
    print("    --------------")
    print("                              ")
    print("                             ", "_  " * wordLen)
    print(word)
    #
    # emk
    # you are going to need a loop here - so the player can keep  < >
    # guessing the letter...
    #
    guessLetter()

def guessLetter():
    global userGuess
    userGuess = 0
    userGuess = input("Guess a single letter to see if it is in the word! \n >>>")
    inputLen = len(userGuess)
    #
    # emk
    # here is some code i put in to help me figure out what the <x>
    # problem was...
    #
    #print("############################")
    #print(inputLen)
    #print(userGuess)
    #print(wordList)

    if inputLen > 1:
        print("You can only guess one letter! Try again!")
        guessLetter()
    else:
        for i in wordList:
            #
            # emk
            # this was turned around...    <x>
            #
            if userGuess.upper() in i.upper():
                correct()
            else:
                print("")
                #
                # emk
                # the next line was indented incorrectly...   <x>
                #
                wrong()
                                                             # Note to self, write out step by step code on scrap paper tomorrow morning <><><><>><><><><><><<><>
def correct():
    print("That was correct! There is at least one", userGuess, "in this word!")
    print(userGuess)




def wrong():
    global wrongCount
    print("wrong")
    print(userGuess)
    wrongCount += 1
    nextRoundWrong()
def nextRoundWrong():
    if wrongCount == 1:
        print("")
        print("           ____________")
        print("          |            |")
        print("          |            |")
        print("          |           ___")
        print("          |          /   \ ")
        print("          |         |     | ")
        print("          |         |     | ")
        print("          |          \___/ ")
        print("          |      ")
        print("          |      ")
        print("          |      ")
        print("          |      ")
        print("          |      ")
        print("    --------------")
        print("                              ")
        print("                             ", "_  " * wordLen)
        print(word)
        print(wrongCount)
        guessLetter()
    elif wrongCount == 2:
        print("")
        print("           ____________")
        print("          |            |")
        print("          |            |")
        print("          |           ___")
        print("          |          /   \ ")
        print("          |         |     | ")
        print("          |         |     | ")
        print("          |          \___/ ")
        print("          |            |")
        print("          |            |")
        print("          |            |")
        print("          |      ")
        print("          |      ")
        print("    --------------")
        print("                              ")
        print("                             ", "_  " * wordLen)
        print(word)
        print(wrongCount)
        guessLetter()
    elif wrongCount == 3:
        print("")
        print("           ____________")
        print("          |            |")
        print("          |            |")
        print("          |           ___")
        print("          |          /. .\ ")
        print("          |         |   > | ")
        print("          |         | \__/| ")
        print("          |          \___/ ")
        print("          |            |")
        print("          |            |")
        print("          |            |")
        print("          |      ")
        print("          |      ")
        print("    --------------")
        print("                              ")
        print("                             ", "_  " * wordLen)
        print(word)
        print(wrongCount)
        guessLetter()
    elif wrongCount == 4:
        print("")
        print("           ____________")
        print("          |            |")
        print("          |            |")
        print("          |           ___")
        print("          |          /. .\ ")
        print("          |         |   > | ")
        print("          |         | \__/| ")
        print("          |          \___/ ")
        print("          |        \__ | __/")
        print("          |           \|/")
        print("          |            |")
        print("          |      ")
        print("          |      ")
        print("    --------------")
        print("                              ")
        print("                             ", "_  " * wordLen)
        print(word)
        print(wrongCount)
        guessLetter()
    elif wrongCount == 5:
        print("")
        print("           ____________")
        print("          |            |")
        print("          |            |")
        print("          |           ___")
        print("          |          /. .\ ")
        print("          |         |   > | ")
        print("          |         | \__/| ")
        print("          |          \___/ ")
        print("          |        \__ | __/")
        print("          |           \|/")
        print("          |            |")
        print("          |           / \ ")
        print("          |         _/   \_")
        print("    --------------")
        print("                              ")
        print("                             ", "_  " * wordLen)
        print(word)
        print(wrongCount)
        guessLetter()
    elif wrongCount >= 6:
        gameOVer()
    else:
        print("HOW IN DA TACO")
def gameOVer():
    print("")
    print("           ____________")
    print("          |            |")
    print("          |            |")
    print("          |           ___")
    print("          |          /. .\ ")
    print("          |         | <__ | ")
    print("          |         | /  \| ")
    print("          |          \___/ ")
    print("          |        \__ | __/")
    print("          |           \|/")
    print("          |            |")
    print("          |           / \ ")
    print("          |         _/   \_")
    print("    --------------")
    print("                       _____________________________       ")
    print("                      /                             \      ")
    print("                      | ~=+~=+~=+GAME OVER+=~+=~+=~ |      ")
    print("                      \_____________________________/      ")
    print("                            The word was:", word)
    print(wrongCount)
    x = str(input("Would you like to play again?  y/n \n >>>"))
    goAgain(x)

def goAgain(goAgain):
    #goAgain = input("Would you like to play again?  y/n \n >>>")
    if goAgain == "y":
        print("Okay!")
        startDisplay()
    elif goAgain == "n":
        print("Come again soon!")
        sys.exit()
    else:
        print("Why is this not working?")
        x = str(input("Would you like to play again?  y/n \n >>>"))
        goAgain(x)

startDisplay()
