import requests
from config.config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

def get_spotify_token():
    """Get Spotify API token using client credentials."""
    auth_url = "https://accounts.spotify.com/api/token"
    auth_data = {"grant_type": "client_credentials"}
    auth_response = requests.post(auth_url, data=auth_data, auth=(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET))
    
    if auth_response.status_code == 200:
        token = auth_response.json()['access_token']
        return token
    else:
        print(f"Error generating token: {auth_response.status_code}")
        print(auth_response.json())  # Print error message
        return None


def search_spotify_podcast(person_name):
    """Search for podcasts on Spotify by person's name."""
    token = get_spotify_token()
    
    if not token:
        return None  # Exit if token generation fails
    
    headers = {"Authorization": f"Bearer {token}"}
    query = f"q={person_name}&type=show,episode"  # Include both podcast shows and episodes
    url = f"https://api.spotify.com/v1/search?{query}"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error searching Spotify: {response.status_code}")
        print(response.json())  # Print any error messages for debugging
        return None
