from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday
from datetime import datetime

@app.route("/maintenance_date", methods=["GET","POST"])
def deal():
    if request.method == "POST":
        if not request.form["code"] or not request.form["holiday"]:
            flash("値を入力してください。")
            return redirect(url_for("input"))
        
        else:
            holi_date = request.form["holiday"]
            holi_text = request.form["holiday_text"].strip()
            try:
                holi_date = datetime.strptime(request.form["holiday"], "%Y-%m-%d").date()
            except:
                flash("日付が無効な値です。")
                return redirect(url_for("input"))
            
            message = "処理に失敗しました"
            
            if request.form["code"] == "CreateUpdate":
                if not holi_text:
                    flash("祝日テキストを入力してください。")
                    return redirect(url_for("input"))
                
                else:
                    holiday = Holiday.query.get(holi_date)
                    if holiday:
                        holiday.holi_text = holi_text
                        db.session.merge(holiday)
                        message = f"{(holiday.holi_date.strftime('%Y-%m-%d'))}は「{holiday.holi_text}」に更新されました"

                    else:
                        holiday = Holiday(
                            holi_date=holi_date,
                            holi_text=holi_text
                        )
                        db.session.add(holiday)
                        message = f"{(holiday.holi_date.strftime('%Y-%m-%d'))}  ({holiday.holi_text})  が登録されました"
                    db.session.commit()

            elif request.form["code"] == "Delete":
                holiday = Holiday.query.get(holi_date)
                if holiday:
                    db.session.delete(holiday)
                    message = f"{(holiday.holi_date.strftime('%Y-%m-%d'))}  ({holiday.holi_text})  は、削除されました"
                else:
                    flash(f"{(holi_date.strftime('%Y-%m-%d'))}は、祝日マスタに登録されていません")
                    return redirect(url_for("input"))
                db.session.commit()
            return render_template("result.html", message=message)
    return redirect(url_for("input"))


