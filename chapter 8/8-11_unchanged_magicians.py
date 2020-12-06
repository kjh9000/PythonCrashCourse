#!/usr/bin/python3

'''start with exercise 8-10. call the make_great function with a copy of the
list. return the new list and store it in a seperate list. call
show_magicians() with each list to show the original and altered lists
'''

magicians =['bob', 'alice']
magicians_copy = magicians[:]
new_list= []

def make_great(magicians):
    while magicians_copy:
        temp = magicians_copy.pop(0) #use zero here to preserve list order
        new_list.append(temp + " the Great")

make_great(magicians)


def show_magicians(magicians):
    for i in magicians:
        print(i.title())

print("The original list contains:")
show_magicians(magicians)

print("\nThe altered list is:")
show_magicians(new_list)
