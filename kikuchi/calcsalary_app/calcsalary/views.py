from flask import request, redirect, url_for, render_template, flash, session
from calcsalary import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/output", methods=["GET","POST"])
def output():
    if request.method == "POST":
        if not request.form["salary"]:
            flash("入力しろください。__(:3」∠)__")
        else:
            salary = int(request.form["salary"])
            tax = salary * 0.1
            if salary>=1000000:
                tax += (salary-1000000) * 0.1
            tax = int(tax)
            payment = salary-tax
            return render_template("output.html", salary="{:,}".format(salary), payment="{:,}".format(payment), tax="{:,}".format(tax))
        
    return redirect(url_for("index"))
