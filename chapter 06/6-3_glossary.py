#!/usr/bin/python3

"""use a dict to store five programming words as keys, and their meaninings
as values. print each entry formatted. after the key use a colon, and insert a
new line between each word-meaning pair
"""

glossary = {
    'print': 'Prints text out.',
    'for': 'Used to start for loops.',
    'list': 'Another word for indexed array in Python. Mutable.',
    'tuple': 'An immutable list.',
    'dictionary': 'Another word for associative array. Mutable.',
    }

print('print:', glossary['print'] + '\n')
print('for:', glossary['for']  + '\n')
print('list:', glossary['list'] + '\n')
print('tuple:', glossary['tuple']+ '\n')

print('dictionary:', glossary['dictionary'] + '\n')
