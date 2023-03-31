from flask import Flask, jsonify, request
import mysql.connector
from SQL import SQLQueries

app = Flask(__name__)

# función para conectarse a la base de datos
def get_database_connection():
    db = mysql.connector.connect(
        host="localhost",
        user="provenusr",
        password="provenpass",
        database="fertilizers_db"
    )
    return db

# función para obtener fertilizantes por región
def get_fertilizers_by_region(region):
    try:
        db = get_database_connection()
        cursor = db.cursor()
        query = SQLQueries.get_all_fertilizers_by_region_query
        cursor.execute(query, (region,))
        fertilizers = cursor.fetchall()
        return fertilizers
    except Exception as e:
        print("Error:", e)
        return None

def get_fertilizers_by_year(year: str):
    try:
        db = get_database_connection()
        cursor = db.cursor()
        query = SQLQueries.get_all_fertilizers_by_year_query
        cursor.execute(query, (year,))
        fertilizers = cursor.fetchall()
        return fertilizers
    except Exception as e:
        print("Error:", e)
        return None
      


# función para obtener fertilizantes por región y año
def get_fertilizers_by_region_and_year(region : str, year : str):
    try:
        db = get_database_connection()
        cursor = db.cursor()
        query = SQLQueries.get_fertilizers_by_region_and_year_query
        cursor.execute(query, (region, year))
        fertilizers = cursor.fetchall()
        return fertilizers
    except Exception as e:
        print("Error:", e)
        return None
    


# función para obtener fertilizantes por región y año
def get_fertilizers_by_region_and_year_start_year_end(region : str, year_start : str, year_end : str):
    db = get_database_connection()
    cursor = db.cursor()
    query = SQLQueries.get_fertilizers_by_region_year_start_year_end
    cursor.execute(query, (region, year_start, year_end))
    fertilizers = cursor.fetchall()
    return fertilizers


# ruta para obtener fertilizantes por región y año a través de la URL
# @app.route('/fertilizers', methods=['GET'])
# def get_fertilizers_region_year():
#     region = request.args.get('region')
#     year = request.args.get('year')
#     if region:
#         if year:
#             try:
#                 fertilizers = get_fertilizers_by_region_and_year(region, int(year))
#                 if fertilizers is not None:
#                     return jsonify(fertilizers), 200
#                 else:
#                     return "Error en la consulta a la base de datos", 500
#             except ValueError:
#                 return "El valor del año debe ser un número entero", 400
#         else:
#             fertilizers = get_fertilizers_by_region(region)
#             if fertilizers is not None:
#                 return jsonify(fertilizers), 200
#             else:
#                 return "Error en la consulta a la base de datos", 500
#     else:
#         return "El parámetro region es obligatorio en la URL", 400


# # ruta para obtener fertilizantes por región y rango de años
# @app.route('/fertilizers', methods=['GET'])
# def get_fertilizers():
#     region = request.args.get('region')
#     year_start = request.args.get('year_start')
#     year_end = request.args.get('year_end')
#     if region and year_start and year_end:
#         fertilizers = get_fertilizers_by_region_and_year_start_year_end(region, int(year_start), int(year_end))
#         return jsonify(fertilizers)
#     else:
#         return "Please provide region, year_start, and year_end parameters in the URL", 400










# # función para obtener fertilizantes por región y año
# def get_fertilizers_by_region_new():
#     try:
#         db = get_database_connection()
#         cursor = db.cursor()
#         query = SQLQueries.get_all_fertilizers_by_region_query4
#         cursor.execute(query)
#         fertilizers = cursor.fetchall()
#         return fertilizers
#     except Exception as e:
#         print("Error:", e)




# @app.route('/fertilizers_by_region', methods=['GET'])
# def get_fertilizers():
#         fertilizers = get_fertilizers_by_region_new
#         return jsonify(fertilizers)


@app.route('/regions-fertilizers-flora')
def get_regions_fertilizers_flora():
    db_connection = mysql.connector.connect(host='localhost', user='provenusr', password='provenpass', database='project_db')
    cursor = db_connection.cursor(dictionary=True)

    query = "SELECT regions.region_name, regions_fertilizers_flora.year, fertilizers.name_fertilizer, flora.name_flora, regions_fertilizers_flora.amount, regions_fertilizers_flora.unit \
            FROM regions_fertilizers_flora \
            JOIN regions ON regions_fertilizers_flora.id_region = regions.id_region \
            JOIN fertilizers ON regions_fertilizers_flora.id_fertilizer = fertilizers.id_fertilizer \
            JOIN flora ON regions_fertilizers_flora.id_flora = flora.id_flora"

    cursor.execute(query)
    results = cursor.fetchall()
    
    cursor.close()
    db_connection.close()
    
    return jsonify(results)


@app.route('/regions-fertilizers-nitrogen')
def get_regions_fertilizers_nitrogen():
    db_connection = mysql.connector.connect(host='localhost', user='provenusr', password='provenpass', database='project_db')
    cursor = db_connection.cursor(dictionary=True)

    query = "SELECT regions.region_name, fertilizers.name_fertilizer, regions_fertilizers.year, regions_fertilizers.amount, regions_fertilizers.unit \
            FROM regions_fertilizers \
            JOIN regions ON regions_fertilizers.id_region = regions.id_region \
            JOIN fertilizers ON regions_fertilizers.id_fertilizer = fertilizers.id_fertilizer \
            WHERE fertilizers.name_fertilizer = 'nitrogen_derived'"

    cursor.execute(query)
    results = cursor.fetchall()
    
    cursor.close()
    db_connection.close()
    
    return jsonify(results)



@app.route('/regions-fertilizers/<pais>/<int:anio>')
def get_regions_fertilizers(pais, anio):
    db_connection = mysql.connector.connect(host='localhost', user='provenusr', password='provenpass', database='project_db')
    cursor = db_connection.cursor(dictionary=True)

    query = "SELECT regions.region_name, fertilizers.name_fertilizer, regions_fertilizers.amount \
            FROM regions_fertilizers \
            JOIN regions ON regions_fertilizers.id_region = regions.id_region \
            JOIN fertilizers ON regions_fertilizers.id_fertilizer = fertilizers.id_fertilizer \
            WHERE regions.region_name = %s AND regions_fertilizers.year = %s"

    cursor.execute(query, (pais, anio))
    results = cursor.fetchall()
    
    cursor.close()
    db_connection.close()
    
    return jsonify(results)




@app.route('/regions-fertilizers/nitrogen-derived/<string:country>/<int:year>')
def get_nitrogen_derived(country, year):
    db_connection = mysql.connector.connect(host='localhost', user='provenusr', password='provenpass', database='project_db')
    cursor = db_connection.cursor(dictionary=True)

    query = "SELECT regions.region_name, fertilizers.name_fertilizer, regions_fertilizers.year, regions_fertilizers.amount \
             FROM regions_fertilizers \
             JOIN regions ON regions_fertilizers.id_region = regions.id_region \
             JOIN fertilizers ON regions_fertilizers.id_fertilizer = fertilizers.id_fertilizer \
             WHERE regions.region_name = %s AND regions_fertilizers.year = %s AND fertilizers.name_fertilizer = 'nitrogen_derived'"
    
    cursor.execute(query, (country, year))
    results = cursor.fetchall()

    cursor.close()
    db_connection.close()

    return jsonify(results)


@app.route('/regions-fertilizers/<string:country>')
def get_regions_fertilizers1(country):
    year = request.args.get('year')
    # Resto del código












# ruta para obtener fertilizantes por región y rango de años
# @app.route('/fertilizers', methods=['GET'])
# def get_fertilizers():
#     region = request.args.get('region')
#     year_start = request.args.get('year_start')
#     year_end = request.args.get('year_end')
#     if region and year_start and year_end:
#         fertilizers = get_fertilizers_by_region_and_year_start_year_end(region, int(year_start), int(year_end))
#         return jsonify(fertilizers)
#     else:
#         return "Please provide region, year_start, and year_end parameters in the URL", 400








if __name__ == '__main__':
    app.run(debug=True)








# ruta para obtener fertilizantes por región a través de la URL
# @app.route('/fertilizers', methods=['GET'])
# def get_fertilizers_region():
#     region = request.args.get('region')
#     if region:
#         fertilizers = get_fertilizers_by_region(region)
#         return jsonify(fertilizers)
#     else:
#         return "Please provide a region parameter in the URL", 400


# ruta para obtener fertilizantes por región y año a través de la URL
# @app.route('/fertilizers', methods=['GET'])
# def get_fertilizers():
#     region = request.args.get('region')
#     year = request.args.get('year')
#     if region and year:
#         fertilizers = get_fertilizers_by_region_and_year(region, int(year))
#         return jsonify(fertilizers)
#     elif region:
#         fertilizers = get_fertilizers_by_region(region)
#         return jsonify(fertilizers)
#     else:
#         return "Please provide a region parameter in the URL", 400