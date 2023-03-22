from flask_sqlalchemy import SQLAlchemy
from .fertilizer import db

db = SQLAlchemy()

class RegionFertilizerYear(db.Model):
    region_name = db.Column(db.String(50), db.ForeignKey('regions.region_name'), primary_key=True, nullable=False)
    code = db.Column(db.String(50), db.ForeignKey('regions.code'), primary_key=True, nullable=False)
    year = db.Column(db.Integer, db.ForeignKey('years.year'), primary_key=True, nullable=False)
    total_kg_nitrogen_per_hectare = db.Column(db.Float, nullable=False)
    total_kg_phosphorous_per_hectare = db.Column(db.Float, nullable=False)
    total_kg_per_potassium_hectare = db.Column(db.Float, nullable=False)

    region = db.relationship('Region', foreign_keys=[region_name, code], backref=db.backref('fertilizers_years', lazy=True))
    year_rel = db.relationship('Year', foreign_keys=[year], backref=db.backref('fertilizers_years', lazy=True))

    def __init__(self, region_name, code, year, total_kg_nitrogen_per_hectare, total_kg_phosphorous_per_hectare, total_kg_per_potassium_hectare):
        self.region_name = region_name
        self.code = code
        self.year = year
        self.total_kg_nitrogen_per_hectare = total_kg_nitrogen_per_hectare
        self.total_kg_phosphorous_per_hectare = total_kg_phosphorous_per_hectare
        self.total_kg_per_potassium_hectare = total_kg_per_potassium_hectare
