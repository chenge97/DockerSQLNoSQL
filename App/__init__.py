from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('App.config.flask_config.FlaskConfig')

db = SQLAlchemy(app)


import App.blueprints