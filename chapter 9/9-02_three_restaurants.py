#!/usr/bin/python3

''' Three Restaurants: Start with your class from Exercise 9-1 Create three
different instances from the class, and call describe_restaurant() for each
instance
'''

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name  
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant " + self.restaurant_name.title() + " serves " + 
        self.cuisine_type + " food.")

    def open_restaurant(self):
        print("The restaurant " + self.restaurant_name.title() + " is open.")

restaurant = Restaurant('my restaurant', 'american')
restaurant2 = Restaurant('my german restaurant', 'german')
restaurant3 = Restaurant('my mexican restaurant', 'mexican')

restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
