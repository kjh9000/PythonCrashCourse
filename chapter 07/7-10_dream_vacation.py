#!/usr/bin/python3

print("~~~~Dream Vacation Poll~~~")
vacation = {}
while True:
    name = input("Who are you? ")
    place = input("Where do you want to go? ")
    anwser = input("Do you want to add another person and place? ('n' to quit)")
    vacation[name] = place
    if anwser == 'n':
        break
for k, v in vacation.items():
    print(k.title() + " entered " + v.title() + " as their dream vacation destination.")
