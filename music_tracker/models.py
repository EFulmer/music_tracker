# -*- coding: utf-8 -*-
# music_tracker/models.py

from . import db


class ArtistInfo(db.Model):
    """Info about a musical artist."""
    id      = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name    = db.Column(db.String(128))
    album   = db.Column(db.String(128))
    track   = db.Column(db.String(128))
    bio     = db.Column(db.String(1024))
    yt      = db.Column(db.String(128))
    spotify = db.Column(db.String(128))
    lastfm  = db.Column(db.String(128))
    rym     = db.Column(db.String(128))


class UsersArtist(db.Model):
    id         = db.Column(db.ForeignKey('user.id'))
    artist     = db.Column(db.ForeignKey('artistInfo.id'))
    date_added = db.Column(db.DateTime)
    active     = db.Column(db.Boolean)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # TODO login stuff ...
