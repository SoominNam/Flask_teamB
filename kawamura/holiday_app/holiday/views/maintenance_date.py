from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday.models.mst_holiday import Holiday
from holiday import db
from datetime import date,datetime

@app.route('/update_delete_entry', methods=['POST'])
def update_delete_entry():
    try:
        date = datetime.strptime(request.form['holiday'],'%Y-%m-%d')
    except ValueError:
        flash('error: 5桁はダメ')
        return render_template('input.html')

    if request.form["button"] == "insert":
        entry = Holiday(
            holi_date = date,
            holi_text = request.form['holiday_text']
        )
        db.session.add(entry)
        db.session.commit()
        flash('記事が登録されました')
        return render_template('result.html', entry=entry, result="登録") 
    if request.form["button"] == "delete":
        date_count = Holiday.query.filter_by(holi_date = date).count()
        print(type(date_count))
        print(date_count)
        if date_count == 0:
            flash(str(request.form['holiday'])+'は祝日マスタに登録されていません')
            return render_template('input.html')
        else:
            entry = Holiday.query.filter_by(holi_date= date).first()
            db.session.delete(entry)
            db.session.commit()
            flash('投稿が削除されました')
            return render_template('result.html', entry=entry, result="削除")
