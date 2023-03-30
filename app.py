import os
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist
from flask import Flask, request, render_template

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# @app.route('/albums', methods=['POST'])
# def post_albums():
#     if 'title' not in request.form or 'release_year' not in request.form or 'artist_id' not in request.form:
#         return "You need to submit a title, release_year, and artist_id", 400
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     album = Album(
#         None,
#         request.form['title'],
#         request.form['release_year'],
#         request.form['artist_id']
#         )
#     repository.create(album)

#     return "", 200

# @app.route('/artists', methods=['POST'])
# def post_artists():
#     if 'name' not in request.form or 'genre' not in request.form:
#         return "You need to submit a name, and genre", 400
#     connection = get_flask_database_connection(app)
#     repository = ArtistRepository(connection)
#     artist = Artist(
#         None,
#         request.form['name'],
#         request.form['genre']
#         )
#     repository.create(artist)

#     return "", 200


# @app.route('/artists', methods=['GET'])
# def get_artists():
#     connection = get_flask_database_connection(app)
#     repository = ArtistRepository(connection)

#     return ", ".join(
#         f"{artist}" for artist in repository.all()
#     )


@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artists = artist_repository.all()

    return render_template("artists/main.html", artists=artists)


@app.route('/artists/<id>', methods=['GET'])
def get_artists_id(id):
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)    
    artist = artist_repository.find(id)

    return render_template("artists/show.html", artist=artist)


@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    albums = album_repository.all()

    return render_template("albums/main.html", albums=albums)


@app.route('/albums/<id>', methods=['GET'])
def get_albums_id(id):
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)    
    album = album_repository.find(id)
    artist_repository = ArtistRepository(connection)
    artist = artist_repository.find(album.artist_id)

    return render_template("albums/index.html", album=album, artist=artist)


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

