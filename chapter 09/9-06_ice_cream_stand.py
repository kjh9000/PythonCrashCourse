#!/usr/bin/python3

'''Ice Cream Stand: An ice cream stand is a specific kind of restaurant Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171) Either version of
the class will work; just pick the one you like better Add an attribute called
flavors that stores a list of ice cream flavors Write a method that displays
these flavors Create an instance of IceCreamStand, and call this method
'''

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()  
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant " + self.restaurant_name + " serves " + 
        self.cuisine_type + " food.")

    def open_restaurant(self):
        print("The restaurant " + self.restaurant_name + " is open.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'strawberry']

    def display_flavors(self):
        print("The ice cream stand has the following flavors available:")
        for i in self.flavors:
            print("-" + i)

baskinrobbins = IceCreamStand('baskin robbins', 'ice cream')
baskinrobbins.display_flavors()
