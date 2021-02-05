#!/usr/bin/python3

""" make a dict called cities. use the name of three cities as keys, and details
such as name, country, population, and one unique fact about the city as values.
loop through and print everything out
"""

cities = {
    'las vegas': ['usa', 1000000,'gambling'],
    'san francisco':['usa', 1000000, 'frisco burger'],
    'new york': ['usa', 1000000, 'carnagie hall']
    }

for k,v in cities.items():
    print(k.title() + " is located in the country of " + v[0].title() + 
    ". It has a population of " + str(v[1]) + ", and is known for its " +  
    v[2].title() + ".")
