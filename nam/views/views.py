from flask import request, redirect, url_for, render_template, flash, session
from attendance_manage.views import views

@views.route('/', methods=['GET', 'POST'])
def input():
    return render_template('input.html')