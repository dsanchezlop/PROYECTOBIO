from flask_sqlalchemy import SQLAlchemy
from .regions import db

db = SQLAlchemy()

class Region(db.Model):
    id_region = db.Column(db.Integer, primary_key=True, autoincrement=True)
    region_name = db.Column(db.String(50), unique=True, nullable=False)
    code = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, region_name, code):
        self.region_name = region_name
        self.code = code
