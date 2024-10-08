import unittest
from utils.spotify_api import search_spotify_podcast

class TestSpotifyAPI(unittest.TestCase):
    def test_search_spotify_podcast(self):
        results = search_spotify_podcast("Elon Musk")
        self.assertIsNotNone(results)

if __name__ == '__main__':
    unittest.main()
