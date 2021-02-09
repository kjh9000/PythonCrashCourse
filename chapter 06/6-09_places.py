#!/usr/bin/python3

""" make a dict called favorite_places. think of three people's names to use as
keys, and places as values.  print each name and place out
"""

places = {'larry': 'switzerland', 'curly': 'beruit', 'moe': 'england'}

for k, v in places.items():
    print(k.title() + "'s favorite place is " + v.title() + ".")
