#!/usr/bin/python3

'''   Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166) Write a method called increment_
login_attempts() that increments the value of login_attempts by 1 Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0
Make an instance of the User class and call increment_login_attempts()
several times Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts() Print login_attempts again to
make sure it was reset to 0
'''

class User():
    def __init__(self, first_name, last_name, age, occupation, login_attempts):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.occupation = occupation
        self.login_attempts = login_attempts

    def describe_user(self):
        print("User " + self.first_name + " " + self.last_name + " is " +
        str(self.age) + " years" +
        " old, and lists his/her occupations as " + self.occupation + ".")

    def greet_user(self):
        print("Hello, " + self.first_name +" " + self.last_name + ".")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

bob = User('bob', 'smith', 105, 'programmer', 0)
bob.increment_login_attempts()
bob.increment_login_attempts()
bob.increment_login_attempts()
bob.increment_login_attempts()
bob.increment_login_attempts()
print(bob.login_attempts)
bob.reset_login_attempts()
print(bob.login_attempts)
