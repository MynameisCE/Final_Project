# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 12:35:46 2022

@author: omega
"""
#wassup
import spotipy 
import spotipy.util as util
#from spotipy.oauth2 import SpotifyOAuth


SPOTIPY_CLIENT_ID = "35fc3e9be25d4f4da6d71571455e7110"
SPOTIPY_CLIENT_SECRET = "6834ba5d6a14462ca652f81ae11adf17"
SPOTIPY_REDIRECT_URI = "https://www.google.com/"

user = "xxstorm-walkerxx"
token = util.prompt_for_user_token(user,
                                   scope=None,
                                   client_id=SPOTIPY_CLIENT_ID,
                                   client_secret=SPOTIPY_CLIENT_SECRET,
                                   redirect_uri=SPOTIPY_REDIRECT_URI)
spotifyObject = spotipy.Spotify(auth=token)


spotifyObject.user_playlist_create(user=user, name="RANDOM_PLAYLIST")


