#!/usr/bin/python3

""" write a program that asks the user what kind of rental car they want. print
a message about the car, such as 'Let me see if we have a suburu'
"""

rental = input("What kind of car would you like to rent? ")
print("Let me see if we have a " + rental.title() + ".")
