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

@app.route("/all", methods=["POST"])
def new_meal():
    return

@app.route("/manage", methods=["POST"])
def manage():
    if request.form["button"] == "history":
        return redirect(url_for("history"))
    elif request.form["button"] == "manage-menu":
        return redirect(url_for("manage_menu"))
    
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

@app.route("/manage")
def manage_menu():
    return render_template("manage_menu.html")

@app.route("/delete",methods=["POST"])
def delete_meal():
    id_ = request.form["button"]
    print("id: ",request.form["button"])
    return redirect(url_for("history"))

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
