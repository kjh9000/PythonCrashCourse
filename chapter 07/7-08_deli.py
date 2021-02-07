#!/usr/bin/python3

sandwich_orders = ['sub', 'pb&j', 'knuckle']
finished_sandwiches = []

while sandwich_orders:
    temp = sandwich_orders.pop()
    print("Making a " + temp + ".")
    finished_sandwiches.append(temp)
print("\nDone!\n")
print("The following sandwiches were made:")
for i in finished_sandwiches:
    print(i)
