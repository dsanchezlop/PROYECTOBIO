from flask import Blueprint, jsonify, request
from fertilizer_api.app import app
from fertilizer_api.models.regions import Regions

regions_bp = Blueprint('regions', __name__)

@regions_bp.route('/regions', methods=['GET'])
def get_all_regions():
    regions_model = Regions()
    regions = regions_model.get_all_regions()
    return jsonify(regions), 200
