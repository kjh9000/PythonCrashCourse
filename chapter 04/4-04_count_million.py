#!/usr/bin/python3
#create a list of numbers from one to one million. use a for loop to print out each number. end the program if its taking too long
numbers=[i+1 for i in range(1000000)]
for i in numbers:
	print(i)
