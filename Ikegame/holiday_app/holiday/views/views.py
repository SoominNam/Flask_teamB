from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from functools import wraps
from holiday.models.holiDB import Holiday
from holiday import db
from datetime import date

class DBError(Exception):
    pass

# argsは[holidate,holitext]
errors = {
    "W01":lambda **kwargs:"{date}は、祝日マスタに登録されていません".format(**kwargs),
    "W02":lambda **kwargs:"日付形式で入力してください".format(**kwargs),
    "W03":lambda **kwargs:"{date}は、有効な日付ではありません".format(**kwargs),
    "W04":lambda **kwargs:"テキストは20文字以内で入力してください".format(**kwargs),
    "W05":lambda **kwargs:"{date}{text}はすでに登録されています。".format(**kwargs)
}

messages = {
    "I01":lambda **kwargs:"{date}({text})が登録されました".format(**kwargs),
    "I02":lambda **kwargs:"{date}は「{text}」に変更されました".format(**kwargs),
    "I03":lambda **kwargs:"{date}({text})は削除されました".format(**kwargs),
    "I04":lambda **kwargs:"祝日マスタが登録されていません".format(**kwargs)
}

def check_input(holi_date=None,holi_text=None):
    """
    mode = 0:新規、更新
    mode = 1:削除
    エラーが発生したら: raise

    """
    try:
        dt = holi_date
        tx = holi_text

        #入力チェック
        #テキストの長さ
        if len(tx) > 20:
            raise DBError(errors["W04"](date=dt, text=tx))
        
        #日付チェック

        date(*list(map(lambda x:int(x),dt.split("-"))))
    except:
        raise DBError(errors["W02"](date=dt, text=tx))


def insert_record(dt,tx):
    holiday = Holiday(
        holi_date=dt,
        holi_text=tx
    )
    db.session.add(holiday)
    db.session.commit()

    return    

def update_record(dt,tx):
    holiday = Holiday.query.filter_by(holi_date=dt).first()
    holiday.holi_text=tx
    db.session.merge(holiday)
    db.session.commit()
    return

# insertとupdateが同じボタンなのでそれをまとめた関数
def insert_update(dt,tx):
    """メッセージをかえす"""
    holiday = Holiday.query.filter_by(holi_date=dt).first()
    # 変更の場合
    if holiday:
        if Holiday.query.get(dt).holi_text == tx:
            return errors["W05"](date=dt,text=tx)
        update_record(dt,tx)
        message = messages["I02"](date=dt, text=tx)
        
    # 挿入の場合
    else:
        insert_record(dt,tx)
        message = messages["I01"](date=dt, text=tx)

    return message

def delete_record(dt,tx):
    holiday = Holiday.query.get(dt)
    db.session.delete(holiday)
    db.session.commit()
    return messages["I03"](date=dt,text=tx)

@app.route("/",methods=["GET","POST"])
def input_():
    if request.method == 'POST':
        if request.form["button"] == "insert_update":
            dt = request.form["holi_date"]
            tx = request.form["holi_text"]

            try:
                check_input(holi_date=dt,holi_text=tx)
            except DBError as e:
                flash(e)
                return render_template("input.html")

            dt = date(*list(map(lambda x:int(x),dt.split("-"))))
            flash(insert_update(dt,tx))

        if request.form["button"] == "delete":
            dt = request.form["holi_date"]
            try:
                check_input(dt)
            except DBError as e:
                flash(e)
                return render_template("input.html")

            dt = date(*list(map(lambda x:int(x),dt.split("-"))))

            if Holiday.query.get(dt):
                flash(delete_record(dt,Holiday.query.get(dt).holi_text))
            else:
                flash(errors["W01"](date=dt))

        return render_template("result.html")
        
    return render_template("input.html")

@app.route("/list",methods=["GET","POST"])
def show_records():
    if request.method == 'POST':
        records = Holiday.query.order_by().all()
        return render_template("show_all.html",records=records)