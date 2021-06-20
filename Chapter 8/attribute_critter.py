#Attribute Critter
#Demonstrates creating and accessing attributes

class Critter(object):
    """A virtual pet"""
    def __init__(self):
        print("A new critter has been born!")
        self.name = name

    def __str__(self):
        rep = "Critter object\n"
        rep += "name: " + self.name + "\n"
        return rep
    
    def talk(self):
        print("\nHi. I'm an instance of a class Critter.")

#main
crit1 = Critter("Poochie")
crit1.talk() 

crit2 = Critter("Randolph")
crit2.talk() 

print("Printing crit1")
print(crit1)

print("Directly accessing crit1.name:")
print(crit1.name)

input("\n\nPress the enter key to exit.")
