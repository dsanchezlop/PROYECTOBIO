# Imports
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from config import config
import hashlib
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
conexion = MySQL(app)

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/users')
def users():
    try:
        cursor = conexion.connection.cursor()
        sql = 'SELECT * FROM users WHERE role = 2'
        cursor.execute(sql)
        datos = cursor.fetchall()
        users = []
        for fila in datos:
            user ={'user_id':fila[0] ,'username': fila[1], 'passw': fila[2]}
            users.append(user)
        return jsonify({'users':users, 'msg': 'Showing all users'})
    except Exception as ex:
        return jsonify({'error':'error'})


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
        return jsonify({'message': 'User logged in successfully.'})
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
        cursor = conexion.connection.cursor()
        query = "SELECT * FROM users WHERE email = %s"
        values = (email,)
        cursor.execute(query, values)
        emailCheck = cursor.fetchone()
        cursor.close()

        if emailCheck:
            return jsonify({'error': 'Email not available'}), 401
        else:
            try:
                cursor = conexion.connection.cursor()
                query = "INSERT INTO users (username, passw, name, surname, email, role) VALUES (%s, %s, %s, %s, %s, 2)"
                values = (username, password, name, surname, email)
                print('Inserting values:', values)
                result = cursor.execute(query, values)
                print('Rows affected:', cursor.rowcount)
                cursor.close()
                return jsonify({'message': 'User registered successfully'})
            except Exception as e:
                print(e)
                return jsonify({'error': 'Error registering user'}), 500



def not_found(error):
    return '<h1>Página no encontrada</h1>', 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, not_found)
    app.run()
