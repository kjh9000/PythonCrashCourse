#!/usr/bin/python3

"""more conditionals
- test for equality and inequality
- test using the lower() function
- numerical tests using <, >, >=, <=.
- test using the and and or keywords
- test for an item in a list
- test if an item is not in a list
"""

cat='dog'
print('Does cat == dog?')
print('cat' == 'dog')

cheese = 'gouda'
print('\nDoes cheese == gouda')
print('cheese' != 'gouda')

name='ALICE'
print('\nDoes name == alice?')
print(name.lower() == 'alice')

the_number = 5
print('\nDoes the_number == 5')
print(the_number == 5)

print('\nIs the_number > 5 ')
print(the_number > 5)


print('\nIs the_number < 5 ')
print(the_number < 5)


print('\nIs the_number >= 5 ')
print(the_number >= 5)


print('\nIs the_number <= 5 ')
print(the_number <= 5)

pig_noise = 'oink'
cow_noise = 'moo'
print('\nDoes pig_noise == oink and cow_noise == moo?')
print(pig_noise == 'oink' and cow_noise == 'moo')


print('\nDoes pig_noise == oink or cow_noise == baah?')
print(pig_noise == 'oink' or cow_noise == 'moo')

list=['Bob','Alice']
print('\nIs Bob in list? ')
print('Bob' in list)

print('\nIs Alice not in list?')
print('Alice' not in list)

