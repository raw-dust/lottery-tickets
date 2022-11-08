## This will generate random lottery tickets for any draw game
## It will choose numbers from two different groups of numbers
## For games like Powerball and Mega Millions the first group would be the
##  white balls and the second group would be the Powerball/Meagball
## For games like Lottery, which only have one group of numbers, set the balls
##  drawn to zero

import random

groupOneBalls = 69
groupOneBallsDrawn = 5
groupTwoBalls = 26
groupTwoBallsDrawn = 1

tickets = 5

for x in range(tickets):
    white= range(1,groupOneBalls+1)
    mega = range(1, groupTwoBalls+1)
    balls= random.sample(white,groupOneBallsDrawn)
    mega= random.sample(mega,groupTwoBallsDrawn)
    balls.sort()
    mega.sort()
    print(str(balls)+" "+str(mega))

