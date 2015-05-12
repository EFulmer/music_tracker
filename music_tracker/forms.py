# music_tracker/forms.py
# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms.fields import BooleanField, DateTimeField, FieldList, \
        FormField, IntegerField, PasswordField, StringField, SubmitField, \
        TextField, PasswordField
from wtforms.validators import DataRequired, Email, Required


# shamelessly stolen from Explore Flask
class EmailPasswordForm(Form):
    email = TextField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])


# ditto
class UsernamePasswordForm(Form):
    username = TextField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])

class EmailForm(Form):
    email = TextField('Email', validators=[Required(), Email()])

class PasswordForm(Form):
    password = PasswordField('Password', validators=[Required()])

class EnterArtistForm(Form):
    artist = StringField('artist', validators=[DataRequired()])
    submit = SubmitField('Get Artist Info')


class AddArtistForm(Form):
    submit = SubmitField('Add {} To Your List')


# lifted from Explore Flask: https://exploreflask.com/forms.html
class EmailPasswordForm(Form):
    email    = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

