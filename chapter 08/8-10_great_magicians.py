#!/usr/bin/python3

'''modify 8-9 to add 'the Great' to each magician's name
'''

magicians = ['bob', 'alice']
def make_great(magicians):
    newlist = []
    while magicians:
        temp = magicians.pop()
        newlist.append(temp.title() + " the Great")
    magicians = newlist[:]    
    return magicians
print(make_great(magicians))
