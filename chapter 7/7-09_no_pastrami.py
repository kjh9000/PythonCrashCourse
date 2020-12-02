#!/usr/bin/python3

sandwich_orders = ['sub', 'pb&j', 'knuckle', 'pastrami']
finished_sandwiches = []

while sandwich_orders:   
    temp = sandwich_orders.pop()
    if temp == 'pastrami':
        print("We're out of pastrami. Skipping...")
    else:
        print("Making a " + temp + ".")
        finished_sandwiches.append(temp)
print("\nDone!\n")
print("The following sandwiches were made:")
for i in finished_sandwiches:
    print(i)
