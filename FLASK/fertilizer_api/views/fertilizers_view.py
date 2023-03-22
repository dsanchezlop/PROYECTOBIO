from flask import Blueprint, request, jsonify
from models.regions import db, Region
from models.years import db, Year
from models.fertilizers import RegionFertilizerYear
from marshmallow import Schema

fertilizer_bp = Blueprint('fertilizer_bp', __name__)

class RegionSchema(Schema):
    class Meta:
        fields = ("id_region", "region_name")

class YearSchema(Schema):
    class Meta:
        fields = ("id_year", "year")

class RegionFertilizerYearSchema(Schema):
    class Meta:
        fields = ("region_name", "code", "year", "total_kg_nitrogen_per_hectare", "total_kg_phosphorous_per_hectare", "total_kg_per_potassium_hectare")

region_schema = RegionSchema()
regions_schema = RegionSchema(many=True)

year_schema = YearSchema()
years_schema = YearSchema(many=True)

fertilizer_schema = RegionFertilizerYearSchema()
fertilizers_schema = RegionFertilizerYearSchema(many=True)

# Aquí puedes agregar los controladores para cada entidad (Region, Country, Year, Fertilizer)
# siguiendo el mismo patrón que en el ejemplo anterior (crear, leer, actualizar, eliminar).

# Ejemplo: Obtener todas las regiones
@fertilizer_bp.route('/regions', methods=['GET'])
def get_regions():
    regions = Region.query.all()
    return regions_schema.jsonify(regions)

# Ejemplo: Obtener todos los fertilizantes
@fertilizer_bp.route('/fertilizers', methods=['GET'])
def get_fertilizers():
    fertilizers = RegionFertilizerYear.query.all()
    return fertilizers_schema.jsonify(fertilizers)

# Añade más rutas y controladores aquí
