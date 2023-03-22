import pandas as pd
import mysql.connector

# Leer archivo CSV con pandas
df = pd.read_csv('../data/Nitrogen.csv')

# Establecer conexión a la base de datos MySQL
cnx = mysql.connector.connect(user='provenusr', password='provenpass',
                               host='localhost',
                               database='data_fertilizers')
cursor = cnx.cursor()

# Iterar sobre las filas del DataFrame y cargar los datos en las tablas SQL
for index, row in df.iterrows():
    # Cargar datos en tabla Entity
    query = "INSERT INTO entity (entity_name, code) VALUES ('%s', '%s')" % (row['Entity'], row['Code'])
    cursor.execute(query)

    # # Cargar datos en tabla Nutrient
    # query = "INSERT INTO Nutrient (nutrient) VALUES ('%s')" % (row['Nutrient nitrogen N (total) | 00003102 || Use per area of cropland | 005159 || kilograms per hectare'])
    # cursor.execute(query)

    # # Cargar datos en tabla Year
    # query = "INSERT INTO Year (year) VALUES (%s)" % (row['Year'])
    # cursor.execute(query)

    # # Cargar datos en tabla Data
    # query = "INSERT INTO EntityNutrientYear (entity, nutrient, year) \
    #          VALUES ('%s', '%s', %s)" % (row['Entity'], row['Nutrient nitrogen N (total) | 00003102 || Use per area of cropland | 005159 || kilograms per hectare'], row['Year'])
    # cursor.execute(query)

# Confirmar cambios y cerrar conexión a la base de datos
cnx.commit()
cursor.close()
cnx.close()
