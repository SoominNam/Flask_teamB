from flask import request, redirect, url_for, render_template, session, flash
from holiday import app
from holiday import db
from holiday.models.mst_holiday  import Holiday
from datetime import datetime as date

@app.route('/maintenance_date', methods=['GET', 'POST'])
def maintenance():
    if request.method == "POST":
        if request.form["button"] == "insert_update":
            if request.form["holiday"] == "" or request.form["holiday_text"] == "":
                flash("日付またはテキストを入力してください")
                return redirect(url_for("input"))   
            else:
                input_date = date.strptime(request.form["holiday"], '%Y-%m-%d')
                holiday = Holiday.query.filter_by(holi_date=input_date).first()
                if holiday is None:
                    # 新規作成
                    new_holiday = Holiday (
                        holi_date= request.form["holiday"],
                        holi_text= request.form["holiday_text"]
                    )
                    db.session.add(new_holiday)
                    db.session.commit()
                    msg = request.form["holiday"] + "(" + request.form["holiday_text"] + ")が登録されました"
                else:
                    # 更新 
                    new_holiday = Holiday (holi_date = holiday.holi_date, holi_text= request.form["holiday_text"])
                    db.session.merge(new_holiday)
                    db.session.commit()
                    msg = request.form["holiday"] + "は「" + request.form["holiday_text"] + "」に更新されました"

                return render_template("result.html", msg = msg)
                    
        elif request.form["button"] == "delete":
            if request.form["holiday"] == "":
                flash("日付を入力してください")
                return redirect(url_for("input"))   
            else:
                input_date = date.strptime(request.form["holiday"], '%Y-%m-%d')
                holiday = Holiday.query.filter_by(holi_date=input_date).first()
                if holiday is None:
                    flash(request.form["holiday"] + "は、祝日マスタに登録されていません")
                    return redirect(url_for("input"))
                else:
                    db.session.delete(holiday)
                    db.session.commit()
                    msg = str(holiday.holi_date) + "(" + holiday.holi_text + ")は、削除されました"
                    return render_template("result.html", msg = msg)