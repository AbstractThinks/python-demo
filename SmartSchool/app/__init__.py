from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_json import FlaskJSON

app = Flask(__name__)
FlaskJSON(app)
app.config.from_object('config')
db = SQLAlchemy(app)


from app.models import user,school,classes,subject
from app.views import view
