#!/usr/bin/python3
#make a list of 5 foods and store in a tuple. print out with a for loop, and rewrite the program changing 2 foods. print revised menu
buffet=('macaroni salad','chicken wings','garden salad','steak','fish')
print('Original buffet:')
for i in buffet:
	print(i)
buffet=('macaroni salad','chicken wings','garden salad','bologna sandwiches','tofu')
print('New buffet:')
for i in buffet:
	print(i)
#the exercise calls for attempting to change a tuple in place, so its placed at the end
buffet[0]='lasgana'
