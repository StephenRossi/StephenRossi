import random

##### DEFINING CLASSES, VARIBLES, AND FUNCTIONS #####
class CROP:
	name = ""
	plantDate = 0
	startDate = 0
	seasonLength = 0
	endDate = 0
	harvestDate = 0

	precipitationNeeded = 0.00
	precipitationSinceStart = 0.00
	precipitationPerDay = 0.00

	def getName(self):
		return self.name
	def getPlantDate(self):
		return self.plantDate
	def getStartDate(self):
		return self.startDate
	def getSeasonLength(self):
		return self.seasonLength
	def getEndDate(self):
		return self.endDate
	def getHarvestDate(self):
		return self.harvestDate
	def getPrecipitationNeeded(self):
		return self.precipitationNeeded
	def getPrecipitationSinceStart(self):
		return self.precipitationSinceStart
	def getPrecipitationPerDay(self):
		return self.precipitationPerDay

	def setName(self, x):
		self.name = str(x)

	def displayCROP(self):
		print("name - " + self.getName())
		print("plantDate - " + str(self.getPlantDate()))
		print("startDate - " + str(self.getStartDate()))
		print("seasonLength - " + str(self.getSeasonLength()))
		print("endDate - " + str(self.getEndDate()))
		print("harvestDate - " + str(self.getHarvestDate()))
		print("precipitationNeeded - " + str(self.getPrecipitationNeeded()))
		print("precipitationSinceStart - " + str(self.getPrecipitationSinceStart()))
		print("precipitationPerDay - " + str(self.getPrecipitationPerDay()))

	def setStartDate(self, x):
		self.startDate = int(x)
		self.plantDate = int(x) - 1
	def setEndDate(self, x):
		self.endDate = int(x)
		self.harvestDate = int(x) + 1

	def setPrecipitationNeeded(self, x):
		self.precipitationNeeded = x
		self.seasonLength = self.endDate - self.startDate
		self.precipitationPerDay = format(self.precipitationNeeded / self.seasonLength, ".2f")
	def setPrecipitationSinceStart(self, x):
		self.precipitationSinceStart = self.precipitationSinceStart + float(x)

#converts (month, day) to day of year
#for calculating start and end dates for crops consistently
def convertCalendarToDay(month, day):
	daysFromMonth = 0
	if month == 1:
		daysFromMonth = 0
	elif month == 2:
		daysFromMonth = 31
	elif month == 3:
		daysFromMonth = 59
	elif month == 4:
		daysFromMonth = 90
	elif month == 5:
		daysFromMonth = 120
	elif month == 6:
		daysFromMonth = 151
	elif month == 7:
		daysFromMonth = 181
	elif month == 8:
		daysFromMonth = 212
	elif month == 9:
		daysFromMonth = 243
	elif month == 10:
		daysFromMonth = 273
	elif month == 11:
		daysFromMonth = 304
	elif month == 12:
		daysFromMonth = 334
	return int(daysFromMonth + day)

def generateRainFall():
	possibleRain = [0, 0, 0, 0, 0, 0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.3]
	return possibleRain[random.randint(0, len(possibleRain) - 1)]

asparagus = CROP()
potatoes = CROP()
tomatoes = CROP()
sugarSnapPeas = CROP()
spinach = CROP()
soyBeans = CROP()

crops = []

def determineInSeason(array, x):
	placeholder = []
	for i in array:
		if i.getStartDate() >= x and i.getEndDate() <= x:
				placeholder.append(i)
	return placeholder

##### PRE-LOOP SETUP #####

asparagus.setName("ASPARAGUS")
asparagus.setStartDate(convertCalendarToDay(4, 1))
asparagus.setEndDate(convertCalendarToDay(6, 10))
asparagus.setPrecipitationNeeded(4.32)
crops.append(asparagus)

potatoes.setName("POTATOES")
potatoes.setStartDate(convertCalendarToDay(3, 30))
potatoes.setEndDate(convertCalendarToDay(10, 1))
potatoes.setPrecipitationNeeded(12.01)
crops.append(potatoes)

tomatoes.setName("TOMATOES")
tomatoes.setStartDate(convertCalendarToDay(5, 1))
tomatoes.setEndDate(convertCalendarToDay(9, 30))
tomatoes.setPrecipitationNeeded(11.04)
crops.append(tomatoes)

sugarSnapPeas.setName("SUGAR SNAP PEAS")
sugarSnapPeas.setStartDate(convertCalendarToDay(4, 10))
sugarSnapPeas.setEndDate(convertCalendarToDay(9, 10))
sugarSnapPeas.setPrecipitationNeeded(2.81)
crops.append(sugarSnapPeas)

spinach.setName("SPINACH")
spinach.setStartDate(convertCalendarToDay(3, 30))
spinach.setEndDate(convertCalendarToDay(5, 30))
spinach.setPrecipitationNeeded(1.47)
crops.append(spinach)

soyBeans.setName("SOY BEANS")
soyBeans.setStartDate(convertCalendarToDay(5, 30))
soyBeans.setEndDate(convertCalendarToDay(11, 10))
soyBeans.setPrecipitationNeeded(7.67)
crops.append(soyBeans)

currentDay = 0
farmingTime = True
firstDayOfFarming = crops[0].getStartDate()
for i in crops:
	if i.getPlantDate() <= firstDayOfFarming:
		firstDayOfFarming = i.getPlantDate()
lastDayOfFarming = crops[0].getHarvestDate()
for i in crops:
	if i.getHarvestDate() >= lastDayOfFarming:
		lastDayOfFarming = i.getHarvestDate()

print("Your current season is from day number " + str(firstDayOfFarming) + " to day number " + str(lastDayOfFarming) + ".")
print("The current day is day number " + str(currentDay) + ".")
input("Press enter to advance to the first day of the season, or " + str(firstDayOfFarming) + ".")
currentDay = firstDayOfFarming
print(" ")
print("Today is day number " + str(currentDay) + ".")
print("Today you need to plant:")
for i in crops:
	if i.getPlantDate() == currentDay:
		print(i.getName())
input("Press enter to advance to the next day.")
currentDay += 1
print("")

##### MAIN LOOP #####

while farmingTime:
	print("Today is day number " + str(currentDay) + ".")
	rainfallLastNight = generateRainFall()
	print("Last night you got " + str(rainfallLastNight) + " inches of rain.")
	print("Today you need to water")
	cropsInSeason = []
	for i in crops:
		if i.getStartDate() <= currentDay and i.getEndDate() >= currentDay:
				cropsInSeason.append(i)

	for i in cropsInSeason:
		print(i.getName())
	currentDay += 1
	input("")
	if currentDay > lastDayOfFarming:
		farmingTime = False

##### POST LOOP #####

print("Today it is day number " + str(currentDay) + " and it is now out of season.")

##### NOTES #####

# pre-loop:
# i. create all crops
# ii. setStartDate, setEndDate
# iii. setPrecipitationNeeded
# iv. find first day to plant and last day to harvest
# v. ask to advance to first day to plant those crops
# vi. advance to that day
# vii. print that day and to plant those crops
# viii. advance to next day
# ix. start loop

# in loop: (while day less than last harvest date)
# 1. Print which day it is
# 2. Generate rain number from previous night
# 3. Check which crops are in season
# 4. Add rain to those crops
# 5. Find difference between actual rain and needed rain of those crops
# 6. Check which crops to plant
# 7. Check which crops to harvest
# 8. Press enter to advance day

#CURRENTLY - FIX FLOATING POINT