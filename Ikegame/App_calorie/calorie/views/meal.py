from flask import request, redirect, url_for, render_template, flash, session
from calorie import app,db
from calorie.models.calDB import Meal,MenuMaster
from functools import wraps
import datetime

@app.route("/add",methods=["POST"])
def add_meal():
    if request.method=="POST":
        if request.form["button"] == "take":
            menu_name = request.form["meal"]

            today = datetime.date.today()
            meal_id = 0
            meal_id += len(Meal.query.filter_by(date=today).all())

            menu_id = MenuMaster.query.filter_by(name=menu_name).first().menu_id
            
            meal = Meal(
                meal_id=meal_id,
                menu_id=menu_id,
                date = today
            )

            db.session.add(meal)
            db.session.commit()
        return redirect(url_for("index"))
    return redirect(url_for("input_"))

@app.route("/history")
def history():
    history = db.session.query(
    Meal.date,
    MenuMaster.name,
    MenuMaster.calorie,
    MenuMaster.price,
    Meal.meal_id
    ).join(MenuMaster, Meal.menu_id == MenuMaster.menu_id).all()

    return render_template("history.html",history=history)

@app.route("/delete", methods=["POST"])
def delete_meal():
    # 文字列として返ってきてしまうのでプログラムとして実行
    dt,id_ = eval(request.form.get("button"))
    meal = Meal.query.filter_by(date=dt,meal_id=id_).first()
    db.session.delete(meal)
    db.session.commit()
    return redirect(url_for("history"))
