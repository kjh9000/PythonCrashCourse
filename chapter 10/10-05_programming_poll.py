#!/usr/bin/python3

""" Write a while loop that asks people why they like
programming Each time someone enters a reason, add their reason to a file
that stores all the responses """

while True:
    answer = input("Why do you like prgramming? (Hit q to quit): ")
    if answer == 'q':
        break
    with open('answers.txt', 'a') as fo:
        fo.write(answer)
        fo.write("\n")
