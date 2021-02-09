#!/usr/bin/python3

"""make a list of five or more usernames, one called 'admin'. loop through the list and print a greeting. if the user is admin. print something like 'hello
admin. would you like to see a status report?' otherwise print a generic hello greeting
"""

usernames = ['admin', 'bob', 'alice', 'heckyl', 'jeckyl']
for i in usernames:
    if i == 'admin':
        print('Hello, admin. Would you like to see a status report?')
    else:
        print('Hello,', i.title() + '. Thanks for logging on.')
