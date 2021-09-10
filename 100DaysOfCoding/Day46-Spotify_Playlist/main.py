from pprint import pprint
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


SPOTIFY_CLIENT_ID = "Your Spotify Client ID"
SPOTIFY_CLIENT_SECRET = "Your client Secret"
user_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD?: ")
year_list = user_input.split("-")
# print(year_list)
response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_input}").text

soup = BeautifulSoup(response, "html.parser")
# print(soup.prettify())
songs_span_list = soup.find_all(name="span", class_="chart-element__information__song")
# print(songs_span_list)
songs_title_list = [song_title.getText() for song_title in soup.find_all(name="span", class_="chart-element__information__song")]
# print(songs_title_list)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri="http://example.com",
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="token.txt"
))

user_id = sp.current_user()["id"]

songs_uri = []
for song in songs_title_list:
    result = sp.search(q=f"track:{song} year:{year_list[0]}", type="track")
    # pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs_uri.append(uri)
    except IndexError:
        pass
        # print(f"{songs_title_list} doesn't exist in Spotify. Skipped.")
    # print(songs_uri)


playlist = sp.user_playlist_create(user=sp.current_user()["id"], name=f"{user_input} Billboard 100", public=False)
pprint(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=songs_uri)
