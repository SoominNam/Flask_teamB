from flask import request, redirect, url_for, render_template, flash, session
from music import app
from music.models.database import Music


@app.route('/')
def show_input():
    return render_template('input.html')



