""" this is the module to be imported in exercise 9-10"""

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()  
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant " + self.restaurant_name + " serves " + 
        self.cuisine_type + " food.")

    def open_restaurant(self):
        print("The restaurant " + self.restaurant_name + " is open.")
