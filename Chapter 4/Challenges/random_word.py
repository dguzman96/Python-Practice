#Random Word
#Computer picks a random word
#Player has to guess
#Computer tells player how many letters are in the word
#Player gets 5 chances
#Computer can only respond yes or no

import random

tries = 0

print("Random Word")
print("Guess my word by guessing the letters first")

#create a sequence of words to choose from
WORDS = ("soccer", "red", "running", "programmer", "chivas", "snapple")

word = random.choice(WORDS)

correct = word
length = len(word)
length = str(length)

while tries <5:
    guess = input("The word is " + length + " letters long. Guess a letter!: ")
    if guess not in word:
        print("No")
    else:
        print("Yes")
    tries = tries + 1
            
if tries == 5:
    final = input("Try to guess the word: ")
    if final == correct:
        print("Correct! You guessed it!")
    else:
        print("Sorry. My word was ", word)

input("\n\nPress enter to exit")
