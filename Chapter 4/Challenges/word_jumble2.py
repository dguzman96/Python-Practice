#Word Jumble 2.0
#each word is paired with a hint, seen when stuck
#scoring system rewards players for those who solve without hint

import random

#create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

#pick one word randomly from the sequence
word = random.choice(WORDS)

#create a variable to use later to see if the guess is correct
correct = word

#create a jumbled version of the word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

#set score
score = 0

#start the game
print(
"""
        Welcome to Word Jumble!

  Unscramble the letters to make a word.
Enter a guess, an X to give up, or type ? and press enter for a hint.
(Press the enter key at the prompt to quit)

Try to ge the lowest score possible. For each hint, you gain a point.
See if you can win with no points!!
"""

)
print("The jumble id:", jumble)

lst = range(len(jumble))
hint = '_' * len(jumble)
while True:
    guess = input("Guess or '?' or 'X': ").lower()
    if guess == correct:
        print("That's it! You guessed it! Your score is", score)
        break
    elif guess == '?':
        i = random.choice(lst)
        print(correct[i], "is the", i + 1, "letter.")
        score += 1
    elif guess == 'x':
        print("Sorry you gave up!")
        break
    else:
        print("Sorry, that's not it.")

print("Thanks for playing.")

input("\n\nPress the enter key to exit.")
