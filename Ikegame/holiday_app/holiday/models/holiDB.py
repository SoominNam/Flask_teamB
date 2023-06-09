from flask_sqlalchemy import SQLAlchemy
from holiday import app
from holiday import db

class Holiday(db.Model):
    __tablename__ = "holiday"
    holi_date = db.Column(db.Date,unique=True,primary_key=True)
    holi_text = db.Column(db.Text)

    def __init__(self,holi_date=None,holi_text=None):
        self.holi_date = holi_date
        self.holi_text = holi_text

    def __repr__(self):
        return '<Entry id:{}title:{}text:{}>'.format(self.id,self.title,self.text)