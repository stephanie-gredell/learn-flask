from flask import Flask

app = Flask(__name__)
app.config.from_object('config') #tell flask to use our config

from app import views
