#Guess My Number- Limited
#The player guesses a number between 1 and 100
#and has 10 of guesses
#If the player fails to guess in time, message displayed

import random

print("\tWelcome to 'Guess My Number-Limted'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in 10 attempts.\n")

#set the initial values
the_number = random.randint(1,100)
guess = int(input("Take a guess: "))
tries = 1

#guessing loop
while guess != the_number:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")

    guess = int(input("Take a guess: "))
    tries += 1
    if tries == 10:
        break

print("You guessed it! The number was", the_number)
print("And it only took you", tries, "tries!\n")

input("\n\nPress the enter key to exit.")
