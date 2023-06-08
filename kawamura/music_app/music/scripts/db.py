from flask_script import Command
from music import db
from music.models.database import Music

class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()