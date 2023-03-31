from flask import Flask, jsonify, request, render_template
import mysql.connector
from mysql.connector import errorcode
import SQL.SQLQueries as SQLQueries
import utils.utils as utils
from flask_cors import CORS
# from typing import List, Dict, Tuple, Union, Any


app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/*":{'origins': "*"}})
# CORS(app, resources={r"/*":{'origins': "http://localhost:8080","allow_headers":"Acces-Control-Allow-Origin"}})

@app.route("/")
def homepage():
    return render_template("index.html")

# route to obtain nitrogen-derived fertilisers by region.
@app.route('/api/regions-fertilizers-nitrogen', methods=['GET'])
def get_fertilizers_nitrogen_region():
    region = request.args.get('region_name')
    if region:
        if any(char.isdigit() for char in region):
            return "The name of the region cannot contain numbers.", 400
        try:
            fertilizers = utils.get_fertilizers_nitrogen_region(region)
            if fertilizers:
                return jsonify(fertilizers), 200
            else:
                return "No fertiliser data were found for the region provided.", 404
        except Exception as e:
            return f"An error occurred while obtaining fertiliser data.: {str(e)}", 500


# route to obtain phosphorus-derived fertilisers by region.
@app.route('/api/regions-fertilizers-phosphorous', methods=['GET'])
def get_fertilizers_phosphorous_region():
    region = request.args.get('region_name')
    if region:
        try:
            fertilizers = utils.get_fertilizers_phosphorous_region(region,)
            if fertilizers is not None:
                return jsonify(fertilizers), 200
            else:
                return "Error en la consulta a la base de datos", 500
        except ValueError:
            return "El valor del año debe ser un número entero", 400
    else:
        return "Please provide region_name parameter in the URL", 400


# route to obtain phosphorus-derived fertilisers by region.
@app.route('/api/regions-fertilizers-potassium', methods=['GET'])
def get_fertilizers_potassium_region():
    region = request.args.get('region_name')
    if region:
        try:
            fertilizers = utils.get_fertilizers_potassium_region(region,)
            if fertilizers is not None:
                return jsonify(fertilizers), 200
            else:
                return "Error en la consulta a la base de datos", 500
        except ValueError:
            return "El valor del año debe ser un número entero", 400
    else:
        return "Please provide region_name parameter in the URL", 400

# route to obtain potassium-derived fertilisers.
@app.route('/api/fertilizers-nitrogen', methods=['GET'])
def get_fertilizers_nitrogen():
    try:
        fertilizers = utils.get_fertilizers_nitrogen()
        return jsonify(fertilizers), 200
    except:
        return jsonify({'error': 'An error occurred while obtaining nitrogen fertiliser data.'}), 500


# route to obtain potassium-derived fertilisers.
@app.route('/api/fertilizers-phosphorous', methods=['GET'])
def get_fertilizers_phosphorous():
    try:
        fertilizers = utils.get_fertilizers_phosphorous()
        return jsonify(fertilizers), 200
    except:
        return jsonify({'error': 'An error occurred while obtaining nitrogen fertiliser data.'}), 500
    

# route to obtain potassium-derived fertilisers.
@app.route('/api/fertilizers-potassium', methods=['GET'])
def get_fertilizers_potassium():
    try:
        fertilizers = utils.get_fertilizers_potassium()
        return jsonify(fertilizers), 200
    except:
        return jsonify({'error': 'An error occurred while obtaining nitrogen fertiliser data.'}), 500


# route to obtain all fertilisers and their derivatives by region.
# Region, Derived, Year, Amount, Unit
@app.route('/api/regions-fertilizers', methods=['GET'])
def get_fertilizers_year():
    year: int = request.args.get('year')
    region: str = request.args.get('region_name')
    if year:
        try:
            year = int(year)
            if year < 0:
                raise ValueError
            fertilizers = utils.get_fertilizers_by_year(year)
            return jsonify(fertilizers), 200
        except ValueError:
            return "The value of the year must be a positive whole number.", 400
        except Exception as e:
            return f"An error occurred while obtaining fertiliser data.: {str(e)}", 500

    if region:
        if any(char.isdigit() for char in region):
            return "The name of the region cannot contain numbers.", 400

        try:
            fertilizers = utils.get_fertilizers_by_region(region)
            if fertilizers:
                return jsonify(fertilizers), 200
            else:
                return "No fertiliser data were found for the region provided.", 404
        except Exception as e:
            return f"An error occurred while obtaining fertiliser data.: {str(e)}", 500

    return "Please enter a whole number in Year like this ?year= Or enter a region_name like this ?region_name= ", 400



# route to obtain fertilisers from region and year
@app.route('/api/regions-fertilizers/<string:region>/<int:year>')
def get_fert_region_year(region, year):
    if not region:
        return "The region has not been specified.", 400
    elif any(char.isdigit() for char in region):
        return "The name of the region cannot contain numbers.", 400

    try:
        fertilizers = utils.get_fertilizers_by_region_and_year(region, year)
        if fertilizers:
            return jsonify(fertilizers), 200
        else:
            return "No fertiliser data were found for the region and year provided.", 404
    except ValueError:
        return "The value of the year must be a positive integer.", 400
    except Exception as e:
        return f"An error occurred while obtaining fertiliser data: {str(e)}", 500



# route to obtain fertilisers from region and year
@app.route('/api/regions-fertilizers-flora')
def get_fert_region_flora():
    try:
        fertilizers: list[dict[str,any]] = utils.get_fertilizers_flora_by_region_and_year()
        return jsonify(fertilizers),200
    except:
        return jsonify({'error': 'An error occurred while obtaining nitrogen fertiliser data.'}), 500



# route to obtain fertilisers from region and year
@app.route('/api/all-fertilizers-regions')
def get_all_fert():
    try:
        fertilizers: list[dict[str,any]] = utils.get_fertilizers_regions_all_data()
        return jsonify(fertilizers), 200
    except:
        return jsonify({'error': 'Ha ocurrido un error al obtener los datos de los fertilizantes por región'}), 500


# route to obtain fertilisers from region and year
@app.route('/api/fertilizers-nitrogen')
def get_all_nitrogen():
    try:
        fertilizers: list[dict[str,any]] = utils.get_fertilizers_nitrogen_all_data()
        return jsonify(fertilizers), 200
    except:
        return jsonify({'error': 'An error occurred while obtaining nitrogen fertiliser data.'}), 500



if __name__ == '__main__':
    app.run(debug=True)
