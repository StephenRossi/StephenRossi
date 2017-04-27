class FManip:
    name = ""
    location = ""
    fileType = ""
    dateCreated = ""
    lineCount = 0
    fileHandle = ""
    lineArray = []
    line = ""
    fileOpen = False
    def openFile(self, mode="r"):
        self.fileHandle = open(self.name, mode)
        self.fileOpen = True
    def close(self):
        self.fileHandle.close()
    def closeFile(self):
        self.fileHandle.close()
        self.fileOpen = False
    def readFile(self):
        self.lineArray = self.fileHandle.read().split("\n")
    def printFile(self):
        i = 1
        for line in self.lineArray:
            print(str(i) + " ==> " + line)
            i += 1
    def writeLine(self, x):
        self.fileHandle.write("\n" + x)
        print(x)
   
    def setName(self, name):
        self.name = name
    def writeFile(self, arr):
        for line in arr:
            self.writeLine(line)
    def getLineArray(self):
        return self.lineArray


#################
##   TESTING   ##
#################


f1 = FManip()
f2 = FManip()
f1.setName("FManip.py")
f1.openFile("r")
f1.readFile()
f1.printFile()
f2.setName("looser.txt")
f2.openFile("w")
f2.printFile()
f2.writeFile(f1.getLineArray())
f2.close()
f1.close()
