# music_tracker/views.py
# -*- coding: utf-8 -*-

import datetime

from flask import render_template, redirect, url_for

import lastfm
from . import app, db
from .forms import AddArtistForm, EnterArtistForm
from .models import ArtistInfo, User, UsersArtist


@app.route('/')
def index():
    return 'hello'


# TODO login check
@app.route('/add/', methods=('GET', 'POST'))
def find_artist():
    # TODO errors if not valid
    form = EnterArtistForm()
    if form.validate_on_submit():
        return redirect('/artist/' + form.artist.raw_data[0])
    return render_template('add.html', form=form)


# TODO login check
@app.route('/artist/<string:artist>', methods=('GET', 'POST'))
def artist_info(artist):
    form = AddArtistForm()
    name = artist.replace('_', ' ')
    # TODO check for artist in db before doing this
    info = lastfm.get_artist_info(name)
    form.submit.label.text = form.submit.label.text.format(name)

    artist_info = ArtistInfo(name=str(info['artist']), album=info['album'], 
            track=info['track'], bio=info['bio'], youtube='DUMMY', 
            spotify='DUMMY', lastfm='DUMMY', rym='DUMMY')

    if form.validate_on_submit():
        user_artist = UsersArtist(user=1, artist=artist_info.id, 
                date_added=datetime.datetime.now(), active=True)
        db.session.add(artist_info)
        db.session.add(user_artist)
        db.session.commit()
        # TODO redirect to list manage page
        return 'success'

    return render_template('artist_info.html', form=form, info=info)


# TODO everything
@app.route('/my_artists/', methods=('GET', 'POST'))
def manage_artists():
    pass
