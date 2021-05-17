#!/usr/bin/python3

""" Modify your except block in Exercise 10-8 to fail
silently if either file is missing """

files = ['cats.txt', 'dogs.txt', 'nothinghere.txt']

for filename in files:
    try:
        with open(filename) as fo:
            contents = fo.read()
    except FileNotFoundError:
        pass
    else:
        print(contents.strip())
