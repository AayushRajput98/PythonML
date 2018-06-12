import random
def roll_dice(side,dice):
    for i in range(0,dice):
        print(random.randint(0,side))
side=int(input("Enter the number of sides"))
dice=int(input("Enter the number of rolls in a dice"))
roll_dice(side,dice)