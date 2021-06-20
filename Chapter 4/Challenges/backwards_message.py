#Backwards
#User enters a message and returned backwards

print("Backwards:")
message = input("Enter a message: ")

backwardmsg = ""

while message:
    reverseltr = (len(message) - 1)
    backwardmsg += message[reverseltr]
    message = message[:reverseltr]

print("Your message backwards is: ", end = "")
print(backwardmsg)

input("\n\nPress the enter key to exit.")

    
