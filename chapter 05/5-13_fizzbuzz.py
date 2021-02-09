#!/usr/bin/python3

"""choose a program you want to write. im doing a variant of the fizzbuzz 
program that most compsci grads couldnt complete. loop through a list of numbers 1-100. if a number is:
divisible by 3, print Fizz
divisible by 5, print Buzz
divisible by both 3 and 5, print Fizzbuzz
if not divisible by any of the above numbers, print the number
"""

for i in range(1, 101):
    if i % 15 == 0:
        print('Fizzbuzz.')
    elif i % 5 == 0:
        print('Buzz.')
    elif i % 3 == 0:
        print('Fizz.')
    else:
        print(i)
