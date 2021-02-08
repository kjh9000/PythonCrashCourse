#!/usr/bin/python3

'''make a list of magicians. pass the list to a function show_magicians, 
printing the name of each magician in the list
'''

magicians =['bob', 'alice']
def show_magicians(magicians):
    for i in magicians:
        print(i.title())
show_magicians(magicians)
