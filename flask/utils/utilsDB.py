import mysql.connector

def get_database_connection():
    db = mysql.connector.connect(
        host="localhost",
        user="provenusr",
        password="provenpass",
        database="projectFertFloraImpact_db"
    )
    return db

