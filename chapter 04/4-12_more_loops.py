#!/usr/bin/python3
#use a verson of the foods.py program, and modify to use a for loop to print out each list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
for i in my_foods:
	print(i)
print("\nMy friend's favorite foods are:")
for i in friend_foods:
	print(i)
