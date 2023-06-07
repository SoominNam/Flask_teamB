from flask import request, redirect, url_for, render_template, session, flash
from baseball import app
from baseball import db
from baseball.models.players  import Player

@app.route('/new', methods=['GET', 'POST'])
def add_player():
    if request.method == "POST":
        player = Player (
            name = request.form["name"],
            number = request.form["number"],
            text = request.form["text"]
        )
        db.session.add(player)
        db.session.commit()
        flash("新しい選手を登録しました")
    return render_template('new.html')