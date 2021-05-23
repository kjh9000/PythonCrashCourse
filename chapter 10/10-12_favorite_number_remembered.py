#!/usr/bin/python3

""" Combine the two programs from
Exercise 10-11 into one file If the number is already stored, report the favorite
number to the user If not, prompt for the user’s favorite number and store it in a
file Run the program twice to see that it works """

import json

try:
    with open('fav_number.json') as fo:
        print("I know your favorite number! It's " + json.load(fo) + ".")
except (ValueError, FileNotFoundError):
    with open('fav_number.json', 'w') as fo:
        fav_number = input("What is your favorite number? ")
        json.dump(fav_number, fo)
        print("We will remember your favorite number, " + fav_number + ".")
