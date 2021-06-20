#Car Salesman
#Demonstrates base price of car with fees (tax, license, dealer prep,
#destination charge.
#Tax and license is a percent of base price, other values are set


carbaseprice = int(input("Car Base Price: $ "))
                

taxfee = carbaseprice * .15
print("\nTax Fee: $", taxfee)
licensefee = carbaseprice * .11
print("\nLicense Fee: $", licensefee)
dealerprepfee = 350
print("\nDealer Prep Fee: $", dealerprepfee)
destinationchargefee = 400
print("\nDestination Charge Fee: $", destinationchargefee)
actualprice = carbaseprice + taxfee + licensefee + dealerprepfee + destinationchargefee
print("\nActual price with fees: $ ", actualprice)

input("\n\nPress the enter key to exit.")
