from flask import request, redirect, url_for, render_template, flash, session
from game import app
from game import db
from functools import wraps
from game.models.players import Player

def login_requied(views):
    @wraps(views)
    def inner(*args, **kwargs):
        if not session.get("logged_in"):
            flash("ログインが必要です")
            return redirect(url_for("login"))
        return views(*args, **kwargs)
    return inner

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        if not request.form["email"] and not request.form["password"]:
            flash("入力してください")
        else:
            player = Player.query.filter(Player.email == request.form["email"]).first()
            if player:
                session["logged_in"] = player.email
                flash("ログインしました")
                return redirect(url_for("index"))
            else:
                flash("メールアドレスまたはパスワードが間違えています")
    return render_template("auth/login.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        if not request.form["email"] and not request.form["name"] and not request.form["password"]:
            flash("入力してください")
        else:
            player = Player.query.filter(Player.email == request.form["email"]).first()
            if player:
                flash(f"そのメールアドレスは既に使われています。\nここだけの話、パスワードは{player.password}です")
            else:
                player = Player(
                    email = request.form["email"],
                    name = request.form["name"],
                    password = request.form["password"]
                )
                db.session.add(player)
                db.session.commit()
                flash("登録が完了しました")
                session["logged_in"] = player.email
                return redirect(url_for("index"))
    return render_template("auth/register.html")

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    flash("ログアウトしました__(:3」∠)__なにみてんだよ")
    return redirect(url_for("index"))