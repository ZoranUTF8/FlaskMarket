
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# create the app
app = Flask(__name__)
app.app_context().push()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
app.config["SECRET_KEY"] = "e4194bfabcb346ff60e510e4"
db = SQLAlchemy(app)


# with app.app_context():
#     db.create_all()
from market.routes import routes