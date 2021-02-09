#!/usr/bin/python3

""" modify exercise 6-2 so each person has more than one favorite number. loop
through the dict and print each person's name and numbers
"""

people = {'larry': [4, 11], 'curly': [12, 41], 'moe': [12, 11], 'bob': [1, 33], 'alice': [55, 12]}

for k, v in people.items():
    print(k.title() + "'s favorite number are " + str(v))
