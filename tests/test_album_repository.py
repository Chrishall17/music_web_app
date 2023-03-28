from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call AlbumRepository#all
We get a list of Albums objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/record_store.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new ArtistRepository

    albums = repository.all() # Get all albums

    # Assert on the results
    assert albums == [
        Album(1, 'Greatest Hits', 1981, 1)
    ]

"""
When we call AlbumRepository#find
We get a single Album object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)

    album = repository.find(1)
    assert album == Album(1, 'Greatest Hits', 1981, 1)

"""
When we call AlbumRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album(None, "Test Album", 1990, 1))

    result = repository.all()
    assert result == [
        Album(1, 'Greatest Hits', 1981, 1),
        Album(2, "Test Album", 1990, 1)
    ]

"""
When we call AlbumRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    repository.delete(1) 

    result = repository.all()
    assert result == [

    ]