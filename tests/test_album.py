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
