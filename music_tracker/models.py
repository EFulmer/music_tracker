# music_tracker/models.py
# -*- coding: utf-8 -*-

from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # TODO login stuff; there are almost certainly Flask plugins for it

    def __repr__(self):
        return 'User: {}'.format(self.id)


# Not currently being used, purpose is to cache data from Last.fm
class ArtistInfo(db.Model):
    """Info about a musical artist."""
    id      = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name    = db.Column(db.String(128))
    album   = db.Column(db.String(128))
    track   = db.Column(db.String(128))
    bio     = db.Column(db.String(1024))
    youtube = db.Column(db.String(128))
    spotify = db.Column(db.String(128))
    lastfm  = db.Column(db.String(128))
    rym     = db.Column(db.String(128))

    def __repr__(self):
        return 'ArtistInfo: {} {} {} {} {} {} {} {} {}'.format(self.id,
                self.name, self.album.self.track, self.bio, self.youtube,
                self.spotify, self.lastfm, self.rym)


# TODO give this a less stupid name.
class UsersArtist(db.Model):
    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user        = db.Column(db.ForeignKey(User.id))
    artist_name = db.Column(db.String(128))
    best_album  = db.Column(db.String(128))
    best_song   = db.Column(db.String(128))
    date_added  = db.Column(db.DateTime)
    active      = db.Column(db.Boolean)

    def __repr__(self):
        return 'UsersArtist: {}'.format(self.artist_name)
        return 'UsersArtist: {} {} {} {} {} {} {}'.format(self.id, self.user,
                self.artist_name, self.best_album, self.best_song, 
                self.date_added, self.active)

