from flask_script import Command
from calorie import db
from calorie.models.calDB import Meal,MenuMaster

class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()