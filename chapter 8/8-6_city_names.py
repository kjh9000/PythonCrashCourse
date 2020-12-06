#!/usr/bin/python3

'''write a function called city_country() that takes the name of a city and
country and returns a formatted string like "Santiago, Chile" (with the
double quotes). call three times
'''

def city_country(city, country):
    return '"' + city.title() + ", " + country.title() + '"'

print(city_country('new york', 'united states of america'))
print(city_country('berlin', 'germany'))
print(city_country('london', 'england'))
