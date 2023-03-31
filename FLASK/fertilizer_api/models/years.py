from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Year(db.Model):
    id_year = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer, unique=True, nullable=False)

    def __init__(self, year):
        self.year = year
