#Guess My Number- Limited
#The player guesses a number between 1 and 100
#and has 10 of guesses
#If the player fails to guess in time, message displayed

import random

GUESS_LIMIT = 5


print("\tWelcome to 'Guess My Number-Limted'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in 10 attempts.\n")

# functions
def display_instruct():
    """Display game instructions."""
    print("\tWelcome to 'Guess My Number'!")
    print("\nI'm thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible.")
    print("\nHARDCORE mode - You have 5 tries to guess the number!\n")


def ask_number(question, low, high, step = 1):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high, step):
        response = int(input(question))
    return response


def guessing_loop():
    the_number = random.randint(1, 100)
    guess = ask_number("\nTake a guess:", 1, 100)
    tries = 1

    while guess != the_number or tries != GUESS_LIMIT:
        if guess > the_number:
            print("Lower...")
        else:
            print("Higher...")

        guess = ask_number("Take a guess:", 1, 100)
        tries += 1

    if tries == GUESS_LIMIT:
        print("\nOh no! You have run out of tries!")
        print("Better luck next time!")
    else:
        print("\nYou guessed it! The number was", the_number)
        print("And it only took you", tries, "tries!")


def main():
    display_instruct()
    guessing_loop()


# start the program
main()
input("\n\nPress the enter key to exit")
