from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('attendance_manage.config')

db = SQLAlchemy(app)

from attendance_manage.views import views