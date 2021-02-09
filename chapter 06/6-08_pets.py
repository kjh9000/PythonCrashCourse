#!/usr/bin/python3

""" make several dicts. each name is of a pet. store info about the owner, name,
and species of animal. store the dicts in a list called pets. loop through and
print out the details.
"""

roland = {
    'name': 'roland',
    'species': 'cat', 
    'owner':'me'
    }

mathilda = {
    'name': 'mathilda',
    'species': 'cat',
    'owner':'me'
    }

boots = {
    'name': 'boots',
    'species':'dog',
    'owner': 'chris'
    }

pets = [roland, mathilda, boots]

for i in pets:
   print(i['name'].title() + " is a "+ i['species'] + " owned by " + i['owner'].title() + ".")

