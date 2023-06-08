from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from decimal import Decimal,ROUND_HALF_UP


print("aaasdad")

#間違えそうなので定数にしておく
BOUND = 1000000

#関数
def check_value(value):
    #空白か？
    if not value:
        raise ValueError("input value is empty")
    
    #数値か？
    try:
        value = int(value)
    except ValueError:
        raise ValueError("input value is not numeric")
    
    #マイナスか？
    if value < 0:
        raise ValueError("input value is under 0")
    
    #10桁いないか？
    elif value > 1000000000:
        raise ValueError("input value exceeds 1,000,000,000")
    
    return None


def calc_salary(pay):
    #バリューチェック
    try:
        check_value(pay)
    except ValueError as e:
        flash(e)
        return None,None,None

    #額面給与を100万より上と以下にわける
    #100万より上の部分がマイナスの場合は額面が100万以下であるので、上の部分は0に直す
    upper_pay = int(pay) - BOUND
    if upper_pay < 0:
        upper_pay = 0

    #以下の部分
    lower_pay = int(pay) - upper_pay

    #それぞれの税額計算
    lower_tax = lower_pay * 0.1
    upper_tax = upper_pay * 0.2

    #税額をがっさんして四捨五入
    tax = lower_tax + upper_tax
    tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)

    #支払い額は額面-税額
    payment = int(pay) - tax
    return pay,tax,payment

#html紐づけ
@app.route('/', methods=['GET', 'POST'])
def show_entries():
    print('aaa')
    return render_template("input.html")

@app.route('/input', methods=['GET', 'POST'])
def calc_routine():
    if request.method=="POST":
        pay,tax,payment = calc_salary(request.form["input_number"])
        if pay:
            return render_template("output.html",pay=pay,tax=tax,payment=payment)
    return render_template("input.html")

@app.route("/output",methods=["GET","POST"])
def outoput():
    if request.method == "POST":
        render_template(url_for("show_entries"))
    return render_template("output.html")