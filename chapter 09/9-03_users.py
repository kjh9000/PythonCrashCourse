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
    def __init__(self, first_name, last_name, age, occupation):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.occupation = occupation

    def describe_user(self):
        print("User " + self.first_name + " " + self.last_name + " is " + str(self.age) + " years" +
        " old, and lists his/her occupations as " + self.occupation + ".")

    def greet_user(self):
        print("Hello, " + self.first_name +" " + self.last_name + ".")

bob = User('bob', 'smith', 105, 'programmer')
alice = User('alice', 'smith', 30, 'database admin')

bob.greet_user()
bob.describe_user()
alice.greet_user()
alice.describe_user()
