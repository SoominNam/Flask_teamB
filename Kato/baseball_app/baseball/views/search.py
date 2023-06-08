from flask import request, redirect, url_for, render_template, session, flash
from baseball import app
from baseball import db
from baseball.models.players  import Player

@app.route('/result', methods=['GET', 'POST'])
def search():
    if request.form["button"] == "search":
        input_number = request.form["player_number"]          
        if not input_number:
            flash("背番号を入力してください")
        elif input_number.isdecimal() == False:
            flash("数値で入力してください")
        elif int(input_number) > 99:
            flash("99以下の番号を入力してください")
        else:
            player = Player.query.filter_by(number=input_number).first()
            if not player:
                flash("該当選手がいません")
            else:
                name = player.name
                text = player.text
                return render_template("result.html", name = str(name), text = str(text))
    return redirect(url_for("main"))
        