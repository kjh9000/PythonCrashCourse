""" users module for exercise 9-12 """

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
