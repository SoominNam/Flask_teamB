#入力画面の呼び出し
from flask import request, redirect, url_for, render_template, flash, session
from holiday import app

@app.route('/', methods=['GET', 'POST'])
def input():
    return render_template('input.html')