from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday.models.mst_holiday import Holiday

@app.route('/templates/list')
def show_entries():
    entries =Holiday.query.order_by(Holiday.holi_date.desc()).all()
    return render_template('list.html', entries = entries)