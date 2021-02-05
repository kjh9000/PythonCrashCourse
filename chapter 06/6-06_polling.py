#!/usr/bin/python3

"""using the code from favorite)languages, make a list of people who may or
may not have taken the poll. if theyve taken it, print a message thanking them.
if they havent taken the poll print a message inviting them to do so
"""

people = ['bob', 'alice', 'phil']
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for i in people:
    if i in favorite_languages:
        print('Hey there,',i.title() + '! Thanks for taking our poll!')
    else:
        print('Hey there,',i.title() + '! You are invited to take out poll!')
