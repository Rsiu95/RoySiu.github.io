import requests
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
import spotipy
from dotenv import load_dotenv
import os

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

URL = "https://www.billboard.com/charts/hot-100/"

sp = spotipy.Spotify(
auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri="http://example.com",
    client_id= SPOTIFY_CLIENT_ID,
    client_secret= SPOTIFY_CLIENT_SECRET,
    show_dialog=True,
    cache_path="./Udemy 100 Days of Code/Day 46/token.txt",
    )
)

def get_top_100_song_list():

    date_of_interest = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

    songs_of_date = URL + date_of_interest
    response = requests.get(songs_of_date)
    web_info = response.text

    soup = BeautifulSoup(web_info, "html.parser")
    
    song_titles = []
    for song in soup.select(selector="li #title-of-a-story"):
        song_titles.append(song.getText().split("\t")[9].split("\t")[0])
        
    artist_label = soup.select(selector = "li.o-chart-results-list__item span.c-label")
    artists = []
    for artist in artist_label:
        name = artist.get_text(strip = True)
        try:
            int(name)
        except ValueError:
            if str(name) == "-" or str(name) == "RE-\nENTRY" or str(name) == "NEW":
                continue
            artists.append((name))
    song_info = {song:artist for song, artist in zip(song_titles, artists)}
        
    return [song_info, date_of_interest]

def get_song_uri(song_info_list):
    song_uri = []
    for key, value in song_info_list[0].items():
        results = sp.search(q=f'track:{key}',type = "track")
        try:    
            for artist in results['tracks']['items']:
                if value in artist['artists'][0]['name']:
                    song_uri.append(artist['uri'])
                    break
        except:
            print(f"{key} song not found.")
            continue
    return song_uri

def create_playlist(user_id, user_date, playlist_name, status=bool):
    playlist = sp.user_playlist_create(user_id, f"{user_date[1].strip()} {playlist_name}", public=status)
    return playlist['id']

def main():
    song_info = get_top_100_song_list()
    song_uris = get_song_uri(song_info)
    user_id = sp.current_user()["id"]
    playlist_id = create_playlist(user_id, song_info[1], f"{song_info[1].strip()} Billboard Top 100", False)
    sp.user_playlist_add_tracks(user_id, playlist_id, song_uris)

if __name__ == '__main__':
    main()