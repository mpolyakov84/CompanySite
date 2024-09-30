from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_wtf.file import FileField, FileAllowed

class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired])
    submit = SubmitField('Log In')

class RegisterForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(), EqualTo('confirm_pass')])
    confirm_pass = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

class UserForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    profile_photo = FileField('Profile Photo', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')
