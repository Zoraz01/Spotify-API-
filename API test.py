import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = 'Enter your own client id here'
secret = 'Enter your own secret id here'

travis_Scott = 'spotify:artist:0Y5tJX1MQlPlqiwlOH1tJY'
client_credentials_manager = SpotifyClientCredentials(client_id= cid,client_secret=secret)
spotify = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

results = spotify.artist_albums(travis_Scott,album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
