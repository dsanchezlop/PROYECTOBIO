from flask import Flask, jsonify, request
from config import config
from flask_mysqldb import MySQL
import SQL.SQLQueries as SQLQueries

app = Flask(__name__)

# Configuración de la base de datos
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'provenusr'
# app.config['MYSQL_PASSWORD'] = 'provenpass'
# app.config['MYSQL_DB'] = 'fertilizers_db'

mysql = MySQL(app)


# @app.route('/fertilizers', methods=['GET'])
# def get_fertilizers():
#     cur = mysql.connection.cursor()
#     cur.execute('''SELECT * FROM regions_fertilizers_years''')
#     data = cur.fetchall()
#     cur.close()

#     return jsonify(data)


@app.route('/fertilizers', methods=['GET'])
def get_fertilizers():
    region = request.args.get('region_name')
    if region:
        fertilizers = SQLQueries.get_all_fertilizers_for_region_query(region)
        return jsonify(fertilizers)
    else:
        return "Please provide a region parameter in the URL", 400








# Ruta de la API para obtener todos los datos de la tabla de fertilizers
# @app.route('/fertilizers', methods=['GET'])
# def get_fertilizers():
#     cur = mysql.connection.cursor()
#     cur.execute(SQLQueries.select_all_info_fertilizers_query)
#     data = cur.fetchall()
#     cur.close()

#     return jsonify(data)



# @app.route('/fertilizers', methods=['GET'])
# def get_fertilizers_by_region(region):

#     cur = mysql.connection.cursor()
#     cur.execute(SQLQueries.get_all_fertilizers_for_region_query.format(region = region))
#     data = cur.fetchall()
#     cur.close()

#     return jsonify(data)


# @app.route('/fertilizers', methods=['GET'])
# def get_fertilizers_by_region():
#     region_name = request.args.get('region_name')
#     cur = mysql.connection.cursor()
#     cur.execute(SQLQueries.get_all_fertilizers_for_region_query,(region_name))
#     data = cur.fetchall()
#     cur.close()
#     return jsonify(data)

# @app.route('/fertilizers', methods=['GET'])
# def get_fertilizers_by_region():
#     region_name = request.args.get('region_name')
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT region_name, code, year, total_kg_nitrogen_per_hectare, total_kg_phosphorous_per_hectare, total_kg_per_potassium_hectare FROM regions_fertilizers_years WHERE region_name = %s", (region_name,))
#     data = cur.fetchall()
#     cur.close()

#     # Convertir los resultados de la consulta en un diccionario
#     results = []
#     for row in data:
#         result = {}
#         result['region_name'] = row[0]
#         result['code'] = row[1]
#         result['year'] = row[2]
#         result['total_kg_nitrogen_per_hectare'] = row[3]
#         result['total_kg_phosphorous_per_hectare'] = row[4]
#         result['total_kg_per_potassium_hectare'] = row[5]
#         results.append(result)

#     return jsonify(results)





# @app.route('/fertilizers', methods=['GET'])
# def get_fertilizers_by_region():
#     region_name = request.args.get('region_name')
#     cur = mysql.connection.cursor()
#     cur.execute(SQLQueries.get_all_fertilizers_for_region_query, (region_name))
#     data = cur.fetchall()
#     cur.close()

#     # Convertir los resultados de la consulta en un diccionario
#     results = []
#     for row in data:
#         results.append({
#             'region_name': row[0],
#             'code': row[1],
#             'year': row[2],
#             'total_kg_nitrogen_per_hectare': row[3],
#             'total_kg_phosphorous_per_hectare': row[4],
#             'total_kg_potassium_per_hectare': row[5]
#         })

#     return jsonify(results)




# @app.route('/fertilizers/<string:region>', methods=['GET'])
# def get_fertilizers_by_region(region):
#     cur = mysql.connection.cursor()
#     cur.execute(SQLQueries.get_all_fertilizers_for_region_query.format(region_name = region))
#     data = cur.fetchall()
#     cur.close()

#     return jsonify(data)


# Ruta de la API para obtener los datos de fertilizers por región
# @app.route('/fertilizers/<string:region>', methods=['GET'])
# def get_fertilizers_by_region(region):
#     cur = mysql.connection.cursor()
#     cur.execute(f'''SELECT * FROM regions_fertilizers_years WHERE region_name = '{region}' ''')
#     data = cur.fetchall()
#     cur.close()

#     return jsonify(data)

# Ruta de la API para obtener los datos de fertilizers por año
@app.route('/fertilizers/<int:year>', methods=['GET'])
def get_fertilizers_by_year(year):
    cur = mysql.connection.cursor()
    cur.execute(f'''SELECT * FROM regions_fertilizers_years WHERE year = {year} ''')
    data = cur.fetchall()
    cur.close()

    return jsonify(data)


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()
# if __name__ == '__main__':
#     app.run(debug=True)
