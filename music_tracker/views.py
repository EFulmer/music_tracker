# music_tracker/views.py
# -*- coding: utf-8 -*-
from flask import render_template, redirect, url_for

import lastfm
from . import app
from .forms import EnterArtistForm


@app.route('/')
def index():
    return 'hello'


@app.route('/add/', methods=('GET', 'POST'))
def add_artist():
    # TODO errors if not valid
    form = EnterArtistForm()
    if form.validate_on_submit():
        return redirect('/artist/' + form.artist.raw_data[0])
    return render_template('add.html', form=form)


@app.route('/artist/<string:artist>')
def artist_info(artist):
    info = lastfm.get_artist_info(artist.replace('_', ' '))
    return render_template('artist_info.html', info=info)
