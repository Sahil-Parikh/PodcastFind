from utils.spotify_api import search_spotify_podcast
from utils.youtube_api import search_youtube_podcast

def search_podcasts(person_name):
    spotify_results = search_spotify_podcast(person_name)
    youtube_results = search_youtube_podcast(person_name)

    # Combine results and return
    return {
        "spotify": spotify_results,
        "youtube": youtube_results
    }
