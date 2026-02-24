import requests
import os
from dotenv import load_dotenv

load_dotenv()

class LastFmClient:
    def __init__(self):
        self.api_key = os.getenv("LASTFM_API_KEY")
        self.base_url = "https://ws.audioscrobbler.com/2.0/"

    def get_top_artists(self, limit=50):
        params = {
            "method": "chart.getTopArtists",
            "api_key": self.api_key,
            "format": "json",
            "limit": limit
        }
        response = requests.get(self.base_url, params=params)
        return response.json()

    def get_artist_info(self, artist_name):
        params = {
            "method": "artist.getInfo",
            "artist": artist_name,
            "api_key": self.api_key,
            "format": "json"
        }
        response = requests.get(self.base_url, params=params)
        return response.json()

    def get_viral_artists(self):
        top_artists = self.get_top_artists()
        artists = []

        for artist in top_artists["artists"]["artist"]:
            info = self.get_artist_info(artist["name"])
            artist_info = info.get("artist", {})
            stats = artist_info.get("stats", {})

            artists.append({
                "name": artist["name"],
                "listeners": int(stats.get("listeners", 0)),
                "playcount": int(stats.get("playcount", 0)),
                "tags": [tag["name"] for tag in artist_info.get("tags", {}).get("tag", [])[:3]]
            })

        return sorted(artists, key=lambda x: x["listeners"], reverse=True)