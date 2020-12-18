#!/usr/bin/python3

""" Addition: One common problem when prompting for numerical input
occurs when people provide text instead of numbers When you try to convert
the input to an int, you’ll get a TypeError Write a program that prompts for
two numbers Add them together and print the result Catch the TypeError if
either input value is not a number, and print a friendly error message Test your
program by entering two numbers and then by entering some text instead of a
number """


""" note- trying to convert a string into an int results in a ValueError. i simply cannot replicate a TypeError for this exercise so im going to chock this up to a mistake in the book """

print("Give me two numbers and I'll add them together.")
num1 = input("Give me a number: ")
num2 = input("Give me another number: ")
try:
    sum = int(num1) + int(num2)
except ValueError:
    print("Must be two digits")
else:
    print(sum)
