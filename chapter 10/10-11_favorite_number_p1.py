#!/usr/bin/python3

"""Write a program that prompts for the user’s favorite number Use json.dump() 
to store this number in a file Write a separate program that reads in this
value and prints the message, “I know your favorite number! It’s _____ ”"""

import json

with open('fav_number.json', 'w') as fo:
    fav_number = input("What is your favorite number? ")
    json.dump(fav_number, fo)
    print("We will remember your favorite number, " + fav_number + ".")
