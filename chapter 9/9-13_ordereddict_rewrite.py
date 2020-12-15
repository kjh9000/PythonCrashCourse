#!/usr/bin/python3

""" Start with Exercise 6-4 (page 108), where you
used a standard dictionary to represent a glossary Rewrite the program using
the OrderedDict class and make sure the order of the output matches the order
in which key-value pairs were added to the dictionary """

from collections import OrderedDict

glossary = OrderedDict()

glossary['print'] = 'Prints text out.',
glossary['for'] = 'Used to start for loops.',
glossary['list'] = 'Another word for indexed array in Python. Mutable.',
glossary['tuple'] = 'An immutable list.',
glossary['dictionary'] = 'Another word for associative array. Mutable.',


for k, v in glossary.items():
    print(k + ':',v)
