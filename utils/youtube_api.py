import requests
from config.config import YOUTUBE_API_KEY

def search_youtube_podcast(person_name):
    query = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={person_name}+podcast&key={YOUTUBE_API_KEY}"
    response = requests.get(query)
    return response.json()
