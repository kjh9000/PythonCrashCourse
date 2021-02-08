#!/usr/bin/python3

'''alter 8-7 to use a while loop that allows the user to enter an artist and 
album title, then call the function with that info. make sure users can quit
'''
print("Welcome to the album generator. Enter q to quit at any time.")
while True:
    artist = input("Enter the name of the artist: ") 
    if artist == 'q':
        break
    album = input("Enter an album title: ")
    if album == 'q':
        break
    def make_album(artist, album):
        return {'artist': artist.title(), 'album' : album.title()}
    print("You entered:")
    print(make_album(artist, album))
