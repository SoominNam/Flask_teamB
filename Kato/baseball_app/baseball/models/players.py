from baseball import db
from datetime import datetime

class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    number = db.Column(db.String(3))
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    def __init__(self, name=None, number=None, text=None):
        self.name = name
        self.number = number
        self.text = text
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<Player id:{} name:{} number:{} text:{}>'.format(self.id, self.name, self.number, self.text)