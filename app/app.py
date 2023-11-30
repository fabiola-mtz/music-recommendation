from flask import Flask, request, redirect
import requests
import base64

app = Flask(__name__)

# Replace with your actual client ID, client secret, and redirect URI
CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URI = 'http://localhost:8080/'

# Base64 encode the client ID and client secret
client_credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
client_credentials_base64 = base64.b64encode(client_credentials.encode()).decode()

@app.route('/login')
def login():
    authorize_url = 'https://accounts.spotify.com/authorize'
    authorize_params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': REDIRECT_URI,
        'scope': 'playlist-modify-public',
    }
    authorize_url_with_params = f"{authorize_url}?{urlencode(authorize_params)}"
    return redirect(authorize_url_with_params)

@app.route('/callback')
def callback():
    # Capture the authorization code from the redirect URI
    authorization_code = request.args.get('code')

    # Exchange authorization code for access token
    token_url = 'https://accounts.spotify.com/api/token'
    token_data = {
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'redirect_uri': REDIRECT_URI,
    }
    token_headers = {
        'Authorization': f'Basic {client_credentials_base64}',
    }
    token_response = requests.post(token_url, data=token_data, headers=token_headers)

    # Extract access token from the response
    access_token = token_response.json().get('access_token')

    # return f"Access Token: {access_token}"
    return access_token

if __name__ == '__main__':
    app.run(port=5000)
