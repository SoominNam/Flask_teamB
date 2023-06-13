from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('music.config')
db = SQLAlchemy(app)

from music.views import input, list, maintenance_date