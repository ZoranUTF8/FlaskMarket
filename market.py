from flask import Flask, render_template
from utils.marketPageData import items
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
app.app_context().push()
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)

# Data model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    barcode = db.Column(db.String(12), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    date_created = db.Column(db .DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Item {self.name}"


with app.app_context():
    db.create_all()


@app.route("/")
@app.route("/home")
def homePage():
    return render_template("home.html")


@app.route("/publicMarket")
def marketPage():
    return render_template("market.html", items=Item.query.all())
