# music_tracker/lastfm.py
# -*- coding: utf-8 -*-

import pylast

from . import app


network = pylast.LastFMNetwork(api_key=app.config['API_KEY'], 
    api_secret=app.config['API_SECRET'])


def get_artist_info(artist):
    """
    Get a dict containing the name of artist's top album and other 
    relevant metadata (proper name, etc.).
    """
    info = {}
    a = network.get_artist(artist)
    album_data = a.get_top_albums()
    track_data = a.get_top_tracks()
    bio = a.get_bio('summary')
    bio = bio[:bio.find('<a href=')].strip()
    info = { 'artist': track_data[0].item.artist, 
             'bio': bio, 
             'album': album_data[0].item.title, 
             'track': track_data[0].item.title,
             'url': a.get_url(),
             'pic': a.get_cover_image(), 
           }
    return info
