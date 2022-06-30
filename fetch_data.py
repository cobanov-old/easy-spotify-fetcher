from dataclasses import dataclass
from numpy import datetime64
from pendulum import date
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
import json


SPOTIPY_CLIENT_ID = "YOUR_SPOTIPY_CLIENT_ID"
SPOTIPY_CLIENT_SECRET = "YOUR_SPOTIPY_CLIENT_SECRET"
ARTIST_ID = "YOUR_ARTIST_ID"


spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
    )
)

results = spotify.artist_albums(ARTIST_ID, album_type="album")  # artist id


albums = results["items"]

while results["next"]:
    results = spotify.next(results)
    albums.extend(results["items"])


metadatas = []

for album in albums:
    data = {}
    data["name"] = album["name"]
    data["release_date"] = album["release_date"]
    data["total_tracks"] = album["total_tracks"]
    data["image"] = album["images"][0]["url"]
    data["artists"] = [artists["name"] for artists in album["artists"]]
    metadatas.append(data)


with open("spotify_data.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(metadatas, ensure_ascii=False, indent=4))

# metadatas = []


# for album in albums:
#     metadatas.append(album["images"][0]["url"])

# with open("spotify_images.txt", "w") as f:
#     for i in metadatas:
#         f.write(i)
#         f.write("\n")
