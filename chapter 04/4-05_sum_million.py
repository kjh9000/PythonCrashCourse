#!/usr/bin/python3
#make a list of numbers one to one million, then use min(), max() and sum() functions to be certain of the range and to see the sum of the numbers
numbers=[i+1 for i in range(0,1000000)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))
