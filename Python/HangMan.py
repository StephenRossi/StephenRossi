import math, sys, random
easyArray = ["House", "Car", "Fish", "Dog", "People", "Math", "Memes", "Dank", "Sweg", "Looser", "DuckZ", "Duck", "Moose", "Animal", "Pizza", "Can", "Worms"]
mediumArray = ["Burrito", "Relationship", "Christmas", "Cytoskeleton", "Champion", "Baseball", "Students", "Teacher", "Community","Bizbappo", "Dictator", "Universe",]
wordLen = 0
word = ""
wrongCount = 0
userGuess = 0
wordList = []
correctLetters = []
wrongLetters = []
lettersGuessed = []

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
    wordList.append(word)
    wordLen = len(word)
    startGame()
def setDifficultyHard():
    print("This difficulty has not been set up, try easy!")
def setDifficultyImpossible():
    print("This difficulty has not been set up, try easy!")


def startGame():
    print("                               ___________________")
    print("           ____________  ")
    print("          |            |       ", " X " *wrongCount)
    print("          |            |       ___________________")
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
    guessLetter()                                             #does the way I did this now fix the problem with the user not being able to guess another character
                                                              #  now that it is, or at least this section more towards finished?
def guessLetter():
    global userGuess
    userGuess = 0
    userGuess = input("Guess a single letter to see if it is in the word! \n >>>")
    inputLen = len(userGuess)
    if inputLen > 1:
        print("")
        print("")
        print(" ______________________________________________")
        print("|                                              |")
        print("|   You can only guess one letter! Try again!  |")
        print("|______________________________________________|")
        print("")
        guessLetter()
    else:                                  
        for i in wordList:
            if userGuess.upper() in lettersGuessed:                           #Creating this so someone can not guess the same letter twice.
                print("")
                print("")
                print(" ________________________________________________________________")
                print("|                                                                |")
                print("|   This letter has alread been guessed silly goober, try again! |")
                print("|________________________________________________________________|")
                print("")
                guessLetter()
            elif userGuess.upper() in i.upper():
                correct()
                
            else:
                print("")
                wrong()
                                                             
                                                             # Note to self, write out step by step code on scrap paper tomorrow morning <><><><>><><><><><><<><>
def correct():
    correctLetters.append(userGuess.upper())
    lettersGuessed.append(userGuess.upper())
    if len(correctLetters) == len(word):
        print(" OMAH GAHD YA DONE DID IT FELLR")
        gameWon()
    else:
        print(" ________________________________________________________________________")
        print("|                                                                        |")
        print("|   That was correct! There is at least one", userGuess, "in this word!  |")
        print("|________________________________________________________________________|")
        print("")
        print(userGuess)
        nextRound()
    
def gameWon():
    print("")
    print("")
    print( '''
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗ ██████╗ ███╗   ██╗██╗    
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██╔═══██╗████╗  ██║██║    
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║   ██║██╔██╗ ██║██║    
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║   ██║██║╚██╗██║╚═╝    
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║ ╚████║██╗    
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝
   ''')
    print("")
    print("")
    x = str(input("Would you like to play again?  y/n \n >>>"))
    goAgain(x)

def wrong():
    global wrongCount
    print(" ____________________________________________________")
    print("|                                                    |")
    print("|   Sorry but...", userGuess, "is not in this word   |")
    print("|____________________________________________________|")
    print("")
    print(userGuess)
    wrongLetters.append(userGuess.upper())
    lettersGuessed.append(userGuess.upper())
    wrongCount += 1
    nextRound()
    
def nextRound():
    if wrongCount == 0:
        print("                               ___________________")
        print("           ____________  ")
        print("          |            |       ", " X " *wrongCount)
        print("          |            |       ___________________")
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
        guessLetter()
    elif wrongCount == 1:
        print("                               ___________________")
        print("           ____________  ")
        print("          |            |       ", " X " *wrongCount)
        print("          |            |       ___________________")
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
        print("                               ___________________")
        print("           ____________  ")
        print("          |            |       ", " X " *wrongCount)
        print("          |            |       ___________________")
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
        print("                               ___________________")
        print("           ____________  ")
        print("          |            |       ", " X " *wrongCount)
        print("          |            |       ___________________")
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
        print("                               ___________________")
        print("           ____________  ")
        print("          |            |       ", " X " *wrongCount)
        print("          |            |       ___________________")
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
        print("                               ___________________")
        print("           ____________  ")
        print("          |            |       ", " X " *wrongCount)
        print("          |            |       ___________________")
        print("          |           ___")
        print("          |          /. .\ ")
        print("          |         |   > |  Wrong letters guessed X:", )
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
    print("                               ___________________")
    print("           ____________  ")
    print("          |            |       ", " X " *wrongCount)
    print("          |            |       ___________________")
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
        wordLen = 0
        word = ""
        wrongCount = 0
        userGuess = 0
        wordList = []
        correctLetters = []
        wrongLetters = []
        lettersGuessed = []
        startDisplay()
    elif goAgain == "n":
        print("Come again soon!")
        sys.exit()
    else:
        print("Wach u sayin?")
        x = str(input("Would you like to play again?  y/n \n >>>"))
        goAgain(x)

startDisplay()

