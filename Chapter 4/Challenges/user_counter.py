#Counter
#User enters starting number, ending number and amount to count

print("Counter:")
startnum = int(input("Enter the starting number: "))
endnum = int(input("Enter the ending number: "))
amount = int(input("Enter the amount to count by: "))

for i in range (startnum, endnum, amount):
    print (i, end = " ")

input("\n\nPress the enter key to exit.")
