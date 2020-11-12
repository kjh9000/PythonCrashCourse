#!/usr/bin/python3

"""make a dict of three major rivers and the country it is in. loop through it,
printing something remarking the river and country
"""

rivers = {'mississipi': 'usa', 'amazon': 'brazil', 'rhine':'germany'}

for k, v in rivers.items():
    print('The river',k.title(),'is in the country',v.title() + '.')
