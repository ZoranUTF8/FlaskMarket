from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.model.models import User


class RegisterForm(FlaskForm):

    # Check if a user with the same username exists
    def validate_userName(self, usernameToCheck):
        user = User.query.filter_by(
            userName=usernameToCheck.data).first()
        if user:
            raise ValidationError(
                "Username already in use. Please choose a new username.")
    # Check if a user with the same email exists

    def validate_emailAddress(self, emailToCheck):
        user = User.query.filter_by(
            emailAddress=emailToCheck.data).first()
        if user:
            raise ValidationError(
                "Email already in use. Please choose a new email")


# Create form fields
    userName = StringField(label="Username", validators=[
                           Length(min=2, max=30), DataRequired()])
    emailAddress = StringField(label="Email", validators=[
                               Email(), DataRequired()])
    passwordOne = PasswordField(
        label="Password", validators=[Length(min=8), DataRequired()])
    passwordTwo = PasswordField(
        label="Confirm Password", validators=[EqualTo("passwordOne"), DataRequired()])
    submit = SubmitField(label="Submit")
