from flask_sqlalchemy import SQLAlchemy
from calorie import app
from calorie import db

class MenuMaster(db.Model):
    __tablename__ = "menumaster"
    menu_id = db.Column(db.Integer,unique=True,primary_key=True,autoincrement=True)
    name = db.Column(db.Text)
    calorie = db.Column(db.Float)
    price = db.Column(db.Integer)

    def __init__(self,menu_id=None,name=None,calorie=None,price=None):
        self.menu_id = menu_id
        self.name = name
        self.calorie = calorie
        self.price = price

class Meal(db.Model):
    __tablename__ = "meal"
    meal_id = db.Column(db.Integer,unique=True,primary_key=True)
    menu_id = db.Column(db.Integer,db.ForeignKey("menumaster.menu_id"))
    date = db.Column(db.Date,primary_key=True)

    def __init__(self,meal_id=None, menu_id=None, date=None):
        self.meal_id = meal_id
        self.menu_id = menu_id
        self.date = date

    