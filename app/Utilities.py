import pandas as pd
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from app import callback

class Utilities:
    def __init__(self, playlist_id, access_token):
        # Initialization code goes here
        self.playlist_id = playlist_id
        self.access_token = access_token

    
    def create_new_pl(access_token, user_id, playlist_name, playlist_description="", public=False):
        # Create playlist endpoint
        create_pl_endpoint = f'https://api.spotify.com/v1/users/{user_id}/playlists'

        # Headers for the request
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }

        # Data payload for the POST request, including playlist details
        data = {
        'name': playlist_name,
        'description': playlist_description,
        'public': public
        }

        response = requests.post(create_pl_endpoint, headers=headers, json=data)

        if response.status_code == 200:
            # Parse the JSON response and extract the playlist ID
            playlist_id = response.json().get("id")
            print(f"Playlist '{playlist_name}' created successfully with ID: {playlist_id}")

            return playlist_id
        else:
            # Print an error message if the request was not successful
            print(f"Error: {response.status_code}")
            print(response.text)
            return None

# Instance of Utilities
pl_data = Utilities('37i9dQZF1Fa1IIVtEpGUcU', callback())
pl_data.create_new_pl(callback(), user_id = '1284826421', playlist_name = "A ver q show Playlist")