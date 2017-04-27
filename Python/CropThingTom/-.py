First possible Project for Cracking the Code:

1) Farmer Brown wants to plant the following:

Season: March 30 - November 10
Area: 25 Acres

 CROP              INCHES OF RAIN        SEASON                AREA (Acres)
  Asparugus              4.32             apr 1 - jun 10          4
  Potatoes              12.01             mar 30 - 1 oct          2
  Tomotoes              11.04             1 may - 30 sept         4
  Sugar Snap Peas        2.81             10 apr - 10 sept        6
  Spinach                1.47             30 mar - 30 may         9
  Soy Bean               7.67             30 may - 10 nov         5


These are the standards for these crops. In other words - in order to
grow asparagus, 4.32 inches of rain has to fall between apr 1 - jun 10.
If only 2 inches falls, the farmer needs to irrigate the asparagus 2.32
inches worth of water.

If we divided the 4.32 inches into days 71 days, it comes out .06 inches / day.
Note: 71 = end_date - start_date

The problem:
Farmer Brown only has one water irrigation truck for all his crops.
But his mom might buy him another one. That would be cool.

With only one truck, he wants to know:
which crops he needs to water,
on which days,
depending on the accumulated rainfall so far for the season

The program should run like this:
>>>> python getRainfall.py
>>>> How many inches of rain has fallen since ... ?
>>>> You need to water as follows (April 10):
         Asparugus:        0
         Potatoes:         .033 inches
         Tomatoes:         0
         Sugar Snap Peas:  .0001 inch
         Spinach:          .002 inch
         Soy Beans:        0

** extra: **
and how much water he needs to put into his truck each day.
to do this, you need the following data:

 1 inch of rain on 1 acre of land = 27,154 gallons, and
  1 acre = 43,560 square feet
  also, irrigation is about 60% as efficient as rain!
  in other words, 1" of rain on 1 acre = 1.67 * 27,154 = 45,347.18 gallons!
  also, a truck only holds 11,600 gallons.

Continuing with asparagus:
4 acres need .06 inches / day => 4 * 1,629.24 = 6516 gallons / day
But, remember, we need to account for 60% efficiency - so we need 10860 gallons
** end extra **

Following is how I would do this. If you want to look - fine. Otherwise,
figure it out and then look - or however you want to use it:

1) Dictionary: crop -> rainfall
2) Dictionary: crop -> start date
3) Dictionary: crop -> end date

 Note: this could be a dictionary of arrays: {crop: [rainfall, start, end]}

function: calcNumberDays(crop)
function: calcDailyNeeds(crop)
function: calcNeeded(date,rainFallen,crop)


***********************************************************************
Second possible project:
The year 2012 could be considered two sides of a right triangle: 20 & 12 -
because (20 * 20) = (12 * 12) + (16 * 16) (Pythagoras)

Write a program to accept 2 ints, and determine:
 1) are they 2 sides of a right triangle?
 2) what is the third side (if they are)

The program should opperate like this:

>>>>> python twoSides.py
>>>>> Enter two sides: 20 12
>>>>> These are two sides of a right triangle. The third side is 16.
>>>>> Enter two sides: 20 14
>>>>> These are NOT two sides of a right triangle.