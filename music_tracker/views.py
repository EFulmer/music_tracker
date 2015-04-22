# music_tracker/views.py
# -*- coding: utf-8 -*-

import datetime

from flask import abort, flash, render_template, redirect, request, url_for
from flask.ext.login import current_user, login_required, login_user
from flask.ext.mail import Message
from sqlalchemy.exc import IntegrityError

import lastfm
from . import app, db, load_user, mail
from .forms import AddArtistForm, EmailForm, EmailPasswordForm, \
        EnterArtistForm, PasswordForm
from .models import ArtistInfo, User, UsersArtist
from .util import ts


@app.route('/')
def index():
    return render_template('index.html')


# shamelessly stolen from Explore Flask
@app.route('/register/', methods=('GET', 'POST',))
def register():
    form = EmailPasswordForm()
    if form.validate_on_submit():
        email = form.email.data.lower()
        try:
            user = User(email=email, password=form.password.data)
            db.session.add(user)
            db.session.commit()
            token = ts.dumps(form.email.data, salt='email-confirm-key')
            confirm_url = url_for('confirm_email', token=token, 
                    _external=True)
            html = render_template('email/activate.html', 
                    confirm_url=confirm_url)

            msg = Message(subject='Confirm your email', recipients=[email,], 
                    html=html, sender='ericsmusictracker@gmail.com')
            mail.send(msg)

            flash('Account created! Check your email for a confirmation ' \
                    'message to activate your account.')
            return redirect(url_for('login'))
        except:
            db.session.rollback()
            flash('There is already an email account for {}.'.format(email))

    return render_template('register.html', form=form)


# also shamelessly stolen from Explore Flask
@app.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = ts.loads(token, salt='email-confirm-key', max_age=86400)
    except:
        abort(404)

    user = User.query.filter_by(email=email).first_or_404()
    user.email_confirmed = True

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/login/', methods=('GET', 'POST'))
def login():
    form = EmailPasswordForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()) \
                   .first_or_404()

        if user.is_correct_password(form.password.data):
            login_user(user)

            flash("You've been logged in!")
            return redirect(url_for('index'))
        else:
            flash("Sorry, but your password was incorrect.")
            return redirect(url_for('login'))

    return render_template('login.html', form=form)


@app.route('/reset/', methods=('GET', 'POST'))
def reset_password():
    form = EmailForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first_or_404()
        
        subject = 'Password reset requested'
        token = ts.dumps(form.email.data, salt='recover-key')
        recover_url = url_for('reset_with_token', token=token, _external=True)
        html = render_template('email/recover.html', recover_url=recover_url)
        send_email(user.email, subject, html)

        return redirect(url_for('index'))

    return render_template('reset.html', form=form)


@app.route('/reset/<token>', methods=('GET', 'POST',))
def reset_wth_token(token):
    try:
        email = ts.loads(token, salt='recover-key', max_age=86400)
    except:
        abort(404)

    form = PasswordForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=email).first_or_404()
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('signin'))

    return render_template('reset_with_token.html', form=form, token=token)


@app.route('/logout/')
@login_required
def logout():
    logout_user()
    flash("You've been logged out.")
    return redirect(url_for('index'))


@app.route('/add/', methods=('GET', 'POST'))
@login_required
def find_artist():
    print current_user.is_authenticated()
    form = EnterArtistForm()
    if form.validate_on_submit():
        return redirect('/artist/' + form.artist.raw_data[0])
    return render_template('add.html', form=form)


@app.route('/artist/<string:artist>', methods=('GET', 'POST'))
@login_required
def artist_info(artist):
    form = AddArtistForm()
    name = artist.replace('_', ' ')

    info = lastfm.get_artist_info(name)
    name = str(info['artist'])

    form.submit.label.text = form.submit.label.text.format(name)

    if form.validate_on_submit():
        user_artist = UsersArtist(user=current_user.id, artist_name=name, 
                best_album=info['album'], best_song=info['track'],
                date_added=datetime.datetime.now(), active=True)
        db.session.add(user_artist)
        db.session.commit()
        return redirect(url_for('manage_artists'))

    return render_template('artist_info.html', form=form, info=info)


@app.route('/my_artists/', methods=('GET',))
@login_required
def manage_artists():
    artists = UsersArtist.query.filter(UsersArtist.user == current_user.id) \
                               .filter(UsersArtist.active).all()
    return render_template('manage_list.html', artists=artists)


@app.route('/my_artists/all/', methods=('GET',))
@login_required
def all_artists():
    artists = UsersArtist.query.filter(UsersArtist.user == current_user.id)\
                               .all()
    return render_template('manage_list.html', artists=artists)


@app.route('/my_artists/archive/<int:artist_id>', methods=('GET', 'POST'))
@login_required
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

