from flask import request, redirect, url_for, render_template, session, flash
from baseball import app

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template("index.html")