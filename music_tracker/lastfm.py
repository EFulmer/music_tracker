# -*- coding: utf-8 -*-

# TODO poss. useful methods; get_cover_image, get_release_date, 
# get_url, get_wiki (on t[0].item; which is an Album object)

import pylast

from . import app


network = pylast.LastFMNetwork(api_key=app.config['API_KEY'], 
    api_secret=app.config['API_SECRET'])


def get_artist_info(artist):
    """
    Get a Pylast object representing the artist's top album.
    The object contains other relevant metadata (proper name, etc)
    """
    a = network.get_artist(artist)
    t = a.get_top_albums()
    return t[0].item
