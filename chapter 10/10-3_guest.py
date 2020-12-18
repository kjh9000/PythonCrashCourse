#!/usr/bin/python3

guest = input("Whpo is the guest?: ")
with open('guests.txt', 'a') as fo:
    fo.write(guest + "\n")
