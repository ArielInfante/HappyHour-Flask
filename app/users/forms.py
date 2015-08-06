from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField, TextAreaField
from wtforms.validators import InputRequired, EqualTo, Optional, Length, Email, Regexp
# from flask.ext.login import current_user
from wtforms import ValidationError
from .models import User
from flask import redirect, url_for


class SignUpForm(Form):
    username = StringField('Username', validators=[
        InputRequired(message="Username is required"),
        Regexp('^[A-Za-z][A-Za-z0-9_]*[A-Za-z0-9]$', 0, "Usernames must only have letters, numbers or underscores")
    ])
    name = StringField('Name', validators=[
        InputRequired(message="Name id required"),
        Regexp('^[A-Za-z][A-Za-z ]*[A-Za-z]$', 0, "Your name must only have letters")
    ])
    email = StringField('Email', validators=[
        InputRequired(message="Email is required"),
        Email(message="This is not a valid email")
    ])
    password = PasswordField('Password', validators=[
        InputRequired(message="Password is required"),
        Length(min=6, message="The password is not long enough")
    ])
    accept_tos = BooleanField("Accept Terms of Service", validators=[
        InputRequired(message="You have to accept the Terms of Service in order to use this site")
    ], default=False)
    submit = SubmitField('Signup')


class LoginForm(Form):
    username_email = StringField('Username or Email', validators=[
        InputRequired(message="Need to insert either username or email")
    ])
    password = PasswordField('Password', validators=[
        InputRequired(message="Insert your password")
    ])
    remember_me = BooleanField('Keep me logged in', default=False)
    submit = SubmitField('Login')


class EditProfileForm(Form):
    privacy_option = RadioField('Private Account', validators=[
        InputRequired(message="Need to have an option chosen")
    ], choices=[
        (True, "Yes"), (False, "No")
    ], default=True)
    name = StringField('Name', validators=[
        InputRequired(message="Name id required"),
        Regexp('^[A-Za-z][A-Za-z]*[A-Za-z]$', 0, "Your name must only have letters")
    ])
    username = StringField('Username', validators=[
        InputRequired(message="Username is required"),
        Regexp('^[A-Za-z][A-Za-z0-9_]*[A-Za-z0-9]$', 0, "Usernames must only have letters, numbers or underscores")
    ])
    email = StringField('Email', validators=[
        InputRequired(message="Email is required"),
        Email(message="This is not a valid email")
    ])
    password = PasswordField('Password', validators=[
        InputRequired(message="Password is required"),
        Length(min=6, message="The password is not long enough")
    ])
    bio = TextAreaField("Bio")
    submit = SubmitField('Save Changes')


class ChangePasswordForm(Form):
    submit = SubmitField('Change Password')


class ChangeEmailForm(Form):
    change_email = StringField('New Email', validators=[
        InputRequired(message="You need to insert a new email"),
        Email(message="This is not a valid email")
    ])
    submit = SubmitField('Change Email')


class ChangeUsernameForm(Form):
    submit = SubmitField('Change Username')

