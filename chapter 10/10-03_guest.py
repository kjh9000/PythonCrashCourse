#!/usr/bin/python3

"""Write a program that prompts the user for their name When they
respond, write their name to a file called guest.txt """

name = input("What name do you want to add to the guest list? ")
with open('guests.txt', 'a') as fo:
    fo.write(name)
    fo.write("\n")
