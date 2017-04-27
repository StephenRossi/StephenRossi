import sys
import time

arr = []

def printMenu():
   print("********************************************")
   print("********************************************")
   print("*                                          *")
   print("*                 Array Menu               *")
   print("*              1. Create Array             *")
   print("*              2. Display Array            *")
   print("*               3. Sort Array              *")
   print("*              4. Insert Values            *")
   print("*              5. Reverse Array            *")
   print("*                  6. Exit                 *")
   print("*                                          *")
   print("********************************************")
   print("********************************************")
   x = str(input(" What would you like to do? >"))
   parseMenu(x)

def parseMenu(x):
   global arr
   if x == "1":
       print("Create Array:")
       arr = createArray()
   elif x == "2":
       print("Display Array:")
       displayArray(arr)
   elif x == "3":
       print("Sort Array:")
       sortArray(arr)
   elif x == "4":
       print("Insert Values into Array")
       insertArray(arr)
   elif x == "5":
       print("Reverse Array:")
       reverseArray(arr)
   elif x == "6":
       print("Exiting Menu!")
       exitMenu()
   else:
       print("Error!")
       printMenu()


def createArray():
    global arr
    print("Please insert 8 values you want when asked in the array below:")

    print(" "*20,"-"*5,"Create Array","-"*5)
    a = int(input("Array Value One >"))
    print("arr[0] is now set to,", a)
    print(" ")
    b = int(input("Array Value Two >"))
    print("arr[1] is now set to,", b)
    print(" ")
    c = int(input("Array Value Three >"))
    print("arr[2] is now set to,", c)
    print(" ")
    d = int(input("Array Value Four >"))
    print("arr[3] is now set to,", d)
    print(" ")
    e = int(input("Array Value Five >"))
    print("arr[4] is now set to,", e)
    print(" ")
    f = int(input("Array Value Six >"))
    print("arr[5] is now set to,", f)
    print(" ")
    g = int(input("Array Value Seven >"))
    print("arr[6] is now set to,", g)
    print(" ")
    h = int(input("Array Value Eight >"))
    print("arr[7] is now set to,", h)
    print("--"*5)

    arr = [a, b, c, d, e, f, g, h]

    time.sleep(.3)

    print("Array creation is now complete, you are being taken back to the menu...")
    time.sleep(.3)
    printMenu()
    return arr

def displayArray(arrz):
    print("The current array assigned with be shown below:")
    time.sleep(.1)
    print("- ")
    print("  ")
    print(arrz)
    print("  ")
    print("- ")
    time.sleep(.4)
    printMenu()
    
def sortArray(arrz):
    global arr
    print("Sorting the Array");
    arrz.sort()
    time.sleep(.4)
    print("- ")
    print("  ")
    print(arrz)
    print("  ")
    print("- ")
    printMenu()
    return arrz
    

def insertArray(arrz):
    print("   ~-+-~   ")
    a = int(input("Which array value ( [0] and up ) would you like to (re)assign?"))
    print("  ")
    print("   ~-+-~   ")
    print("  ")
    b = int(input("What value would you like to assign to that spot in the array?"))
    print("  ")
    print("   ~-+-~   ")
    print("  ")
    time.sleep(.4)
    print("  ")
    x = arr[a] = b
    print(b,"has been inserted into array at arr[",a,"]")
    time.sleep(.5)
    printMenu()

def reverseArray(arrz):
    global arr
    print("Sorting the array from greatest to lowest");
    arrz.sort(reverse = True)
    time.sleep(.4)
    print("- ")
    print("  ")
    print(arrz)
    print("  ")
    print("- ")
    printMenu()
    return arrz

def exitMenu():
    time.sleep(.4)
    print("Goodbye!")
    sys.exit


printMenu()
