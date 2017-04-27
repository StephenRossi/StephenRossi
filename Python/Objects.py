class Meme:
    dankMeter = 0
    spiceMeter = 1 
    name = ""
    def sparkTheImagination(self):
        self.dankMeter = self.dankMeter + 1
    def captivate(self):
        self.spiceMeter = self.spiceMeter * 10
    def ooze(self):
        self.dankMeter -= 3
        self.spiceMeter /= 5
    def display(self):
        print("Name: " + self.name)
        print("Spice: " + str(self.spiceMeter))
        print("Dank: " + str(self.dankMeter))
       
