from flask import request, redirect, url_for, render_template, flash, session
from calorie import app,db
from calorie.models.calDB import Meal,MenuMaster
from functools import wraps
import datetime

@app.route("/")
def index():
    today = Meal.query.filter_by(date=datetime.date.today()).all()
    calorie_today = sum(list(map(lambda x:MenuMaster.query.filter_by(menu_id=x.menu_id).first().calorie, today)))
    price_today = sum(list(map(lambda x:MenuMaster.query.filter_by(menu_id=x.menu_id).first().price, today)))

    return render_template("index.html",calorie_today = "{:.0f}".format(calorie_today),price_today=price_today)

@app.route("/input", methods=["POST"])
def input_():
    allmenu = MenuMaster.query.all()
    list_size = len(MenuMaster.query.all())
    options = list(map(lambda x:x.name, allmenu))
    return render_template("input.html",list_size=list_size,options=options)


@app.route("/manage", methods=["POST"])
def manage():
    if request.form["button"] == "history":
        return redirect(url_for("history"))
    elif request.form["button"] == "manage-menu":
        return redirect(url_for("manage_menu"))
    