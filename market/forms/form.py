from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired


class RegisterForm(FlaskForm):
    userName = StringField(label="Username", validators=[
                           Length(min=2, max=30), DataRequired()])
    emailAddress = StringField(label="Email", validators=[
                               Email(), DataRequired()])
    passwordOne = PasswordField(
        label="Password", validators=[Length(min=8), DataRequired()])
    passwordTwo = PasswordField(
        label="Confirm Password", validators=[EqualTo("passwordOne"), DataRequired()])
    submit = SubmitField(label="Submit")
