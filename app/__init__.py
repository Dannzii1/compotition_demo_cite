import os

from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)

SECRET_KEY = os.getenv('SECRET_KEY')


app.config.from_object(__name__)
from app import views

