# easy-spotify-fetcher

Fetch data as JSON files and download album covers, easily.

## Requirements
```
pendulum
spotipy
```

## Usage
Provide the information and run the script.
```
SPOTIPY_CLIENT_ID = "YOUR_SPOTIPY_CLIENT_ID"
SPOTIPY_CLIENT_SECRET = "YOUR_SPOTIPY_CLIENT_SECRET"
ARTIST_ID = "YOUR_ARTIST_ID"
```


## Download Images

```python
for album in albums:
    metadatas.append(album["images"][0]["url"])

with open("spotify_images.txt", "w") as f:
    for i in metadatas:
        f.write(i)
        f.write("\n")
```

```
wget -i spotify_images.txt
```
```bash
for f in $(ls); do mv $f $f.png ;done
```
