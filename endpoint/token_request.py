import requests
import base64
import pandas as pd

# Replace with own generated Client ID and Client Secret
CLIENT_ID = ""
CLIENT_SECRET = ""

def get_token():
    # Encode credentials on Base64 
    client_credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
    client_credentials_base64 = base64.b64encode(client_credentials.encode())

    # Request access token
    token_url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization':f'Basic {client_credentials_base64.decode()}'
    }
    data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(token_url, data=data, headers=headers)

    if response.status_code == 200:
        access_token = response.json()['access_token']
        print("Access token obtained succesfully")
    else:
        print("Error obtaining access token.")
        exit()
    
    return access_token