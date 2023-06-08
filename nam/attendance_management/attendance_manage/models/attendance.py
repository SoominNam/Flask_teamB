from attendance_manage import db
from datetime import datetime

class Attendance(db.Model):
    __tablename__ = 'attendance'
    staff_num = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    start_time = db.Column(db.String(50))
    end_time = db.Column(db.String(50))
    date = db.Column(db.DateTime)
    text = db.Column(db.Text)

    def __init__(self, staff_num=None, name=None, text=None, start_time = None, end_time = None):
        self.staff_num = staff_num
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.date = datetime.utcnow()
        self.text = text

    def __repr__(self):
        return '<Attendance staff_num:{} name:{} start_time:{} end_time:{} text:{}>'.format(self.staff_num, self.name, self.start_time, self.end_time, self.text)
    
