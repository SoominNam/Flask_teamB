from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("calorie.config")

db = SQLAlchemy(app)

from calorie.views import views,meal,menu