import time

import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import urllib.request

cid = '924d5bddc07f4588a2bd13c7fef258f9'
secret = 'ae858f86e4ae4ee489652037637a23c5'
scope = "user-read-currently-playing"
def get_current_song():
    ##client_credentials_manager = SpotifyClientCredentials(client_id= cid,client_secret=secret)
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid,client_secret=secret,redirect_uri='http://example.com',scope=scope))
    results = sp.currently_playing(market='US')
    track_id = results['item']['id']
    track_name = results['item']['name']
    artists = [artist for artist in results['item']['artists']]

    link = results['item']['external_urls']['spotify']

    artist_names = ', '.join([artist['name'] for artist in artists])
    image = results['item']['album']['images'][1]["url"]
    current_track_info = {
        "id": track_id,
        "track_name": track_name,
        "artists": artist_names,
        "link": link,
        "image": image
        }
    return current_track_info
def main():
    current_track_id = None
    current_track = None
    while True:
        try:
            prevTrack = current_track
            current_track = get_current_song()
            if current_track["id"] != current_track_id:
                print(current_track)
                current_track_id = current_track['id']
                with open("test.jpg",'wb') as f:
                    f.write(requests.get(current_track['image']).content)
        except:
            pass
        time.sleep(2)

if __name__ == '__main__':
    main()