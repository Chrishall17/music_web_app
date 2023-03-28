# Tests for your routes go here

"""
When I call GET /albums
I get a list of albums back
"""
def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, Greatest Hits, 1981, 1)"


"""
# Request:
POST /albums
# With body parameters:
    title=Voyage
    release_year=2022
    artist_id=2
# Expected response (200 OK)
(No content)
"""
def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.post('/albums', data={'title': 'Voyage', 'release_year': 2022, 'artist_id': 2})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ''

    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, Greatest Hits, 1981, 1)\n" \
        "Album(2, Voyage, 2022, 2)"
    

def test_post_albums_no_data(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.post('/albums')
    assert response.status_code == 400
    assert response.data.decode("utf-8") == '' \
        "You need to submit a title, release_year, and artist_id"

    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, Greatest Hits, 1981, 1)" 


"""
When I call GET /artists
I get a list of artists back
"""
def test_get_artists(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Pixies, ABBA, Taylor Swift, Nina Simone"
    
"""
# Request:
POST /artists
# With body parameters:
    name=Wild nothing
    genre=Indie
# Expected response (200 OK)
(No content)
"""
def test_post_artists(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.post('/artists', data={'name': 'Wild nothing', 'genre': 'Indie'})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ''

    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing"
    
def test_post_artists_no_data(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.post('/artists')
    assert response.status_code == 400
    assert response.data.decode("utf-8") == '' \
        "You need to submit a name, and genre"

    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Pixies, ABBA, Taylor Swift, Nina Simone"