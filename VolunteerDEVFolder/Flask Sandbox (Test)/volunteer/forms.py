from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, ValidationError, Regexp, EqualTo
from volunteer.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message="Username is required"),
    Regexp('([A-z]|[0-9]){5,20}',message="Username must be between 5 and 20 characters, and only contain letters and/or numbers.")])
    password = PasswordField('Password', validators=[DataRequired(message="Password is required"),
    Regexp('([A-z]|[0-9]){5,20}',message="Password must be between 5 and 20 characters, and only contain letters and/or numbers."),
    EqualTo('confirm_password',message="Passwords don't match. Try again.")])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(message="Please confirm your password"),
    Regexp('([A-z]|[0-9]){5,20}',message="Password must be between 5 and 20 characters, and only contain letters and/or numbers.")])
    email = StringField('Email')
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user is not None:
            raise ValidationError('Username has been taken. Please choose another.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message="Please enter a username"),
    Regexp('([A-z]|[0-9]){5,20}',message="Username must be between 5 and 20 characters, and only contain letters and/or numbers.")])
    password = PasswordField('Password', validators=[DataRequired(message="Please enter a password"),
    Regexp('([A-z]|[0-9]){5,20}',message="Password must be between 5 and 20 characters, and only contain letters and/or numbers.")])
    submit = SubmitField('Login')

