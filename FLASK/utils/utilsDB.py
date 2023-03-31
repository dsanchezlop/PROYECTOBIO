import mysql.connector



# host: str = "localhost"
# user: str = "provenusr"
# password: str = "provenpass"

def get_database_connection():
    db = mysql.connector.connect(
        host="localhost",
        user="provenusr",
        password="provenpass",
        database="projectFertFloraImpact_db"
    )
    return db

