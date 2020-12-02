#!/usr/bin/python3

"""a movie theater chages different prices depending on age of the patron.
write a program to inform user of ticket price. if:
under 3 = free
between 3 and 12 = $10
over 12 = $15
"""

age = int(input("How old is the movie goer? "))
if age < 3:
    print("Admission is free.")
elif age <= 12:
    print("The ticket costs $10.")
else:
    print("The ticket costs $15.")
