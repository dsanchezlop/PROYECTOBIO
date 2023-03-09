from flask import Flask, render_template, request, session, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)


# MySQL connection settings
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'adminProject'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'proyecto-bio'

mysql = MySQL(app)

with mysql.connection.cursor() as cursor:
    cursor.execute('CREATE TABLE countries (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30) PRIMARY KEY, code VARCHAR(5))')
    cursor.execute('CREATE TABLE fertilizers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30) PRIMARY KEY')
    cursor.execute('CREATE TABLE year (year DATE)')
    cursor.execute('CREATE TABLE country_fertilizer (id INT AUTO_INCREMENT PRIMARY KEY, name_country VARCHAR(30), name_fertilizer VARCHAR(30)), kg_h FLOAT, year DATE, FOREIGN KEY (name_country) REFERENCES countries(name), FOREIGN KEY (name_fertilizer) REFERENCES fertilizers(name), FOREIGN KEY (year) REFERENCES year(year)')
    cursor.execute('ALTER TABLE country_fertilizer ADD PRIMARY KEY (name_country, name_fertilizer, year);)')
    mysql.connection.commit()

# import mysql.connector

# try:
#         mydb = mysql.connector.connect(
#             host="localhost",
#             user="adminProject",
#             password="admin",
#             database="proyecto-bio"
#         )
#         print("Successfully connected to MySQL database")
# except mysql.connector.Error as err:
#         print(f"Error connecting to MySQL database: {err}")


