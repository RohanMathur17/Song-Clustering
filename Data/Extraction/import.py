import spotipy
import spotipy.util as util
from spotipy import oauth2
import pandas as pd

client_id     = 'XXX'
client_secret = 'XXX'


token       = oauth2.SpotifyClientCredentials(client_id = client_id , client_secret = client_secret)
cache_token = token.get_access_token()
sp          = spotipy.Spotify(cache_token)

username    = 'XXX'
playlist_id = 'XXX'

def get_playlist_tracks(username,playlist_id):

    results = sp.user_playlist_tracks(username,playlist_id)
    tracks  = results['items']
    while results['next']:

        results = sp.next(results)
        tracks.extend(results['items'])

    return tracks

def analyze_playlist(creator, playlist_id):
    
    # Create empty dataframe
    playlist_features_list = ["artist","album","track_name",  "track_id","acousticness",
                              "danceability","energy","key","loudness","mode", "speechiness","instrumentalness",
                              "liveness","valence","tempo", "duration_ms","time_signature"]
    
    playlist_df = pd.DataFrame(columns = playlist_features_list)
    
    # Loop through every track in the playlist, extract features and append the features to the playlist df
    
    
    for track in tracks:
    	
        # Create empty dict
        playlist_features = {}
        # Get metadata
        playlist_features["artist"] = track["track"]["album"]["artists"][0]["name"]
        playlist_features["album"] = track["track"]["album"]["name"]
        playlist_features["track_name"] = track["track"]["name"]
        playlist_features["track_id"] = track["track"]["id"]
        
        # Get audio features
        audio_features = sp.audio_features(playlist_features["track_id"])[0]

        for feature in playlist_features_list[4:]:

            playlist_features[feature] = audio_features[feature]
        
        # Concat the dfs
        track_df = pd.DataFrame(playlist_features, index = [0])
        playlist_df = pd.concat([playlist_df, track_df], ignore_index = True)
        
    return playlist_df

tracks=get_playlist_tracks(username,playlist_id)

new_df=analyze_playlist(username,playlist_id)

new_df.to_csv('Country.csv' , index = False)