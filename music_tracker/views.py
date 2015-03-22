# music_tracker/views.py
# -*- coding: utf-8 -*-

import datetime

from flask import render_template, redirect, url_for

import lastfm
from . import app, db
from .forms import AddArtistForm, ArtistField, EnterArtistForm, ManageArtistsForm
from .models import ArtistInfo, User, UsersArtist


# TODO literally everything
@app.route('/')
def index():
    return 'under construction'


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

    #try:
    info = lastfm.get_artist_info(name)
    name = str(info['artist'])

    form.submit.label.text = form.submit.label.text.format(name)

    if form.validate_on_submit():
        # TODO dummy user id
        user_artist = UsersArtist(user=1, artist_name=name, 
                best_album=info['album'], best_song=info['track'],
                date_added=datetime.datetime.now(), active=True)
        db.session.add(user_artist)
        db.session.commit()
        return redirect(url_for('manage_artists'))

    return render_template('artist_info.html', form=form, info=info)
    #except:
        # TODO more info about errors (connection error?
        # artist doesn't exist?) and link back to add artist form.
        #return 'Error encountered in grabbing artist info'


# TODO everything
@app.route('/my_artists/', methods=('GET', 'POST'))
def manage_artists():
    # TODO remove dummy User.id
    # TODO get logged in user's id (User.id)
    # TODO new page to retrieve all artists, even inactive ones
    artists = UsersArtist.query.filter(UsersArtist.user == 1) \
                               .filter(UsersArtist.active).all()
    form = ManageArtistsForm()
    for artist in artists:
        entry.artist_name  = artist.artist_name
        entry.album        = artist.best_album
        entry.song         = artist.best_song
        entry.added        = artist.date_added
        entry.deactivate = False
        entry.delete = False
        form.artists.append_entry(entry)
    return render_template('manage_list.html', form=form)

