from flask import request, redirect, url_for, render_template, session
from salary import app
from decimal import Decimal, ROUND_HALF_UP


@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template("input.html")

@app.route('/output', methods=['GET', 'POST'])
def input():
    salary = int(request.form["salary"])

    if request.method == 'POST':
        if  salary > 1000000:
           tax = (salary - 1000000) * 0.2 + 1000000 * 0.1
           expenses = salary - tax
        else:
            tax = salary * 0.1
            expenses = salary - tax
    return render_template('output.html', salary = salary, tax = tax, expenses = expenses)
   
