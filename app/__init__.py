from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

# Initializing application

bootstrap = Bootstrap()
app = Flask(__name__)

app.config.from_object(DevelopmentConfig)
app.config.from_pyfile('config.py')

from app import views
