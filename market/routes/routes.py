from market import app
from flask import render_template, redirect, url_for, flash
from market.model.models import Item, User
from market.forms.form import RegisterForm
from market import db


@app.route("/")
@app.route("/home")
def homePage():
    return render_template("home.html")


@app.route("/publicMarket")
def marketPage():
    items = Item.query.all()
    return render_template('market.html', items=items)


@app.route("/register", methods=["GET", "POST"])
def registerPage():
    form = RegisterForm()
    # form validation
    if form.validate_on_submit():
        user_to_create = User(userName=form.userName.data,
                              emailAddress=form.emailAddress.data,
                              passwordHash=form.passwordOne.data)

        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for("homePage"))
    # returned errors if any
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"There was an error. {err_msg}")

    return render_template("register.html", form=form)
