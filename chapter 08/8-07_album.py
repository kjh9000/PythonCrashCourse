#!/usr/bin/python3

'''write a function called make_album() that builds a dict describing an album.
the fuction takes an artist name and album title, and return a dict containing 
the two pieces of info. make three ablums and print out details. add an
optional third parameter for the number of tracks. make one album with tracks
'''

def make_album(artist, album, tracks=''):
    if tracks:
        return {'artist': artist.title(), 'album' : album.title(), 'tracks':
        tracks}
    else:
        return {'artist': artist.title(), 'album' : album.title()}
print(make_album('prince','purple rain', 9))
print(make_album('beatles','help'))
print(make_album('u2','war'))

