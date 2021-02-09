#!/usr/bin/python3

"""using the code from 6-1, make two new dicts representing different people.
store all three dicts in a list called people. loop through the list, printing
out thje details about each person
"""

person1 = {
    'first_name': 'mike',
    'last_name': 'johnson',
    'city': 'las vegas'
    }

person2 = {
    'first_name': 'heckyl',
    'last_name': 'the bird',
    'city': 'seattle'
    }

person3 = {
    'first_name': 'jeckyl',
    'last_name': 'the bird',
    'city': 'los angeles'
    }

people = [person1, person2, person3] # if you iterate and try people[0], it will
# return the dict not the name of it.

for i in people:
   print(i['first_name'].title() + " " + i['last_name'].title() + 
   " lives in the city of " + i['city'].title() + ".")
