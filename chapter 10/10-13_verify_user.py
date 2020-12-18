#!/usr/bin/python3

""" Verify User: The final listing for remember_me.py assumes either that the
user has already entered their username or that the program is running for the
first time We should modify it in case the current user is not the person who
last used the program
Before printing a welcome back message in greet_user(), ask the user if
this is the correct username If it’s not, call get_new_username() to get the correct
username """

import json

filename = 'username.json'

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    print(username)
    name = input("Is this you? (y/n) ")
    if name == 'y':
        print("Welcome back, " + username + "!")
    else:
        get_new_username()

greet_user()
