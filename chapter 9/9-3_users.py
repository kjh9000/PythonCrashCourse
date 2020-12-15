#!/usr/bin/python3

'''  Make a class called User Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile Make a method called describe_user() that prints a summary
of the user’s information Make another method called greet_user() that prints
a personalized greeting to the user
Create several instances representing different users, and call both methods
for each user
'''

class User():
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def describe_user(self):
        print("User " + self.name.title() + " is " + str(self.age) + " years" +
        " old, and lists his/her occupations as " + self.occupation + ".")

    def greet_user(self):
        print("Hello, " + self.name.title())

bob = User('bob', 105, 'programmer')
bob.greet_user()
bob.describe_user()

alice = User('alice', 30, 'database admin')
alice.greet_user()
alice.describe_user()
