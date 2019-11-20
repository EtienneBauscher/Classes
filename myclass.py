"""This is 'myclass.py' it is a programme that returns
the following:
    1. The artist in a list.
    2. The albums of the list of a particular artist.

This program utilises a class with two functions."""

# define the class


class MyAlbumCollection():
    """'MyAlbumCollection' class that receives three variables namely:
        a. artist - for receiving the artist name in any class object
        b. album_name - "                   "                       "
        c. number_of_tracks - "              "                      "
    """
    # initiate the variables through the constuctor

    def __init__(self, artist, album_name, number_of_tracks):
        self.artist = artist
        self.album_name = album_name
        self.number_of_tracks = number_of_tracks
    # function 1

    def artist_list(self):
        """'artist_list' function returns the artist in a
        album collection list"""
        artists = self.artist
        print(artists)
    # function2

    def artist_album(self):
        """'artist_album' this function returns a list of artists with
        their corresponding albums"""
        albums = self.album_name
        for i in albums:
            print(i)

    def number_tracks(self):
        """'number_tracks' a function for returning the number of
        tracks in a collection"""
        calc = sum(self.number_of_tracks)
        return calc


# set album collections by creating class objects
ALBUMS1 = MyAlbumCollection(
    'Fred Hammond', ['Speak those things', 'The Spirit of David'], [12, 10])
ALBUMS2 = MyAlbumCollection(
    'J Moss', ['Grown folks gospel', 'Psalm 150'], [11, 14])
ALBUMS3 = MyAlbumCollection('Carmen', ['The Champion', 'Redemption'], [10, 13])
# call some test functions
ALBUMS1.artist_album()
ALBUMS3.artist_list()
print(f'{ALBUMS2.number_tracks()} tracks in the {ALBUMS2.artist} collection')
# sum all the tracks on the collections
NUMBER = [ALBUMS1, ALBUMS2, ALBUMS3]
TOTALTRACKS = []
for num in NUMBER:
    TOTALTRACKS.append(MyAlbumCollection.number_tracks(num))
print(
    f'The total no. of tracks of all the collections is, {sum(TOTALTRACKS)}.')
