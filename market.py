from flask import Flask, render_template

from utils.marketPageData import items

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def homePage():
    return render_template("home.html")


@app.route("/publicMarket")
def marketPage():
    return render_template("market.html", items=items)
