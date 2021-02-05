#!/usr/bin/python3

"""store favorite numbers of people in a dict. use five names as keys, and a
number for each person. print out each person and number
"""

people = {'larry': 4, 'curly': 12, 'moe': 11, 'bob': 1, 'alice': 55}

for k, v in people.items():
    print(k.title() + "'s favorite number is", v)
