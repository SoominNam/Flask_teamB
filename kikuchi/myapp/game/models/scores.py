from game import db
from datetime import datetime

class Score(db.Model):
    __tablename__ = "scores"
    id = db.Column(db.Integer, primary_key = True)
    score = db.Column(db.Integer, unique = True, nullable=False)
    playerid = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    created_at = db.Column(db.DateTime)

    def __init__(self, score=None, playerid=None):
        self.score = score
        self.playerid = playerid
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return "<Entry id:{} title:{} text:{}>".format(self.id, self.title, self.text)