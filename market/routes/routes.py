from market import app
from flask import render_template, redirect, url_for, flash
from market.model.models import Item, User
from market.forms.form import RegisterForm, LoginForm
from market import db
from flask_login import login_user, logout_user, login_required


@app.route("/")
@app.route("/home")
def homePage():
    return render_template("home.html")


@app.route("/publicMarket")
# Decorator that checks if the user is logged in
@login_required
def marketPage():
    items = Item.query.all()
    return render_template('market.html', items=items)


'''
RegisterForm
Register new user and add to db
'''


@app.route("/register", methods=["GET", "POST"])
def registerPage():
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


'''
Check if a user with he provided email is in the database
if true than compare the passwords
'''


@app.route("/login", methods=["GET", "POST"])
def loginPage():
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


@app.route("/logout",)
def logoutPage():
    logout_user()
    flash("Logged out.", category="info")
    return redirect(url_for("homePage"))
