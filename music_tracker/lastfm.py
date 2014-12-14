# -*- coding: utf-8 -*-

# TODO poss. useful methods; get_cover_image, get_release_date, 
# get_url, get_wiki (on t[0].item; which is an Album object)

import pylast

import lastfmcfg


network = pylast.LastFMNetwork(api_key=lastfmcfg.API_KEY, 
    api_secret=lastfmcfg.API_SECRET)


def get_top_album(artist):
    """
    Get the title of artist's top album. Throws pylast.WSError if 
    artist is not found.
    """
    a = network.get_artist(artist)
    t = a.get_top_albums()
    return t[0].item.title


def get_top_track(artist):
    """
    Get the title of artist's top track. Throws pylast.WSError if 
    artist is not found.
    """
    a = network.get_artist(artist)
    t = a.get_top_tracks()
    return t[0].item.title
