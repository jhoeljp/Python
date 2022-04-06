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

#------------------ DEPENDENCIES ------------------


#Spotipy 
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#Web scrapping 
import requests
from bs4 import BeautifulSoup

#import env variables 
from dotenv import load_dotenv
import os 

#pprint 
from pprint import pprint as b_print  


#------------------ BILLBOARD ------------------


#date 
# date = input("Enter date to look 100 Billboard (year-month-day): ")
date = "1996-08-29"
song_delimeter = "@"

def scrape_billboard(date,delimeter):

    #get url's html to scrape from
    URL = f"https://www.billboard.com/charts/hot-100/{date}"
    response = requests.get(url=URL)

    response.raise_for_status()

    #Scrape for list of songs 
    soup = BeautifulSoup(response.text,"html.parser")

    #SONG DETAILS 
    songs_titles, songs_authors = [], []
    #get top song 
    top_song = (soup.find(name='a',class_="c-title__link lrv-a-unstyle-link")).getText().split('\t')[8]
    top_artist = (soup.find(name='p',class_="c-tagline a-font-primary-l a-font-primary-m@mobile-max lrv-u-color-black u-color-white@mobile-max lrv-u-margin-tb-00 lrv-u-padding-t-025 lrv-u-margin-r-150")).getText().split('\n')[0]

    #get rest of top chart songs 
    songs_titles = [(song.getText().split('\t'))[9] for song in soup.find_all(name="h3",id="title-of-a-story",class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")]
    songs_authors = [((((song.getText()).split('\t'))[2]).split('\n'))[0] for song in soup.find_all(name="span",class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")]
    
    songs_titles.insert(0,top_song)
    songs_authors.insert(0,top_artist)
    #join on list song-author for a better spotify api search 
    billboard_list = [f"{song}{delimeter}{songs_authors[i]}" for i,song in enumerate(songs_titles)]
    # b_print(billboard_list)

    return billboard_list

#scrapped top 100 song of date
billboard_list = scrape_billboard(date,song_delimeter)
b_print(billboard_list)

#------------------ SPOTIFY ------------------


#Load environment files 
ENV_FILE = "secrets.env"
full_env_path = f"{os.getcwd()}/{ENV_FILE}"
load_dotenv(full_env_path)


#Authoriation variables
CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
RE_URI = os.environ.get("SPOTIPY_REDIRECT_URI")
SCOPE = "playlist-modify-private"


def get_spotify_user():

    #Obtain Spotidy ID for Spotify client 
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope=SCOPE,
            redirect_uri=RE_URI,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            show_dialog=True,
            cache_path="token.txt"
        )
    )

    #fetch user ID 
    user_id = sp.current_user()["id"]
    print(f"USER ID OF SPOTIFY IS : {user_id}")

    new_playlist = {
        "name": f"{date} 100 Billboard",
        "description": f"Travel back in time and listen to the Top 100 Billboard songs from {date}"}

    # sp.user_playlist_create(user=user_id,
    #                         name=new_playlist['name'],
    #                         public=True,
    #                         description=new_playlist['description'])
    return sp, user_id


#Obtain Spotidy ID for Spotify client 
# SP, USER_ID = get_spotify_user()


#MAKE LIST OF SONGS 
def find_spotify_songs(SP):
    uri_list = []

    for song_info in billboard_list:
        song, author = song_info.split(song_delimeter)
        #narrow down your search using field filters. 
        # query = f"track: {song} artist:{author} year: {date.split('-')[0]}" 
        
        # query = f"track: {song} artist:{author}" 
        #"remaster%20track:Doxy+artist:Miles%20Davis"
        api_song = "%20".join(song.split(' '))
        # print(api_song)
        print(song)
        query = f"track:{api_song}+artist:{author}" 
        # print(query)
    

        #search with filters 
        search_result = SP.search(q=query,limit=1,type="track",offset=0)
        # b_print(search_result)

        # print(((search_result['tracks'])['items'])['uri'])
        try:
            track_uri = ((((search_result['tracks'])['items']))[0])['uri']
            uri_list.append(track_uri)
        except IndexError:
            #track doesnt exist or search is empty 
            # print("IndexError")
            # uri_list.append("None")

            # b_print((((search_result['tracks'])['items'])))
            
            pass
    return uri_list

# songs_uri_list = find_spotify_songs(SP)
# for song in songs_uri_list:
#     print(song)

#Create brand new playlist 

#Authorization method 
#In order to make successful Web API requests your app will need a valid access token. One can be obtained through OAuth 2.0.

# auth2 = SpotifyOAuth(client_id=CLIENT_ID ,client_secret= CLIENT_SECRET,redirect_uri= RE_URI,scope=SCOPE)

# sp = spotipy.Spotify(auth_manager=auth2)

# #Request Access Token
# token = auth2.get_cached_token()
# access_tk = token['access_token']
# refresh_tk = token['refresh_token']

# # access_type = token['token_type']
# print(token)


#---------------- Make Request to Spotify API 
#format "Authorization: Bearer NgCXRK...MzYjw"


# header_auth = {"Authorization": f"Bearer {access_tk}"}

# request_url = "https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V"
# response = requests.get(url=request_url,headers=header_auth)
# response.raise_for_status()
# print(response.text)

#get authorized user account details 
# sp = spotipy.client.Spotify(auth=access_tk)

# AUTH_URL = 'https://accounts.spotify.com/api/token'

# auth_response = requests.post(AUTH_URL, { "grant_type": "client_credentials", "client_id": CLIENT_ID, "client_secret": CLIENT_SECRET, })
# auth_response_data = auth_response.json()

# access_token = auth_response_data["access_token"]
# print(auth_response.text)


#once authorized lets Create a brand new Playlist 
# playlist_end_point = f"https://api.spotify.com/v1/users/{ID}/playlists"


#make POST request creating brand new playlist 
# response = requests.post(url=playlist_end_point,data=new_playlist_data,headers=header_auth)
# response.raise_for_status()
# print(response.text)

