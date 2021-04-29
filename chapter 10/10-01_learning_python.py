#!/usr/bin/python3

"""Open a blank file in your text editor and write a few
lines summarizing what you’ve learned about Python so far Start each line
with the phrase In Python you can... Save the file as learning_python.txt in the
same directory as your exercises from this chapter Write a program that reads
the file and prints what you wrote three times Print the contents once by reading in the entire file, once by looping over the file object, and once by storing
the lines in a list and then working with them outside the with block"""

filename = 'learning_python.txt'
print("~~Printing contents of the file all at once:~~")
with open(filename) as fo:
        print(fo.read())

print("~~Printing contents by looping through said contents once:~~")
with open(filename) as fo:
    temp = ''
    for i in fo:
        temp += i
    print(temp)

print("~~Printing the contents by storing them in a list then manipulating them " + "outside the with block.~~")
with open(filename) as fo:
        temp = fo.readlines()
for i in temp:
    print(i.rstrip())



