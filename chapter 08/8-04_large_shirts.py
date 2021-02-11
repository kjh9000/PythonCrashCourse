#!/usr/bin/python3

''' modify the  make_shirt() so shirts are large by default, and the default
message is 'I love Python'. make three shirts:
-one medium and one large shirt with the default message
-one of any size shirt with a different message
'''

def make_shirt(size='large', message='I love Python'):
    print("You ordered a " + size + " tshirt with the message '" + message + "'.")

make_shirt() 
make_shirt(size='medium')
make_shirt(size='giagantic', message='Howdyho!')
