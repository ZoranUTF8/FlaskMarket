from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# create the app
app = Flask(__name__)
app.app_context().push()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"

db = SQLAlchemy(app)


# with app.app_context():
#     db.create_all()

from market.routes import routes
