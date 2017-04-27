
class myIsol:

    isItPrimeNum = 0
    halfTotalz = 0
    primeArray = []
    
    def isPrime(self, num):
        startLoop = 2
        halfTotalz = num/2
        print(startLoop, halfTotalz)
        while startLoop <= halfTotalz:
            check = num/startLoop
            startLoop += 1
            if float(check).is_integer() == True:
                return False
            
        return True
    
    def findPrimes(self, x, y):
        while x <= y:
            if self.isPrime(x):
                self.primeArray.append(x)
            x += 1

    def getPrimeCount(self):
        return len(self.primeArray)

    def getPrimeArray(self):
        return self.primeArrayZ

i = myIsol()
#print(i.isPrime(7))
#print(i.isPrime(101))
i.findPrimes(7, 29)
print(i.primeArray)




