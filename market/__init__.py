
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# Login manager
from flask_login import LoginManager
# create the app

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///marketDatabase.db"
app.config["SECRET_KEY"] = "e4194bfabcb346ff60e510e4"
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

with app.app_context():
    db.create_all()



from market.routes import routes