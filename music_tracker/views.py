# music_tracker/views.py
# -*- coding: utf-8 -*-

import datetime

from flask import flash, render_template, redirect, request, url_for

import lastfm
from . import app, db
from .forms import AddArtistForm, EnterArtistForm
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
# TODO error check
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
        #return 'Error encountered'


@app.route('/my_artists/', methods=('GET',))
def manage_artists():
    # TODO remove dummy User.id
    # TODO get logged in user's id (User.id) 
    artists = UsersArtist.query.filter(UsersArtist.user == 1) \
                               .filter(UsersArtist.active).all()
    return render_template('manage_list.html', artists=artists)


@app.route('/my_artists/all/', methods=('GET',))
def all_artists():
    # TODO remove dummy User.id
    # TODO get logged in user's id (User.id)
    artists = UsersArtist.query.filter(UsersArtist.user == 1).all()
    return render_template('manage_list.html', artists=artists)


@app.route('/my_artists/archive/<int:artist_id>', methods=('GET', 'POST'))
def archive_artist(artist_id):
    artist = UsersArtist.query.get(artist_id)
    artist.active = False
    db.session.commit()
    flash('{} archived.'.format(artist.artist_name))
    return redirect(url_for('manage_artists'))


@app.route('/my_artists/unarchive/<int:artist_id>', methods=('GET', 'POST'))
def unarchive_artist(artist_id):
    artist = UsersArtist.query.get(artist_id)
    artist.active = True
    db.session.commit()
    flash('{} unarchived.'.format(artist.artist_name))
    return redirect(url_for('manage_artists'))

