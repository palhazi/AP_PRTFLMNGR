from . import db # Az __init__.py modulból importáljuk a db változót.
from flask_login import UserMixin
from sqlalchemy.sql import func

# Definiáljuk a Note osztályt, amely a feljegyzéseket reprezentálja.
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# Definiáljuk a Note osztályt, amely a feljegyzéseket reprezentálja.
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    second_name = db.Column(db.String(150))
    notes = db.relationship('Note')

# Definiáljuk az Investment osztályt, amely a felhasználók befektetéseit reprezentálja.
class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asset_name = db.Column(db.String(150))
    asset_type = db.Column(db.String(150))
    purchase_date = db.Column(db.DateTime(timezone=True))
    purchase_price = db.Column(db.Float)
    quantity = db.Column(db.Float)
    current_price = db.Column(db.Float)
    expected_interest_amount = db.Column(db.Float)
    interest_payment_date = db.Column(db.DateTime(timezone=True))
    maturity_date = db.Column(db.DateTime(timezone=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    user = db.relationship('User', back_populates='investments')


# Hozzáadjuk az 'investments' attribútumot a User osztályhoz.
User.investments = db.relationship('Investment', back_populates='user')
