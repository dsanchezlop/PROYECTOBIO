import mysql.connector as sql
import os
import csv

host: str = "localhost"
user: str = "provenusr"
password: str = "provenpass"


def connection(db_name: str = '') -> sql.MySQLConnection:
    try:
        db: sql.MySQLConnection = sql.connect(
            host = host,
            user = user,
            password = password,
            database = db_name
        )
        return db
    except Exception as e:
        print("Exception ocurred - " + format(e))
        return None

connection("fertilizers_data")
# def login(username: str, password: str):
#     try:
#         db: sql.MySQLConnection = connection("fertilizersWorldData.sql")
#         cursor = db.cursor(prepared=True)