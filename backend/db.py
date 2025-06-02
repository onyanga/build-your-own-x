
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cleaning_management.db'
db.init_app(app)

with app.app_context():
    db.create_all()