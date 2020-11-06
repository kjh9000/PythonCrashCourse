#!/usr/bin/python3

"""make a list of five or more users called current_users. make another list of five called new_users. loop though the new_users to see if each new user is in 
the current_users list. make sure case doesnt affect comparison. if not unique,
print a message stating the user needs to choose a different name.
"""

current_users = ['bob', 'alice', 'larry', 'curly', 'moe']
new_users = ['heckyl', ' Moe', 'BOB', 'shemp', 'alice']

for i in new_users:
    if i.lower() in current_users:
        print('Sorry, but the name ', i, ' is taken. Please choose a different name.')
