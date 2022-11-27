from market.forms.form import PurchaseItemForm, SellItemForm
from market.model.models import Item, User
from flask import render_template, redirect, url_for, flash, request
from market import db
from flask_login import current_user


def marketPage():
    purchase_form = PurchaseItemForm()
    sellItem_form = SellItemForm()

    # Purchase item
    if request.method == "POST":

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

    # Render the items
    if request.method == "GET":
        items = Item.query.filter_by(owner=None)
        user_owned_items = Item.query.filter_by(owner=current_user.id)
        return render_template('market.html', items=items, purchase_form=purchase_form, user_owned_items=user_owned_items, sellItem_form=sellItem_form)
