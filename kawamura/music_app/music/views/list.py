from flask import request, redirect, url_for, render_template, flash, session
from music import app
from music.models.database import Music

@app.route('/templates/list')
def show_entries():
    entries =Music.query.order_by(Music.band_name.desc()).all()
    return render_template('list.html', entries = entries)