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
    is_approved = db.Column(db.Boolean, default=False)
    investments = db.relationship('Investment', back_populates='user', cascade='save-update, merge, refresh-expire')

# Definiáljuk az Investment osztályt, amely a felhasználók befektetéseit reprezentálja.
class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asset_name = db.Column(db.String(150))
    asset_type = db.Column(db.String(150))
    purchase_date = db.Column(db.DateTime(timezone=True))
    purchase_price = db.Column(db.Float, nullable=True)
    quantity = db.Column(db.Float,nullable=True)
    current_price = db.Column(db.Float, nullable=True)
    expected_interest_amount = db.Column(db.Float, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='SET NULL'), nullable=False)
    asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'), nullable=False)
    asset = db.relationship('Asset')
    asset = db.relationship('Asset', back_populates='investments')
    user = db.relationship('User', back_populates='investments', passive_deletes=True)
    snapshots = db.relationship('InvestmentSnapshot', back_populates='investment')


# Definiáljuk az InvestmentSnapshot osztályt, amely a felhasználók befektetéseinek mentett pillanatképét tartalmazza
class InvestmentSnapshot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    investment_id = db.Column(db.Integer, db.ForeignKey('investment.id'))
    snapshot_date = db.Column(db.DateTime(timezone=True), default=db.func.now())
    purchase_price = db.Column(db.Float, nullable=True)
    quantity = db.Column(db.Float, nullable=True)
    current_price = db.Column(db.Float, nullable=True)
    expected_interest_amount = db.Column(db.Float, nullable=True)
    snapshot_group_id = db.Column(db.Integer)

    investment = db.relationship('Investment', back_populates='snapshots')

# Definiáljuk az Asset osztályt, amely a befektetések adatait reprezentálja.

class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    long_name = db.Column(db.String(250), nullable=True)
    type = db.Column(db.String(100), nullable=False)
    interest_payment_date = db.Column(db.Date, nullable=True)
    maturity_date = db.Column(db.Date, nullable=True)
    description = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(100), nullable=True)
    link = db.Column(db.String(200), nullable=True)
    costs = db.Column(db.Float, nullable=True)
    investments = db.relationship('Investment', back_populates='asset')
