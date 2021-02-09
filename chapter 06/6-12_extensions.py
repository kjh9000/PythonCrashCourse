#!/usr/bin/python3

""" use an example program from this chapter. extend it by adding new keys and
values, chanigng the context, or improving the formatting the output

"""

glossary = {
    'print': 'Prints text out.',
    'for': 'Used to start for loops.',
    'list': 'Another word for indexed array in Python. Mutable.',
    'tuple': 'An immutable list.',
    'dictionary': 'Another word for associative array. Mutable.',
    }

for k, v in glossary.items():
    print("The entry '" + k + "' has the following entry:\n" + v + '\n')
