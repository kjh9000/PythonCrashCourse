#!/usr/bin/python3

"""write different versions of exercise 7-4. make sure to do each of the following at least once:
use a conditional test to stop a while loop
use an active variable to control how long the loop runs
use a break statement to exit the loop when the user enters 'quit'
"""

active = True
while active: # active variable
    topping = input("What topping would you like to add? ")
    if topping == 'quit': #conditional
        active = False
    else:
        print("Adding " + topping + ".")

"""
#version 3 break statement
while True:
    topping = input("What topping would you like to add? ")
    if topping == 'quit':
        break #break statement
    else:
        print("Adding " + topping + ".")
"""
