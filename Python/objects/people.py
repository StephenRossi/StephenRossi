class Students:
    First_Name = ""
    Last_Name = ""
    Phone_Number = ""
    Gender = ""
    Favorite_Meme = ""
    Favorite_Bee = ""

    def getFirstName(self):
        return self.First_Name
    def setFirstName(self, x):
        self.First_Name = x
    def getLastName(self):
        return self.Last_Name
    def setLastName(self, x):
        self.Last_Name = x
    def getPhoneNumber(self):
        return self.Phone_Number
    def setPhoneNumber(self, x):
        self.Phone_Number = x
    def getGender(self):
        return self.Gender
    def setGender(self, x):
        self.Gender = x
    def getFavoriteMeme(self):
        return self.Favorite_Meme
    def setFavoriteMeme(self, x):
        self.Favorite_Meme = x
    def getFavoriteBee(self):
        return self.Favorite_Bee
    def setFavoriteBee(self, x):
        self.Favorite_Bee = x



    def setFirstNameFromUser(self):
        self.setFirstName(str(input("What is your First Name? :")))
    def setLastNameFromUser(self):
    	self.setLastName(str(input("What is your last name? :")))
    def setPhoneNumberFromUser(self):
    	self.setPhoneNumber(int(input("What is your phone number? : ")))
    def setGenderFromUser(self):
    	self.setGender(str(input("What is your gender? :")))
    def setFavoriteMemeFromUser(self):
    	self.setFavoriteMeme(str(input("What is your favorite meme? :")))
    def setFavoriteBeeFromUser(self):
    	self.setFavoriteBee(str(input("What is your favorite bee? : ")))
        
    def display(self):
        print("___________________________")
        print("")
        print("| First Name:", self.First_Name)
        print("| Last Name:", self.Last_Name)
        print("| Phone Number:", self.Phone_Number)
        print("| Gender:", self.Gender)
        print("| Favorite Meme:", self.Favorite_Meme)
        print("| Facorite Bee:", self.Favorite_Bee)
        print("___________________________")
        

    
        
    
