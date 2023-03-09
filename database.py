from flask import Flask, render_template, request, session, redirect
from flask_mysqldb import MySQL

# app = Flask(__name__)
# app.secret_key = "clave_secreta"

# # Configuramos la conexión a la base de datos MySQL
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'adminProject'
# app.config['MYSQL_PASSWORD'] = 'admin'
# app.config['MYSQL_DB'] = 'proyecto-bio'

# mysql = MySQL(app)

# print(mysql.connection)

import mysql.connector

try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="adminProject",
            password="admin",
            database="proyecto-bio"
        )
        print("Successfully connected to MySQL database")
except mysql.connector.Error as err:
        print(f"Error connecting to MySQL database: {err}")
