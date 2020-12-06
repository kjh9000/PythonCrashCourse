#!/usr/bin/python3

''' write a function called describe_city() that accepts the name of the city
and country its in. the function should print a simple sentence remarking the
city and country. give the parameter for the country a default value. call the
function for three different cities, at least one of which isnt in the default country
'''

def describe_city(city, country='usa'):
    print("The city of " + city.title() + " is located in the country " + country.title() + ".")

describe_city('san francisco')
describe_city('new york')
describe_city('perth', 'australia')
