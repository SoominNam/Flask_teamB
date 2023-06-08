from flask import request, redirect, url_for, render_template, session, flash
from baseball import app
from baseball import db
from baseball.models.players  import Player

@app.route('/result', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        if request.form["button"] == "search":
            if not request.form["player_number"]:
                flash("背番号を入力してください")
                return redirect(url_for("index"))
            elif int(request.form["player_number"]) > 100:
                flash("99以下の番号を入力してください")
                return redirect(url_for("index"))
        else:
            input_number = int(request.form["player_number"])
            player = Player.query.filter_by(number=input_number)
            if not player:
                flash("該当選手がいません")
                return render_template('index.html')
            else:
                name = player.name
                text = player.text
            return render_template("result.html", name = name, text = text)
        