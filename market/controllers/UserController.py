from market.forms.form import RegisterForm, LoginForm, PurchaseItemForm
from market.model.models import Item, User
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user

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
