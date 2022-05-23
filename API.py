import time
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
# spotipy is required for this application to work

# client id and secret id that corresponds with your account can be acquired from Spotify API website
cid = 'Enter your own client ID here'
secret = 'Enter your own secret ID here'
scope = "user-read-currently-playing"

def get_current_song():
    # Spotify object is created, functions from spotipy can be used on this object to acquire new information
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid,client_secret=secret,redirect_uri='http://example.com',scope=scope))
    # All the information for the currently playing song is assigned to results
    results = sp.currently_playing(market='US')
    # Information from the currently playing song are sorted and assigned
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
    # Application runs in a infinite loop
    while True:
        try:
            prevTrack = current_track
            current_track = get_current_song()
            # Track is only displayed if it is different from the last loop
            if current_track["id"] != current_track_id:
                print(current_track)
                current_track_id = current_track['id']
                # test.jpg is updated with the album cover of the currently playing song
                with open("test.jpg",'wb') as f:
                    f.write(requests.get(current_track['image']).content)
        except:
            # If there is an exception, then the program loops again
            pass
        time.sleep(2)

if __name__ == '__main__':
    main()
