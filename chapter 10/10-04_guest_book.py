#!/usr/bin/python3

""" Guest Book: Write a while loop that prompts users for their name When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt Make sure each entry appears on a
new line in the file """

while True:
    name = input("What name do you want to add to the guest list? (Hit q to quit): ")
    if name == 'q':
        break
    with open('guestbook.txt', 'a') as fo:
        fo.write(name)
        fo.write("\n")
    print(name + " added to the guestbook.")
