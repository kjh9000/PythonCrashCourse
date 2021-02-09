#!/usr/bin/python3

"""store numbers 1-9 in a list, and loop through.each number should be changed to its ordinal counterpart.
"""

numbers = list(range(10))

for i in numbers:
    if i == 1:
        print('1st')
    if i == 2:
        print('2nd')
    if i == 3:
        print('3rd')
    if i >= 4:
        print(str(i) + 'th')
