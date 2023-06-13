from flask import request, redirect, url_for, render_template, flash, session
from calorie import app,db
from calorie.models.calDB import Meal,MenuMaster
from functools import wraps
import datetime

@app.route("/manage",methods=["GET","POST"])
def manage_menu():
    menus = MenuMaster.query.all()
    return render_template("managemenu.html",menus=menus)

@app.route("/choosemanage",methods=["POST"])
def choose_management():
    if request.form["button"] == "add-menu":
        return redirect(url_for("add_menu"))
    elif request.form["button"] == "edit-menu":
        return redirect(url_for("delete_menu"))
    return redirect(url_for("index"))

@app.route("/addmenu",methods=["GET","POST"])
def add_menu(menuname = None,calorie = None,price = None):
    if request.method == "POST":
        if request.form["button"] == "add":
            name = request.form["name"]
            calorie = request.form["calorie"]
            price = request.form["price"]

            # エラーチェック
            assert name and calorie and price
            #型チェック
            try:
                calorie = float(calorie)
                price = int(price)
            except:
                flash("数値で入力してください")
                return redirect("add_menu")
            
            menu = MenuMaster(calorie=calorie,price=price)
            db.session.add(menu)
            db.session.commit()

        return redirect(url_for("manage_menu"))

    return render_template("addmenu.html")

@app.route("/editmenu")
def edit_menu(menu_id):
    menu = MenuMaster.query.get(menu_id)
    return redirect(url_for("choose_management"))