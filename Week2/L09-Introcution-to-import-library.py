import math
print(math.log(10))  # prints the logarithm of 100
print(math.sqrt(25))
print(math.cos(45))

#lets simulate the toos of a coin
import random
coin = random.random()
if coin<0.5:
    print("Heads")
else:
    print("Tails")

#lets simulate a dice roll 6 sided dice
dice = random.randrange(1,7)
print(dice)
#sumation of two dice
dice1=random.randrange(1,7)
dice2=random.randrange(1,7)
print(dice1+dice2)
