import SQL.SQLQueries as SQLQueries
import utils.utilsDB as utilsDB


# función para obtener fertilizantes dervida nitrogeno por year
def get_fertilizers_nitrogen_year(year : int):
    try:
        db = utilsDB.get_database_connection()
        cursor = db.cursor(prepared=True)
        query = SQLQueries.get_fertilizers_nitrogen_by_year_query
        cursor.execute(query, (year,))
        fertilizers = cursor.fetchall()
        json_fertilizers = []
        for f in fertilizers:
            json_fertilizer = {
                "code": f[0],
                "year": f[1],
                "amount": f[2],
            }
            json_fertilizers.append(json_fertilizer)
        return json_fertilizers
    except Exception as e:
        print("Error:", e)
        return None

# función para obtener fertilizantes dervida phosphorous por year
def get_fertilizers_phosphorous_year(year : int):
    try:
        db = utilsDB.get_database_connection()
        cursor = db.cursor(prepared=True)
        query = SQLQueries.get_fertilizers_phosphorous_by_year_query
        cursor.execute(query, (year,))
        fertilizers = cursor.fetchall()
        json_fertilizers = []
        for f in fertilizers:
            json_fertilizer = {
                "code": f[0],
                "year": f[1],
                "amount": f[2],
            }
            json_fertilizers.append(json_fertilizer)
        return json_fertilizers
    except Exception as e:
        print("Error:", e)
        return None
    

# función para obtener fertilizantes dervida potassium por year
def get_fertilizers_potassium_year(year : int):
    try:
        db = utilsDB.get_database_connection()
        cursor = db.cursor(prepared=True)
        query = SQLQueries.get_fertilizers_potassium_by_year_query
        cursor.execute(query, (year,))
        fertilizers = cursor.fetchall()
        json_fertilizers = []
        for f in fertilizers:
            json_fertilizer = {
                "code": f[0],
                "year": f[1],
                "amount": f[2],
            }
            json_fertilizers.append(json_fertilizer)
        return json_fertilizers
    except Exception as e:
        print("Error:", e)
        return None


# función para obtener fertilizantes dervida nitrogeno por region
def get_fertilizers_nitrogen_region(region : str):
    try:
        db = utilsDB.get_database_connection()
        cursor = db.cursor(prepared=True)
        query = SQLQueries.get_fertilizers_nitrogen_by_region_query
        cursor.execute(query, (region,))
        fertilizers = cursor.fetchall()
        json_fertilizers = []
        for f in fertilizers:
            json_fertilizer = {
                "code": f[0],
                "year": f[1],
                "amount": f[2],
            }
            json_fertilizers.append(json_fertilizer)
        return json_fertilizers
    except Exception as e:
        print("Error:", e)
        return None

# función para obtener fertilizantes dervida nitrogeno por region
def get_fertilizers_phosphorous_region(region : str):
    try:
        db = utilsDB.get_database_connection()
        cursor = db.cursor(prepared=True)
        query = SQLQueries.get_fertilizers_phosphorous_by_region_query
        cursor.execute(query, (region,))
        fertilizers = cursor.fetchall()
        json_fertilizers = []
        for f in fertilizers:
            json_fertilizer = {
                "code": f[0],
                "year": f[1],
                "amount": f[2],
            }
            json_fertilizers.append(json_fertilizer)
        return json_fertilizers
    except Exception as e:
        print("Error:", e)
        return None
    
# función para obtener fertilizantes dervida nitrogeno por region
def get_fertilizers_potassium_region(region : str):
    try:
        db = utilsDB.get_database_connection()
        cursor = db.cursor(prepared=True)
        query = SQLQueries.get_fertilizers_potassium_by_region_query
        cursor.execute(query, (region,))
        fertilizers = cursor.fetchall()
        json_fertilizers = []
        for f in fertilizers:
            json_fertilizer = {
                "code": f[0],
                "year": f[1],
                "amount": f[2],
            }
            json_fertilizers.append(json_fertilizer)
        return json_fertilizers
    except Exception as e:
        print("Error:", e)
        return None


# función para obtener fertilizantes nitrogeno
def get_fertilizers_nitrogen():
    try:
        db = utilsDB.get_database_connection()
        cursor = db.cursor(prepared=True)
        query = SQLQueries.get_fertilizers_nitrogen_query
        cursor.execute(query, )
        fertilizers = cursor.fetchall()
        json_fertilizers = []
        for f in fertilizers:
            json_fertilizer = {
                "region_name": f[0],
                "code": f[1],
                "year":f[2],
                "amount": f[3]
                }
            json_fertilizers.append(json_fertilizer)
        return json_fertilizers
    except Exception as e:
        print("Error:", e)
        return None

# función para obtener fertilizantes dervidados del phosphorous
def get_fertilizers_phosphorous():
    try:
        db = utilsDB.get_database_connection()
        cursor = db.cursor(prepared=True)
        query = SQLQueries.get_fertilizers_phosphorous_query
        cursor.execute(query, )
        fertilizers = cursor.fetchall()
        json_fertilizers = []
        for f in fertilizers:
            json_fertilizer = {
                "region_name": f[0],
                "code": f[1],
                "year":f[2],
                "amount": f[3]
                }
            json_fertilizers.append(json_fertilizer)
        return json_fertilizers
    except Exception as e:
        print("Error:", e)
        return None

# función para obtener fertilizantes dervidados del potassio
def get_fertilizers_potassium():
    try:
        db = utilsDB.get_database_connection()
        cursor = db.cursor(prepared=True)
        query = SQLQueries.get_fertilizers_potassium_query
        cursor.execute(query, )
        fertilizers = cursor.fetchall()
        json_fertilizers = []
        for f in fertilizers:
            json_fertilizer = {
                "region_name": f[0],
                "code": f[1],
                "year":f[2],
                "amount": f[3]
                }
            json_fertilizers.append(json_fertilizer)
        return json_fertilizers
    except Exception as e:
        print("Error:", e)
        return None



# función para obtener fertilizantes por región y año
def get_fertilizers_regions(region : str):
    try:
        db = utilsDB.get_database_connection()
        cursor = db.cursor(prepared=True)
        query = SQLQueries.get_fertilizers_regions_query
        cursor.execute(query, (region,))
        fertilizers = cursor.fetchall()
        return fertilizers
    except Exception as e:
        print("Error:", e)
        return None

def get_fertilizers_by_year(year):
    try:
        db = utilsDB.get_database_connection()
        cursor = db.cursor(prepared=True)
        query = SQLQueries.get_fertilizers_year_query
        cursor.execute(query, (year,))
        fertilizers = cursor.fetchall()
        json_fertilizers = []
        for f in fertilizers:
            json_fertilizer = {
                "region_name": f[0],
                "code": f[1],
                "type":f[2],
                "amount": f[3]
                }
            json_fertilizers.append(json_fertilizer)
        return json_fertilizers
    except Exception as e:
        print("Error:", e)
        return None
    

def get_fertilizers_by_region(region):
    try:
        db = utilsDB.get_database_connection()
        cursor = db.cursor(prepared=True)
        query = SQLQueries.get_fertilizers_regions_query
        cursor.execute(query, (region,))
        fertilizers = cursor.fetchall()
        json_fertilizers = []
        for f in fertilizers:
            json_fertilizer = {
                "code": f[0],
                "type":f[1],
                "year":f[2],
                "amount": f[3]
                }
            json_fertilizers.append(json_fertilizer)
        return json_fertilizers
    except Exception as e:
        print("Error:", e)
        return None

# función para obtener fertilizantes por región entre dos años
def get_fertilizers_by_region_and_year_start_year_end(region : str, year_start : int, year_end : int):
    try:
        db = utilsDB.get_database_connection()
        cursor = db.cursor(prepared=True)
        query = SQLQueries.get_fertilizers_regions_start_year_end_year_query
        cursor.execute(query, (region, year_start, year_end))
        fertilizers = cursor.fetchall()
        return fertilizers
    except Exception as e:
        print("Error:", e)
        return None
    


# función para obtener fertilizantes por región y año
def get_fertilizers_by_region_and_year(region : str, year : int):
    try:
        db = utilsDB.get_database_connection()
        cursor = db.cursor(prepared=True)
        query = SQLQueries.get_fertilizers_regions_and_year
        cursor.execute(query, (region, year))
        fertilizers = cursor.fetchall()
        json_fertilizers = []
        for f in fertilizers:
            json_fertilizer = {
                "code": f[0],
                "type":f[1],
                "amount": f[2]
                }
            json_fertilizers.append(json_fertilizer)
        return json_fertilizers
    except Exception as e:
        print("Error:", e)
        return None
    

# función para obtener fertilizantes por región y año de flora
def get_fertilizers_flora_by_region_and_year():
    try:
        db = utilsDB.get_database_connection()
        cursor = db.cursor(prepared=True)
        query = SQLQueries.get_fertilizers_regions_flora
        cursor.execute(query, )
        fertilizers = cursor.fetchall()
        json_flora_fert = []
        for f in fertilizers:
            json_flora = {
                "region_name": f[0],
                "code":f[1],
                "type":f[2],
                "year": f[3],
                "amount": f[4]
                }
            json_flora_fert.append(json_flora)
        return json_flora_fert
        
    except Exception as e:
        print("Error:", e)
        return None
    
# función para obtener fertilizantes por región y año de flora
def get_fertilizers_regions_all_data():
    try:
        db = utilsDB.get_database_connection()
        cursor = db.cursor(prepared=True)
        query = SQLQueries.get_fertilizers_query
        cursor.execute(query, )
        fertilizers = cursor.fetchall()
        json_fertilizers = []
        for f in fertilizers:
            json_fertilizer = {
                "region_name": f[0],
                "code":f[1],
                "type":f[2],
                "year": f[3],
                "amount": f[4]
                }
            json_fertilizers.append(json_fertilizer)
        return json_fertilizers
    except Exception as e:
        print("Error:", e)
        return None
    


# función para obtener fertilizantes por región y año de flora
def get_fertilizers_nitrogen_all_data():
    try:
        db = utilsDB.get_database_connection()
        cursor = db.cursor(prepared=True)
        query = SQLQueries.get_fertilizers_nitrogen_query
        cursor.execute(query, )
        fertilizers = cursor.fetchall()
        json_fertilizers = []
        for f in fertilizers:
            json_fertilizer = {
                "region_name": f[0],
                "code":f[1],
                "year": f[2],
                "amount": f[3]
                }
            json_fertilizers.append(json_fertilizer)
        return json_fertilizers

    except Exception as e:
        print("Error:", e)
        return None