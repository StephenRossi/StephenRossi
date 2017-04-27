import sys, math


def deezbeez():
    x = input("Please Insert 2 Values That Add Up To A 4 Digit Year: ")
    if len(x) == 4:
        print("Good Job, You Can Read!")
        goOn(x)
    else:
        print("HEY DER, U DONE DID IT FELLR. RETRY!")
        deezbeez()

def goOn(x):
    
    print(x)
deezbeez()

