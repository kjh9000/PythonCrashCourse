#!/usr/bin/python3

"""write a loop that prompts the user to enter pizza toppings until they enter 'quit'. as they enter each topping, print a message say you'll add that topping
"""

while True:
    topping = input("What topping would you like to add? ")
    if topping == 'quit':
        break
    else:
        print("Adding " + topping + ".")
