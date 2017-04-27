#################################
# BINARY ENCODER AND DECODER V1 #
#       by Thomas Howells       #
#################################

import random, string, sys

def menu():
	print("-------------------")
	print("|    MAIN MENU    |")
	print("|                 |")
	print("| 1. Encode Text  |")
	print("| 2. Decode Text  |")
	print("| 3. Quit         |")
	print("-------------------")
	parseMenu()

def parseMenu():
	menuChoice = input("Type the number of what you want to do >>> ")
	if(menuChoice == "1"):
		encode()
	elif(menuChoice == "2"):
		decodeQuestion()
	elif(menuChoice == "3"):
		quit()
	else:
		print("Try again")
		parseMenu()

def encode():
	text = input("Enter the text you want to encode. >>> ")
	textIn = text + "`" #adding signal character for end of inputted text in textIn
	multiple = 16
	while len(textIn) % multiple != 0:
		textIn = textIn + random.choice(string.ascii_lowercase)
		#loop adds random characters until textIn is a multiple of 16

	textInBinary = []
	for i in textIn:
		textInBinary.append("0b0" + "".join(format(ord(i), "b")))
		#loop turns each character in textIn to binary from normal text and adds to an array
		#0b0 has to be added or the strings will not be treated as binary numbers

	binaryKey = []
	for i in range(1):
		placeholder = ""
		#placeholder string created to create a random 8-bit binary string
		for j in range(8):
			placeholder = placeholder + str(random.randint(0, 1))
			#adds random bit to the end of the placeholder string until it is 8 bits long
		binaryKey.append("0b" + placeholder)
		#loop repeats until the binaryKey array has 16 places filled with randomized binary data

	encodedArr = []
	j = 0 
	for i in range(len(textInBinary)):
		if j > len(binaryKey): #starts a secondary loop to measure which binaryKey address to access
			j = 0
		xor = int(textInBinary[i], 2) ^ int(binaryKey[j], 2) #performs xor operator on binary
		# xor example
		# str1 = 0 0 1 1
		# str2 = 0 1 0 1
		# out  = 0 1 1 0
		encodedArr.append("0b{0:08b}".format(xor))
		#loop runs until each part of textInBinary has been xor'd by a binaryKey part
	print("Your original inputted text of '" + text + "' has been encoded as:")
	for i in range(len(encodedArr)):
		print(encodedArr[i], sep = "", end = "", flush = True)
		#makes sure that this all prints on one line for easy copying and pasting
	print("\nThe randomly generated 128-bit key is: ")
	for i in range(len(binaryKey)):
		print(binaryKey[i], sep = "", end = "", flush = True)
		#makes suer that this all prints on one line for easy copying and pasting
	print("\nYou're going to need both of these if you want to decode your message, so write them down or copy and paste them somewhere safe!")
	input("Hit enter when you're ready to return to the main menu.")
	menu()

def decodeQuestion():
	question = input("Do you have both encoded text and the key? (input 'y' for yes, 'n' for no) >>> ")
	if question == "y":
		decode()
	else:
		print("Returning you to the main menu to encode some text.")
		input("Hit enter when you're ready to return to the main menu.")
		menu()

def decode():
	encodedText = input("Please input your encoded text. >>> ")
	encodedTextArr = []
	while encodedText:
		encodedTextArr.append(encodedText[:10])
		encodedText = encodedText[10:]
		#splits encoded text into 10 character blocks and appends them to an array
	key = input("Please input your key. >>> ")
	keyArr = []
	while key:
		keyArr.append(key[:10])
		key = key[10:]
		#splits key into 10 character blocks and appends them to an array
	
	decodedBinArr = []
	j = 0
	for i in range(len(encodedTextArr)):
		if j > len(keyArr):
			j = 0
		xor = int(encodedTextArr[i], 2) ^ int(keyArr[j], 2)
		#xor is the only operation that's reversible
		decodedBinArr.append("0b{0:08b}".format(xor))

	decodedText = ""
	for i in range(len(decodedBinArr)):
		placeholder = format(int(decodedBinArr[i], 2), "c")
		#formats the binary into an integer which is then converted to the character corresponding to the ascii number
		if placeholder == "`":
			#if the signal character is detected it will print the decoded text and skip the character and the randomly-generated padding characters
			print("Here's your decoded text: " + decodedText)
			input("Hit enter when you're ready to return to the main menu.")
			menu()
		else:
			decodedText = decodedText + placeholder
			#if the character detected is anything but a "`"" then it will add it to the end of the decodedText string


def quit():
	print("Thank you for using my science fair project!")
	sys.exit()

menu()
#all the functions execute each other so I only have to run one function when the program starts
