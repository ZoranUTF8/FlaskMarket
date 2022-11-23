from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class RegisterForm(FlaskForm):
    userName = StringField(label="Username")
    emailAddress = StringField(label="Email")
    passwordOne = PasswordField(label="Password")
    passwordTwo = PasswordField(label="Repeat Password")
    submit = SubmitField(label="Submit")
