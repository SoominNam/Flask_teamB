from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from flask_blog import db
from flask_blog.models.entries import Entry
from flask_blog.views.views import login_required

@app.route("/")
@login_required
def show_entries():
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template("entries/index.html",entries=entries)

@app.route("/entries/new",methods=["GET"])
def new_entry():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("entries/new.html")

@app.route("/entries",methods=["POST"])
def add_entry():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    entry = Entry(
        title=request.form["title"],
        text=request.form["text"]
    )
    db.session.add(entry)
    db.session.commit()
    flash("新規投稿成功")
    return redirect(url_for("show_entries"))

@app.route("/entries/<int:id>",methods=["GET"])
def show_entry(id):
    if not session.get("logged_in"):
        return redirect(url_for('login'))
    entry = Entry.query.get(id)
    return render_template("entries/show.html",entry=entry)

@app.route("/entries/<int:id>/edit",methods=["GET"])
def edit_entry(id):
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    ent = Entry.query.get(id)
    return render_template("entries/edit.html",entry=ent)

@app.route("/entries/<int:id>/update",methods=["POST"])
def update_entry(id):
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    entry = Entry.query.get(id)
    entry.title = request.form["title"]
    entry.text = request.form["text"]
    db.session.merge(entry)
    db.session.commit()
    flash("更新成功")
    return redirect(url_for("show_entries"))

@app.route('/entries/<int:id>/delete',methods=["POST"])
def delete_entry(id):
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    entry = Entry.query.get(id)
    db.session.delete(entry)
    db.session.commit()
    flash("削除成功")
    return redirect(url_for("show_entries"))