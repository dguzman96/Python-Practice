# Random Word List
#Demonstrates list of words in random order

import random

myList = ["Hello", "Name", "Color", "Today", "Never"]

for i in range(len(myList)):
    randomWord = random.choice(myList)
    print(randomWord)
    myList.remove(randomWord)

input("\n\nPress the enter key to exit.")
