#!/usr/bin/python3
'''Start with your program from Exercise 9-1 (page 166) Add an 
attribute called number_served with a default value of 0 Create an 
instance called restaurant from this class Print the number of customers
the restaurant has served, and then change this value and print it again
Add a method called set_number_served() that lets you set the number of
customers that have been served Call this method with a new number and print 
the value again Add a method called increment_number_served() that lets you
increment the number of customers who’ve been served Call this method with
any number you like that could represent how many customers were served in
a day of business
'''

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name  
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def decribe_restaurant(self):
        print("The restaurant " + self.restaurant_name.title() + " serves " + 
        self.cuisine_type + " food.")

    def open_restaurant(self):
        print("The restaurant " + self.restaurant_name.title() + " is open.")

    def set_number_served(self):
        return self.number_served

    def increment_number(self, inc):
        return number_serverd *= inc

my_resturant = Resturant('my resturant', 'fast food')
my_resturant.set_number_served(1000)
print(number_served)
my_resturant.increment_number(500)
print(number_served)


