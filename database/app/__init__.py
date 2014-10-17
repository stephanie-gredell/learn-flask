from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config') #tell flask to use our config
db = SQLAlchemy(app)

from app import views, models
