#!/usr/bin/python3

'''write a function that stores info about a car in a dict. the function should
always recieve an manufacturer and model. it should then accept an arbitrary
number of keyword arguments call the fucntion with the required into and two
name-value pairs.
'''

def car(make, model, year, **other):
    details = {}
    details['make'] = make
    details['model'] = model
    details['year'] = year
    for k, v in other.items():
        details[k] = v
    return details
print(car('suburu', 'outback', 2010, color='blue', towpackage=True))
