from market.forms.form import RegisterForm, LoginForm
from market.model.models import User
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user
from market import db


def loginUser():
    form = LoginForm()
    # form validation
    if form.validate_on_submit():

        userToLogIn = User.query.filter_by(
            emailAddress=form.emailAddress.data).first()

        if userToLogIn and userToLogIn.check_password_match(password_to_test=form.password.data):
            flash(f"Welcome back: {userToLogIn.userName}", category="success")
            login_user(userToLogIn)
            return redirect(url_for("homePage"))
        else:
            flash(f"Check your input.", category="danger")

            # returned errors if any
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"There was an error. {err_msg}", category="danger")

    return render_template('login.html', form=form)


def logoutUser():
    logout_user()
    flash("Logged out.", category="info")
    return redirect(url_for("homePage"))


'''
Register the new user after
the register form has been submitted
and validated.
When completed login the user and redirect to homePage
If error than flash the error message

'''


def registerUser():
    form = RegisterForm()
    # form validation
    if form.validate_on_submit():
        user_to_create = User(userName=form.userName.data,
                              emailAddress=form.emailAddress.data,
                              password=form.passwordOne.data)

        db.session.add(user_to_create)
        db.session.commit()

        login_user(user_to_create)
        flash(
            f"Account created. You are now logged in as: {user_to_create.userName}", category="success")
        return redirect(url_for("homePage"))
    # returned errors if any
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"There was an error. {err_msg}", category="danger")

    return render_template("register.html", form=form)


def homePage():
    return render_template("home.html")
