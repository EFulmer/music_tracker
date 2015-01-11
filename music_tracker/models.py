# -*- coding: utf-8 -*-
# music_tracker/models.py

from .music_tracker import db


class ArtistItem(db.Model):

    # Columns

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # user will be used later
    # user = db.Column(db.String(128))

    artist = db.Column(db.String(128))

    album = db.Column(db.String(128))

