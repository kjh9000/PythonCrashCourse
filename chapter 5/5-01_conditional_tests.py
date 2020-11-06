#!/usr/bin/python3

"""write a series of conditional tests. print a statement describing
each test and a prediction for the result. create at least 10 test,
five that evaluate to true and five that evaluate to false
"""

# 5 true tests
the_number = 9001
print('Is the_number > 9000? I predict true')
print(the_number > 9000)

mice_caught = 0
print('\nHas the number of mice my cat caught == 0? I predict true.')
print(mice_caught == False)

dog = 'doberman'
print('\nDoes dog == doberman? I predict true.')
print(dog =='doberman')

wi_capital = 'Madison'
print('\nIs the capital of Wisconsin == Madison? I predict true.')
print(wi_capital == 'Madison')

number_kittens = 4
print('\nDo the number_kittens == 4? I predict true.')
print(number_kittens == 4)

# 5 false tests
print('\nIs the_number < 0 I predict false.')
print(the_number < 0)

sky_color='blue'
print('\nIs the sky_color == red? I predict false.')
print(sky_color == 'red')

car='BMW'
print('\nDoes car == Pinto?')
print(car == 'pinto')

music='hiphop'
print('\nDoes music == disco? I predict false.')
print(music == 'disco')

sport='baseball'
print('\nDoes the sport == soccor? I predict false.')
print(sport == 'soccor')


