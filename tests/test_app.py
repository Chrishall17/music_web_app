from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
When I call GET /albums
I get a list of albums back
"""
# def test_get_albums(db_connection, web_client):
#     db_connection.seed("seeds/record_store.sql")
#     get_response = web_client.get('/albums')
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == "" \
#         "Album(1, Greatest Hits, 1981, 1)"


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
# def test_post_albums(db_connection, web_client):
#     db_connection.seed("seeds/record_store.sql")
#     response = web_client.post('/albums', data={'title': 'Voyage', 'release_year': 2022, 'artist_id': 2})
#     assert response.status_code == 200
#     assert response.data.decode("utf-8") == ''

#     get_response = web_client.get('/albums')
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == "" \
#         "Album(1, Greatest Hits, 1981, 1)\n" \
#         "Album(2, Voyage, 2022, 2)"
    

# def test_post_albums_no_data(db_connection, web_client):
#     db_connection.seed("seeds/record_store.sql")
#     response = web_client.post('/albums')
#     assert response.status_code == 400
#     assert response.data.decode("utf-8") == '' \
#         "You need to submit a title, release_year, and artist_id"

#     get_response = web_client.get('/albums')
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == "" \
#         "Album(1, Greatest Hits, 1981, 1)" 


"""
When I call GET /artists
I get a list of artists back
"""
# def test_get_artists(db_connection, web_client):
#     db_connection.seed("seeds/record_store.sql")
#     get_response = web_client.get('/artists')
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == "" \
#         "Pixies, ABBA, Taylor Swift, Nina Simone"
    
"""
# Request:
POST /artists
# With body parameters:
    name=Wild nothing
    genre=Indie
# Expected response (200 OK)
(No content)
"""
# def test_post_artists(db_connection, web_client):
#     db_connection.seed("seeds/record_store.sql")
#     response = web_client.post('/artists', data={'name': 'Wild nothing', 'genre': 'Indie'})
#     assert response.status_code == 200
#     assert response.data.decode("utf-8") == ''

#     get_response = web_client.get('/artists')
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == "" \
#         "Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing"
    
# def test_post_artists_no_data(db_connection, web_client):
#     db_connection.seed("seeds/record_store.sql")
#     response = web_client.post('/artists')
#     assert response.status_code == 400
#     assert response.data.decode("utf-8") == '' \
#         "You need to submit a name, and genre"

#     get_response = web_client.get('/artists')
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == "" \
#         "Pixies, ABBA, Taylor Swift, Nina Simone"
    
def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    paragraph_tags = page.locator("p")
    expect(paragraph_tags).to_have_text([
        "Release year: 1981",
        "Artist: Pixies",
        "Go back"      
    ])
    

def test_visit_album_show_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Greatest Hits'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Greatest Hits")

def test_visit_album_show_page_and_go_back(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Greatest Hits'")
    page.click("text='Go back'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Albums")


def test_get_artists_by_id(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/artists/1")
    paragraph_tags = page.locator("p")
    expect(paragraph_tags).to_have_text([
        "Genre: Rock"      
    ])

def test_visit_artist_show_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Pixies'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Pixies")
    p_tag = page.locator("p")
    expect(p_tag).to_have_text("Genre: Rock")

"""
We can create a new album
And see it reflected in the list of albums
"""
def test_create_album(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Add new album'")
    page.fill("input[name=title]", "Test Album")
    page.fill("input[name=release_year]", "2000")
    page.fill("input[name=artist_id]", "4")

    page.click("text=Add album")

    paragraph_tags = page.locator("p")
    expect(paragraph_tags).to_have_text([
        "Release year: 2000",
        "Artist: Nina Simone",
        "Go back"      
    ])
    

def test_create_album_with_errors(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")

    page.click("text='Add new album'")
    page.click("text=Add album")

    errors_tag = page.locator(".t-errors")
    expect(errors_tag).to_have_text(
        "Your form contained errors: Title can't be blank, Release year can't be blank, Artist ID can't be blank"
    )
