# Imports
from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL
from config import config
import hashlib
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import utils.utils as utils
import SQL.SQLQueries as SQLQueries

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config['CORS_HEADERS'] = 'Content-Type'
conexion = MySQL(app)
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

# API USERS DANI
@app.route('/users')
def users():
    try:
        cursor = conexion.connection.cursor()
        sql = 'SELECT * FROM users WHERE role = 2'
        cursor.execute(sql)
        datos = cursor.fetchall()
        users = []
        for fila in datos:
            user ={'user_id':fila[0] ,'username': fila[1], 'email': fila[5]}
            users.append(user)
        return jsonify({'users':users})
    except Exception as ex:
        return jsonify({'error':'error'})

@app.route('/delete-user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        cursor = conexion.connection.cursor()
        sql = 'DELETE FROM users WHERE id = %s'
        cursor.execute(sql, (user_id,))
        conexion.connection.commit()
        return jsonify({'message': 'User deleted successfully'})
    except Exception as ex:
        return jsonify({'error': 'Error deleting user'})


@app.route('/login', methods=['POST'])
def login():
    print("Received login request...")

    # Get user data from request
    username = request.json['username']
    password = request.json['password']
    password = hashlib.sha256(password.encode()).hexdigest()

    # Check if user exists in database
    cursor = conexion.connection.cursor()
    query = "SELECT * FROM users WHERE username = %s AND passw = %s"
    values = (username, password)
    cursor.execute(query, values)
    user = cursor.fetchone()
    cursor.close()

    if user:
        response = jsonify({'username': user[1], 'role': user[6]})
        return response
    else:
        return jsonify({'error': 'Invalid username or password.'}), 401


@app.route('/register', methods=['POST'])
def register():
    # Get user data from request
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    surname = request.json['surname']
    email = request.json['email']
    password = hashlib.sha256(password.encode()).hexdigest()

    cursor = conexion.connection.cursor()
    query = "SELECT * FROM users WHERE username = %s"
    values = (username,)
    cursor.execute(query, values)
    user = cursor.fetchone()
    cursor.close()

    if user:
        return jsonify({'error': 'User not available'}), 401
    else:
        cursor2 = conexion.connection.cursor()
        query = "SELECT * FROM users WHERE email = %s"
        values = (email,)
        cursor2.execute(query, values)
        emailCheck = cursor2.fetchone()
        cursor2.close()

        if emailCheck:
            return jsonify({'error': 'Email not available'}), 401
        else:
            try:    
                cursor3 = conexion.connection.cursor()
                query = 'INSERT INTO users (username, passw, name, surname, email, role) VALUES (%s, %s, %s, %s, %s, 2)'
                values = (username, password, name, surname, email)
                print('Inserting values:', values)
                cursor3.execute(query, values)
                print('Rows affected:', cursor3.rowcount)
                conexion.connection.commit()
                cursor3.close()
                return jsonify({'message': 'User registered successfully'})
            except Exception as e:
                print(e)
                return jsonify({'error': 'Error registering user'}), 500

# def getRole(username):
#     try:
#         cursor = conexion.connection.cursor()
#         sql = 'SELECT role FROM `users` WHERE username = %s';
#         values =(username,)
#         cursor.execute(sql, values)
#         datos = cursor.fetchone()
#         return datos
#     except Exception as e:
#         return

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    sender_email = "fertimpact@gmail.com"
    sender_password = "elbichosu"
    recipient_email = "fertimpact@gmail.com"
    subject = data['subject']
    body = data['message']

    try:
        
        # Set up SMTP connection
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, sender_password)

        # Create email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Send email
        server.sendmail(sender_email, recipient_email, message.as_string())

        # Close SMTP connection
        server.quit()
        return jsonify({'Message':'Email sent'})
    except Exception as e:
        return jsonify({'Error':'Error, email not sent'})

def not_found(error):
    return '<h1>Página no encontrada</h1>', 404


# API FERTILIZERS ALBERT

@app.route("/")
def homepage():
    return render_template("index.html")


# route to obtain nitrogen-derived fertilisers by year.
@app.route('/api/fertilizers-nitrogen-year', methods=['GET'])
def get_fertilizers_nitrogen_year():
    year = request.args.get('year')
    if year:
        if not year.isdigit():
            return "The year should be a number.", 400
        try:
            fertilizers = utils.get_fertilizers_nitrogen_year(int(year))
            if fertilizers:
                return jsonify(fertilizers), 200
            else:
                return "No fertiliser data were found for the year provided.", 404
        except Exception as e:
            return f"An error occurred while obtaining fertiliser data: {str(e)}", 500
    else:
        return "Please provide a year to obtain fertiliser data.", 400
    

# route to obtain phosphorous-derived fertilisers by year.
@app.route('/api/fertilizers-phosphorous-year', methods=['GET'])
def get_fertilizers_phosphorous_year():
    year = request.args.get('year')
    if year:
        if not year.isdigit():
            return "The year should be a number.", 400
        try:
            fertilizers = utils.get_fertilizers_phosphorous_year(int(year))
            if fertilizers:
                return jsonify(fertilizers), 200
            else:
                return "No fertiliser data were found for the year provided.", 404
        except Exception as e:
            return f"An error occurred while obtaining fertiliser data: {str(e)}", 500
    else:
        return "Please provide a year to obtain fertiliser data.", 400
    
# route to obtain potassium-derived fertilisers by year.
@app.route('/api/fertilizers-potassium-year', methods=['GET'])
def get_fertilizers_potassium_year():
    year = request.args.get('year')
    if year:
        if not year.isdigit():
            return "The year should be a number.", 400
        try:
            fertilizers = utils.get_fertilizers_potassium_year(int(year))
            if fertilizers:
                return jsonify(fertilizers), 200
            else:
                return "No fertiliser data were found for the year provided.", 404
        except Exception as e:
            return f"An error occurred while obtaining fertiliser data: {str(e)}", 500
    else:
        return "Please provide a year to obtain fertiliser data.", 400



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
    app.config.from_object(config['development'])
    app.register_error_handler(404, not_found)
    app.run()
