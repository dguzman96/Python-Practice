#Coin Flip
#Demonstrates a coin being flipped 100 times
#and tells you the number of heads and tails

import random

print("Coin Flip\n")

heads = 0
tails = 0
count = 0

while count < 100:
    coin = random.randrange(2)
    if coin == 0:
        heads = heads + 1
    else:
        tails = tails + 1
    count += 1
print("Number of heads: ", heads)
print("Number of tails: ", tails)

input("\n\nPress the enter key to exit.")

