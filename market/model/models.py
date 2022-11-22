from market import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(30), nullable=False, unique=True)
    emailAddress = db.Column(db.String(50), nullable=False, unique=True)
    passwordHash = db.Column(db.String(60), nullable=False)
    budget = db.Column(db.Integer, nullable=False, default=1000)
    items = db.relationship("Item", backref="owned_user", lazy=True)

    


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    barcode = db.Column(db.String(12), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return f"Item {self.name}"
