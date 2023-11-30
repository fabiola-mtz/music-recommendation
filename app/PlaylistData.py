import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from endpoint import token_request

"""
    playlist_id : 37i9dQZF1Fa1IIVtEpGUcU
    name : Your Top Songs 2023
"""

class PlaylistData:
    def get_playlist_data(playlist_id, access_token):
        # Setup spotipy with the access token
        sp_token = spotipy.Spotify(auth = access_token)
        # Get tracks from playlist
        tracks = sp_token.tracks(playlist_id, fields = 'items(track(id, name, artists, album(id, name)))')

        print(track)
        # Extract relevant info from given playlist
        music_data = []
        for track_info in tracks['items']:
            track = track_info['track']
            track_name = track['name']
            artists = ', '.join([artist['name'] for artist in track['artists']])
            album_name = track['album']['name']
            album_id = track['album']['id']
            track_id = track['id']
        
         # Pandas datafrme (df) from above xtracted info
        df = pd.DataFrame(music_data)

        return df


    def __init__(self, playlist_id, access_token):
        # Initialization code goes here
        self.playlist_id = playlist_id
        self.access_token = access_token

# Instance of PlaylistData
pl_data = PlaylistData('37i9dQZF1Fa1IIVtEpGUcU', token_request.get_token())


