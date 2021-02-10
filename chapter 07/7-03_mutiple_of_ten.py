#!/usr/bin/python3

""" ask the user for a number, then report whether the number is a multiple of 10
"""

number = input("Enter a number: ")

if int(number) %10 == 0:
    print(number + " is a multiple of 10.")
else:
    print(number + " is not a multiple of 10.")
