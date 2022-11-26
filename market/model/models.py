from market import db, bcrypt, login_manager
# Includes method for flask login
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(30), nullable=False, unique=True)
    emailAddress = db.Column(db.String(50), nullable=False, unique=True)
    passwordHash = db.Column(db.String(60), nullable=False)
    budget = db.Column(db.Integer, nullable=False, default=1000)
    items = db.relationship("Item", backref="owned_user", lazy=True)

# User extra properties

    @property
    def format_user_budget(self):
        if len(str(self.budget)) >= 4:
            return f"{str(self.budget)[:-3]},{str(self.budget)[-3:]}$"
        else:
            return f"{self.budget}$"

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.passwordHash = bcrypt.generate_password_hash(
            plain_text_password).decode('utf-8')

    def check_password_match(self, password_to_test):
        return bcrypt.check_password_hash(self.passwordHash, password_to_test)

    def can_purchase(self, item_object):
        return self.budget >= item_object.price


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    barcode = db.Column(db.String(12), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return f"Item {self.name}"

    def sell_item(self, current_user):
        self.owner = current_user.id
        current_user.budget -= self.price
        db.session.commit()
