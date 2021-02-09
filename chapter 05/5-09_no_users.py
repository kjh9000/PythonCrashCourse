#!/usr/bin/python3

"""add an if statement to test if the usernames list is empty. if empty, print
out a message 'We need to find some users!'. test on an empty list
"""

usernames = []#'admin', 'bob', 'alice', 'heckyl', 'jeckyl']
if usernames:
    for i in usernames:
        if i == 'admin':
            print('Hello, admin. Would you like to see a status report?')
        else:
            print('Hello,', i.title()+ '. Thanks for logging on.')
else:
    print("We need to find some users!")
