from flask import request, redirect, url_for, render_template, session, flash
from baseball import app
from baseball import db
from baseball.models.players  import Player

@app.route('/new', methods=['GET', 'POST'])
def add_player():
    if request.method == "POST":
        input_name = request.form["name"]
        input_number = request.form["number"]
        player = Player.query.filter_by(number=input_number).first()
        player_name = Player.query.filter_by(name=input_name).first()
        if not input_name or not input_number:
            flash("名前または背番号が入力されていません")
        elif player or player_name:
            flash("既に選手が登録されています")
        else:
            try:
                int(input_number)
                player = Player (
                    name = request.form["name"],
                    number = request.form["number"],
                    text = request.form["text"]
                )
                db.session.add(player)
                db.session.commit()
                flash("新しい選手を登録しました")
            except:
                flash("背番号は数値で入力してください")
    return render_template('new.html')