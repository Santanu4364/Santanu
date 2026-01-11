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