from market import app
from flask import render_template
from market.model.models import Item


@app.route("/")
@app.route("/home")
def homePage():
    return render_template("home.html")


@app.route("/publicMarket")
def marketPage():
    items = Item.query.all()
    return render_template('market.html', items=items)
