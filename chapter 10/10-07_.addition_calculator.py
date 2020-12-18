#!/usr/bin/python3

""" Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers even if they make a mistake and
enter text instead of a number """


""" note- trying to convert a string into an int results in a ValueError. i simply cannot replicate a TypeError for this exercise so im going to chock this up to a mistake in the book """

while True:
    print("Give me two numbers and I'll add them together.")
    num1 = input("Give me a number: ")
    num2 = input("Give me another number: ")
    try:
        sum = int(num1) + int(num2)
    except ValueError:
        print("Must be two digits")
    else:
        print(sum)
