#!/usr/bin/python3

'''write a function called make_shirt() that accepts a size and message to be
printed on the shirt. call the function twice, once using positional arguments, and again with keyword arguments
'''

#starting with positional arguments
def make_shirt(size, message):
    print("You ordered a " + size + " tshirt with the message '" + message +
    "'.")

make_shirt("large", "Hey there!")


# keyword arguments
def make_shirt(size, message):
    print("You ordered a " + size + " tshirt with the message '" + message +
    "'.")

make_shirt( message="I learned Python and all I got was this lousy tshirt.", size="small")

