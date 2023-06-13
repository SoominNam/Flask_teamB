from flask import request, redirect, url_for, render_template, flash, session
from game import app
from game import db
from game.views.auth import login_requied
from game.models.players import Player
from game.models.scores import Score

@app.route("/")
def index():
    scores = Score.query.order_by(Score.score.asc()).limit(50).all()
    return render_template("home.html", scores=scores)


@app.route("/play")
def play():
    return render_template("play.html")

@app.route("/score", methods=["GET","POST"])
@login_requied
def score():
    if request.method == "POST":
        player = Player.query.filter(Player.email == session.get("logged_in")).first()
        if not player:
            flash("ユーザー情報が不明です")
            return redirect(url_for("index"))
        else:
            rank = False
            score = Score(
                score = int(request.form["score"]),
                playerid = player.id
            )
            try:
                db.session.add(score)
                db.session.commit()
                score = Score.query.filter(Score.score <= score.score).all()
                flash("登録できました")
            except Exception as e:
                print(e)
                flash("登録できませんでした")
                return redirect(url_for("play"))

            return render_template("score.html", rank = len(score))

    return redirect(url_for("index"))
    