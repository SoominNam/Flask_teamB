from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday  import Holiday

@app.route("/list", methods=["GET", "POST"])
def show_list():
    holidaylist = Holiday.query.order_by(Holiday.holi_date.asc()).all()
    return render_template('list.html', holidaylist = holidaylist)