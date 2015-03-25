# music_tracker/forms.py
# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms.fields import BooleanField, DateTimeField, FieldList, \
        FormField, IntegerField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email


class EnterArtistForm(Form):
    artist = StringField('artist', validators=[DataRequired()])
    submit = SubmitField('Get Artist Info')


class AddArtistForm(Form):
    submit = SubmitField('Add {} To Your List')


# lifted from Explore Flask: https://exploreflask.com/forms.html
class EmailPasswordForm(Form):
    email    = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


# TODO remove superfluous form.
class ArtistInfoForm(Form):
    submit = SubmitField('Track Artist')


# TODO remove superfluous form.
class ManageArtistsForm(Form):
    submit = SubmitField('Update')

