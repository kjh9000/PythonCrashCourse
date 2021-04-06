""" module for exercise 9-12 """

from user_mod import User

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

