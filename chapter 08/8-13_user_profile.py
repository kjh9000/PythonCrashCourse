#!/usr/bin/python3

'''start with a copy of user_profile.py. build a profile of yourself by calling
build profile, using first and last name and three other key-value pairs that
describe you
'''

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

print(build_profile('kevin', 'h', fav_programming_language='python', pets='cats', fav_beverage=' japanese sencha'))
