from flask import request, redirect, url_for, render_template, session, flash
from salary import app
from decimal import Decimal, ROUND_HALF_UP


@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template("input.html")

@app.route('/output', methods=['GET', 'POST'])
def input():
    len_salary = len(str(request.form["salary"]))

    if request.method == 'POST':
        if not request.form["salary"]:
            flash("給与が未入力です。入力してください。")
        elif len_salary >= 10:
            flash("給与には最大9,999,999,999まで入力可能です。")
        elif int(request.form["salary"]) < 0:
            flash("給与にはマイナスの値は入力できません。")
        else:
            salary = int(request.form["salary"])
            if  salary > 1000000:
                tax = (salary - 1000000) * 0.2 + 1000000 * 0.1
                expenses = salary - tax
            else:
                tax = salary * 0.1
                expenses = salary - tax
            return render_template('output.html', salary = salary, tax = tax, expenses = expenses)
    return redirect("/")
