from game import db
from datetime import datetime

class Player(db.Model):
    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50), unique = True, nullable=False)
    name = db.Column(db.String(16), nullable=False)
    password = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime)
    score = db.relationship('Score', backref='player', lazy=True)

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return "<Entry id:{} title:{} text:{}>".format(self.id, self.name, self.email)