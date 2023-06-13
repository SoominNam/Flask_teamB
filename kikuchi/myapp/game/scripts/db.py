from flask_script import Command
from game import db
from game.models.players import Player
from game.models.scores import Score

class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()
        