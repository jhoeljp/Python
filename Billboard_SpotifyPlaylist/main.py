'''
Name: Jhoel 

Top 100 Billboard 

Create a Spotify playlist from a list of the Top 100 Billboard songs from a specific date

Use Spotipy - as python library for spotify web api 
https://spotipy.readthedocs.io/en/2.19.0/#
python3 -m pip install spotipy

All methods require user authorization. 
You will need to register your app at My Dashboard to get the credentials necessary to make authorized calls 
(a client id and client secret).

Also add a redirect URI to your application at My Dashboard (navigate to your application and then [Edit Settings]).

'''
#date 
# date = input("Enter date to look 100 Billboard (year-month-day): ")
date = "1996-08-29"

#get url's html to scrape from
import requests
URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url=URL)

response.raise_for_status()


#Scrape for list of songs 
from bs4 import BeautifulSoup
import pprint
soup = BeautifulSoup(response.text,"html.parser")

top_song = (soup.find(name='a',class_="c-title__link lrv-a-unstyle-link")).getText()
# print(top_song)
song_titles = [(song.getText()).split('\n')[1] for song in soup.find_all(name="h3",class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")]
# pprint.pprint(song_titles)

#------------------ SING IN ON SPOTIFY ------------------

#import env variables 
from dotenv import load_dotenv
import os 

#Load environment files 
ENV_FILE = "secrets.env"
full_env_path = f"{os.getcwd()}/{ENV_FILE}"
load_dotenv(full_env_path)

import spotipy
from spotipy.oauth2 import SpotifyOAuth
SCOPE = "playlist-modify-private"

#Authorization method 
#In order to make successful Web API requests your app will need a valid access token. One can be obtained through OAuth 2.0.
auth2 = SpotifyOAuth(client_id=os.environ.get("SPOTIPY_CLIENT_ID"), client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET") , scope=SCOPE)

#Request Access Token
token = auth2.get_cached_token()
access_tk = token['access_token']
refresh_tk = token['refresh_token']
# # access_type = token['token_type']


#Make Request to Spotify API 
#format "Authorization: Bearer NgCXRK...MzYjw"
header_auth = {"Authorization": f"Bearer {access_tk}"}


# request_url = "https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V"
# response = requests.get(url=request_url,headers=header_auth)
# response.raise_for_status()
# print(response.text)

#get authorized user account details 
sp = spotipy.client.Spotify(auth=access_tk)
user = sp.current_user()
ID = user['id']
print(user)

#once authorized lets Create a brand new Playlist 
playlist_end_point = f"https://api.spotify.com/v1/users/{ID}/playlists"

#make body of request

#public field defaults to true
new_playlist_data = {
    "name": f"{date} 100 Billboard",
    "description": f"Travel back in time and listen to the Top 100 Billboard songs from {date}"
}

#make POST request creating playlist 
response = requests.post(url=playlist_end_point,data=new_playlist_data,headers=header_auth)
response.raise_for_status()
print(response.text)