from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_wtf.file import FileField, FileAllowed
from compro.models import Users

class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegisterForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(), EqualTo('confirm_pass')])
    confirm_pass = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

class PhotoForm(FlaskForm):

    profile_photo = FileField('Profile Photo', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')
