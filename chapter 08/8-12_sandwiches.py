#!/usr/bin/python3

'''write a function that accepts a list of sandwiche fixing. the function 
should have one parameter to accept any number of items as the function call provides, and it should print a summary o9f the sandwich being ordered. call
fuction three times each with a different number of items
'''

def sandwich(*fixings):
        print("You ordered a sandwich with " + str(fixings) + ".")
sandwich("ghost peppers", "ham", "bologna")
sandwich("knuckle")
sandwich("pastrami","roast beef")
