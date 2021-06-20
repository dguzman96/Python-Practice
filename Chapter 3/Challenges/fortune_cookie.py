#Fortune Cookie
#Demonstrates one of five fortunes, at random

import random

print("Fortune Cookie!")

fortune = random.randint(1,5)

if fortune == 1:
    print("You will be rich!")
elif fortune == 2:
    print("You will be happy for life!")
elif fortune == 3:
    print("You will be have your dream car in 10 days!")
elif fortune == 4:
    print("You will be bankrupt within 2 years!")
else:
    print("You will not much live longer!")

input("\n\nPress the enter key to exit.")
