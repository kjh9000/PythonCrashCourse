#!/usr/bin/python3

''' An administrator is a special kind of user Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171) Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on
Write a method called show_privileges() that lists the administrator’s set of
privileges Create an instance of Admin, and call your method
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

class Admin(User):
    def __init__(self, name, age, occupation):
        super().__init__(name, age, occupation)
        self.priviledges = ['add', 'ban', 'delete']

    def show_priviledges(self):
        print(self.name.title() + " is an admin and has the following priviledges:")
        for i in self.priviledges:
            print("-" + i)

bob = Admin('bob', 100, 'admin')
bob.show_priviledges()

