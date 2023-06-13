from flask import request, redirect, url_for, render_template, flash, session
from baseball import app
from baseball import db
from baseball.models.players  import Player

@app.route("/list", methods=["GET", "POST"])
def show_list():
    playerList = Player.query.all()
    ikeda = None
    for i, v in enumerate(playerList):
        if v.number == "00":
            ikeda = v
            playerList.remove(ikeda)
            break
    
    for i in range(len(playerList)):
        for j in range(i, len(playerList)):
            if int(playerList[i].number) > int(playerList[j].number):
                p = playerList[i]
                playerList[i] = playerList[j]
                playerList[j] = p
    playerList.insert(0, ikeda)

    return render_template('list.html', playerList = playerList)

@app.route("/delete", methods=["GET", "POST"])
def delete_player():
    if request.method == "POST":
        player_number = request.form["button"]
        player = Player.query.filter_by(number=player_number).first()
        db.session.delete(player)
        db.session.commit()
        flash(player.name + "を削除しました")
    return redirect(url_for('show_list'))