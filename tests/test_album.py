from lib.album import Album

"""
Album constructs with an id, title, release year and artist id
"""
def test_album_constructs():
    album = Album(1, "Test Title", 0, 1)
    assert album.id == 1
    assert album.title == "Test Title"
    assert album.release_year == 0
    assert album.artist_id == 1

"""
We can format albums to strings nicely
"""
def test_albums_format_nicely():
    album = Album(1, "Test Title", 0, 1)
    assert str(album) == "Album(1, Test Title, 0, 1)"


"""
We can compare two identical albums
And have them be equal
"""
def test_artists_are_equal():
    album1 = Album(1, "Test Title", 0, 1)
    album2 = Album(1, "Test Title", 0, 1)
    assert album1 == album2

def test_is_valid():
    album = Album(None, "My title", 1990, 2)
    valid = album.is_valid()
    assert valid == True

"""
With non integer convertible string release year
It is not valid
"""
def test_is_not_valid_with_bad_release_year():
    album1 = Album(None, "My title", "2000", 1)
    valid1 = album1.is_valid()
    assert valid1 == False
    album2 = Album(None, "My title", None, 1)
    valid2 = album2.is_valid()
    assert valid2 == False
    album3 = Album(None, "My title", "fred", 1)
    valid3 = album3.is_valid()
    assert valid3 == False