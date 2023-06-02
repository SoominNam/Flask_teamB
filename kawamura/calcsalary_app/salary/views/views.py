from salary import app
from flask import request, url_for, render_template,flash, session, redirect
import sys
from decimal import Decimal, ROUND_HALF_UP

@app.route('/')
def show_entries():
    return render_template('input.html')

@app.route('/login',methods=['GET','POST'])
def login():
    sikyu = 0
    tax = 0
    if request.method=='POST':
        if request.form['username'] == "":
            flash('入力しろ')
            return render_template('input.html')
        if len(request.form['username']) >= 11:
            flash('10字以内にしろ')
            return render_template('input.html')
        if int(request.form['username']) < 0:
            flash('マイナスはおかしい')
            return render_template('input.html')

        else:
            if int(request.form['username']) > 1000000 :
                tax = Decimal(100000 + ( int(request.form['username']) - 1000000)* 0.2).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
                sikyu = int(request.form['username']) - tax
                print("支給額:" + str(sikyu) + "、", end="")
                print("税額:" + str(tax), end="")

            else :
                tax = Decimal(int(request.form['username'])*0.1).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
                sikyu = int(request.form['username']) - tax
                print("支給額:" + str(sikyu) + "、", end="")
                print("税額:" + str(tax), end="")
            
    return render_template('output.html',kyuyo = request.form['username'], result = sikyu, zei = tax)
