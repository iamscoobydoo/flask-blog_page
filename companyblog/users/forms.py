from flask.app import Flask
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed # to use/update profile pictures
from wtforms import *
from wtforms.validators import DataRequired, Email, EqualTo
from flask_login import current_user
from companyblog.models import User

class LoginForm(FlaskForm):
    email = StringField('Email: ', validators = [DataRequired(), Email()])
    password = PasswordField('Password: ', validators = [DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email = StringField('Email: ', validators = [DataRequired(), Email()])
    username = StringField('Username: ', validators = [DataRequired()])
    password = PasswordField('Password: ', validators = [DataRequired(), EqualTo('pass_confirm', message = 'Passwords must match!')])
    pass_confirm = PasswordField('Re-Enter Password:', validators = [DataRequired()])
    submit = SubmitField('Register!')

    def check_email(self, email):
        if User.query.filter_by(email = self.email.data).first():
            raise ValidationError('This E-mail has already been regisered with us!')
    
    def check_username(self, username):
        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError('The provided username is in use!')

class UpdateUserForm(FlaskForm):
    email = StringField('Email: ', validators = [DataRequired(), Email()])
    username = StringField('Username: ', validators = [DataRequired()])
    picture = FileField('Update profile picture: ', validators = [FileAllowed(['jpg', 'png', 'bmp'])])
    submit = SubmitField('Update Profile')
    
    def check_email(self, email):
        if User.query.filter_by(email = self.email.data).first():
            raise ValidationError('This E-mail has already been regisered with us!')
    
    def check_username(self, username):
        if User.query.filter_by(username = self.username.data).first():
            raise ValidationError('The provided username is in use!')