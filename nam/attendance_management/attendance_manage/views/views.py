from flask import request, redirect, url_for, render_template, flash, session
from attendance_manage import app
from attendance_manage import db
from attendance_manage.models.attendance import Attendance


@app.route('/', methods=['GET', 'POST'])
def input():
    if request.method == "POST":
        staff_num = request.form["staff_num"]
        name = request.form["name"]
        start_time = request.form["start_time"]
        end_time = request.form["end_time"]
        text = request.form["text"]
        db.session.add(Attendance(staff_num=staff_num,name=name, start_time=start_time, end_time=end_time, text=text))
        db.session.commit()
    attendancelist = Attendance.query.order_by(Attendance.date.desc()).all()
    return render_template('index.html', attendancelist = attendancelist)
