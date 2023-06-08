from flask import request, redirect, url_for, render_template, flash, session
from baseball import app
from baseball import db
from baseball.models.players  import Player

@app.route("/list", methods=["GET", "POST"])
def show_list():
    playerList = Player.query.order_by(Player.number.asc()).all()
    return render_template('list.html', playerList = playerList)