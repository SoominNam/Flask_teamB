from flask_script import Command
from baseball import db
from baseball.models.players import Player

class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()