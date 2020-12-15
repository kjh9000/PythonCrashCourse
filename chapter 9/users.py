"""module for exercise 9-11 """

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
        self.priviledges = Priviledges()

class Priviledges():
    def __init__(self):
        self.priviledges = ['add', 'ban', 'delete']

    def show_priviledges(self):
        print("Admin has the following priviledges:")
        for i in self.priviledges:
            print("-" + i)

