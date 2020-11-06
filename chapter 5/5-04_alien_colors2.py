#!/usr/bin/python3

""" a portion of an alien shooter program. use an if-else chain. the alien is
green award 5 points. if it isnt green, award 10 points. write two blocks; one
that uses a series of ifs, and one that uses an if-else block
"""

alien_color = 'green'

#version 1
if alien_color == 'green':
	print('You were awarded 5 points.')
if alien_color != 'green':
	print('You earned 10 points.')

#version 2
if alien_color == 'green':
	print('You were awarded 5 points.')
else:
	print('You earned 10 points.')
