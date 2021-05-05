from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

class Train(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.Integer())
    rate = db.Column(db.Float())
    classification = db.Column(db.String(150))
    quotes = db.relationship('Quote')

class Customer(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80))
    address_one = db.Column(db.String(150))
    address_two = db.Column(db.String(150))
    address_three = db.Column(db.String(150))
    postcode = db.Column(db.String(10))
    quotes = db.relationship('Quote')

class Quote(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    PLA = db.Column(db.String(150))
    cost = db.Column(db.Float())
    cust_id = db.Column(db.Integer(), db.ForeignKey('customer.id'))
    train_id = db.Column(db.Integer(), db.ForeignKey('train.id'))
    #user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    week = db.Column(db.Integer())
    year = db.Column(db.Integer())