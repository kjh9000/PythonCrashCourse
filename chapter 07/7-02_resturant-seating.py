#!/usr/bin/python3

""" write a program that asks the user how many people in their dinner group.
if there are more than eight people, print a message stating they have to wait
for a table. otherwise print a message stating their table uis ready
"""

party = int(input("How many people in your party? "))

if party > 8:
    print("Sorry. A table for a party of your size is unavailable. Would you " +
     "like to wait for a table?")
else:
    print("Your table is ready.")
    
