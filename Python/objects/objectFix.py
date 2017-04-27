needMH = True
needFH = True
for i in studentArray:
        if needMH == True:
                i.displayHeadline("Male Students")
                needMH = False
        if i.getGender() == "Male":
                i.addBee("-Bumble")
                i.display()
        if needFH == True:
            i.displayHeadline("Female Students")
            needSw = False
            
        if i.getGender() == "Female":
                i.addBee("-Honey")
                i.shortDisplay("$  ")  

  
