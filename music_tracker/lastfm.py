# music_tracker/lastfm.py
# -*- coding: utf-8 -*-

import pylast

from . import app


network = pylast.LastFMNetwork(api_key=app.config['API_KEY'], 
    api_secret=app.config['API_SECRET'])


def get_artist_info(artist):
    """
    Get a Pylast object representing the artist's top album.
    The object contains other relevant metadata (proper name, etc)
    """
    info = {}
    a = network.get_artist(artist)
    album_data = a.get_top_albums()
    track_data = a.get_top_tracks()
    bio = a.get_bio('summary')
    info = { 'artist': track_data[0].item.artist, 
             'bio': bio, 
             'album': album_data[0].item.title, 
             'track': track_data[0].item.title,
             'url': a.get_url() }
    return info
