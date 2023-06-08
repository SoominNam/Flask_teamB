from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday

@app.route("/list")
def show_list():
    holidays = Holiday.query.order_by(Holiday.holi_date.asc()).all()
    if len(holidays) == 0:
        flash("登録されている祝日はありません。")
    return render_template("list.html", holidays=holidays)
