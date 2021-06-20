#Who's Your Daddy
#Demonstrates male name and their father and grandfather

sondad = {"Darren Guzman": "Evelio Guzman", "Ramon Dario Morales": "Ramon Morales Higuera", "Conor Jack McGregor Jr.": "Conor Anthony McGregor"}

choice = None
while choice != "0":

    print(
    """
    Who's Your Daddy?!
    
    0 - Quit
    1 - Look Up Pair
    2 - Add a Pair
    3 - Replace a Pair
    4 - Delete a Pair
    
    """
    )

    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Good-bye.")

    # look up pair
    elif choice == "1":
        choice = input("Which pair do you want to look up?: ")
        if choice in sondad:
            dad = sondad[choice]
            print("\n", choice,"is son to:", dad)
        else:
            print("\nSorry, I don't know", choice)

    # add a father
    elif choice == "2":
        choice = input("Who is the son you want to add?: ")
        if choice not in sondad:
            dad = input("\nWho's the father?: ")
            sondad[choice] = dad
            print("\n", dad, "has been added.")
        else:
            print("\nThat pair already exists!  Try replacing them.")

    # replace a father
    elif choice == "3":
        choice = input("Which son do you want to replace a father?: ")
        if choice in sondad:
            dad = input("Who's the father?: ")
            sondad[choice] = dad
            print("\n", choice, "has been replaced.")
        else:
            print("\nThey don't exist! Try adding them.")
       
    # delete a pair
    elif choice == "4":
        choice = input("Which pair do you want to delete?: ")
        if choice in sondad:
            del sondad[choice]
            print("\nOkay, I deleted", choice)
        else:
            print("\nI can't do that!", choice, "don't exist.")
                   
    # some unknown choice
    else:
        print("\nSorry, but", choice, "isn't a valid choice.")
  
input("\n\nPress the enter key to exit.")
    

