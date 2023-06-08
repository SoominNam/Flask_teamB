from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('baseball.config')

db = SQLAlchemy(app)

from baseball.views import search, main, player, list