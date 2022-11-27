from market import app
from flask import render_template, redirect, url_for, flash, request
from market.model.models import Item, User
from market.forms.form import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm
from market import db
from flask_login import login_user, login_required, current_user
from market.controllers import UserController, itemController


@app.route("/")
@app.route("/home")
def homePage():
    return render_template("home.html")


@app.route("/publicMarket", methods=["GET", "POST"])
# Decorator that checks if the user is logged in
@login_required
def marketPage():
    purchase_form = PurchaseItemForm()
    sellItem_form = SellItemForm()
    '''
    Check if the method is post
    Retrieve the name of the item to be purchased from the form
    Query the Item database for the item
    Check if user has enough funds
    Assign the owner of the item to the current logged in user
    Remove the amount of the item from the users budget and flash message

    '''
    if request.method == "POST":
        # Purchase item
        purchased_item = request.form.get("purchased_item")
        p_item_object = Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.sell_item(current_user)
                flash(
                    f"Item {p_item_object.name} purchased for {p_item_object.price}", category="success")

            else:
                flash(
                    f"You do not have enough funds. Item price: {p_item_object.price}. Available funds: {current_user.budget}", category="danger")

        # Sell item
        selling_item = request.form.get("selling_item")
        s_item_object = Item.query.filter_by(name=selling_item).first()

        if s_item_object:
            if current_user.can_sell_item(s_item_object):
                s_item_object.resell(current_user)
                flash(
                    f"Item {s_item_object.name} sold for {s_item_object.price} $.", category="Success")
            else:
                flash(
                    f"Item {s_item_object.name} could not be sold.", category="danger")

        return redirect(url_for("marketPage"))
# Show only items with no owner and the user owned items
    if request.method == "GET":
        items = Item.query.filter_by(owner=None)
        user_owned_items = Item.query.filter_by(owner=current_user.id)
        return render_template('market.html', items=items, purchase_form=purchase_form, user_owned_items=user_owned_items, sellItem_form=sellItem_form)


'''
RegisterForm
Register new user and add to db
'''


@app.route("/register", methods=["GET", "POST"])
def registerPage():
    return UserController.registerUser()


'''
Check if a user with he provided email is in the database
if true than compare the passwords
'''


@app.route("/login", methods=["GET", "POST"])
def loginPage():
    return UserController.loginUser()


@app.route("/logout",)
def logoutPage():
    return UserController.logoutUser()
