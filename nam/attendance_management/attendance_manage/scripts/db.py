from flask_script import Command
from attendance_manage import db
from attendance_manage.models.attendance import Attendance
class InitDB(Command):
    "create datebase"

    def run(self):
        db.create_all()

