# Info Fertilizers Data



get_fertilizers_nitrogen_by_year_query: str = "SELECT regions.code_2, regions_fertilizers.year, regions_fertilizers.amount \
            FROM regions_fertilizers \
            JOIN regions ON regions_fertilizers.id_region = regions.id_region \
            JOIN fertilizers ON regions_fertilizers.id_fertilizer = fertilizers.id_fertilizer \
            WHERE fertilizers.name_fertilizer = 'nitrogen_derived' AND regions_fertilizers.year = %s "

get_fertilizers_phosphorous_by_year_query: str = "SELECT regions.code_2, regions_fertilizers.year, regions_fertilizers.amount \
            FROM regions_fertilizers \
            JOIN regions ON regions_fertilizers.id_region = regions.id_region \
            JOIN fertilizers ON regions_fertilizers.id_fertilizer = fertilizers.id_fertilizer \
            WHERE fertilizers.name_fertilizer = 'phosphorous_derived' AND regions_fertilizers.year = %s "

get_fertilizers_potassium_by_year_query: str = "SELECT regions.code_2, regions_fertilizers.year, regions_fertilizers.amount \
            FROM regions_fertilizers \
            JOIN regions ON regions_fertilizers.id_region = regions.id_region \
            JOIN fertilizers ON regions_fertilizers.id_fertilizer = fertilizers.id_fertilizer \
            WHERE fertilizers.name_fertilizer = 'potassium_derived' AND regions_fertilizers.year = %s "

get_fertilizers_query: str = "SELECT regions.region_name, regions.code_2 ,fertilizers.name_fertilizer, regions_fertilizers.year, regions_fertilizers.amount \
            FROM regions_fertilizers \
            JOIN regions ON regions_fertilizers.id_region = regions.id_region \
            JOIN fertilizers ON regions_fertilizers.id_fertilizer = fertilizers.id_fertilizer "

get_fertilizers_regions_query: str = "SELECT regions.code_2, fertilizers.name_fertilizer, regions_fertilizers.year, regions_fertilizers.amount \
            FROM regions_fertilizers \
            JOIN regions ON regions_fertilizers.id_region = regions.id_region \
            JOIN fertilizers ON regions_fertilizers.id_fertilizer = fertilizers.id_fertilizer \
            WHERE regions.region_name = %s"

get_fertilizers_year_query: str = "SELECT regions.region_name, regions.code_2, fertilizers.name_fertilizer, regions_fertilizers.amount \
            FROM regions_fertilizers \
            JOIN regions ON regions_fertilizers.id_region = regions.id_region \
            JOIN fertilizers ON regions_fertilizers.id_fertilizer = fertilizers.id_fertilizer \
            WHERE regions_fertilizers.year = %s"

get_fertilizers_regions_and_year_query: str = "SELECT regions.region_name, fertilizers.name_fertilizer, regions_fertilizers.year, regions_fertilizers.amount, regions_fertilizers.unit \
            FROM regions_fertilizers \
            JOIN regions ON regions_fertilizers.id_region = regions.id_region \
            JOIN fertilizers ON regions_fertilizers.id_fertilizer = fertilizers.id_fertilizer \
            WHERE regions.region_name = %s AND regions_fertilizers.year = %s"


get_fertilizers_nitrogen_query: str = "SELECT regions.region_name, regions.code_2, regions_fertilizers.year, regions_fertilizers.amount\
            FROM regions_fertilizers \
            JOIN regions ON regions_fertilizers.id_region = regions.id_region \
            JOIN fertilizers ON regions_fertilizers.id_fertilizer = fertilizers.id_fertilizer \
            WHERE fertilizers.name_fertilizer = 'nitrogen_derived'"


get_fertilizers_nitrogen_by_region_query: str = "SELECT regions.code_2, regions_fertilizers.year, regions_fertilizers.amount \
            FROM regions_fertilizers \
            JOIN regions ON regions_fertilizers.id_region = regions.id_region \
            JOIN fertilizers ON regions_fertilizers.id_fertilizer = fertilizers.id_fertilizer \
            WHERE fertilizers.name_fertilizer = 'nitrogen_derived' AND regions.region_name = %s "

get_fertilizers_phosphorous_by_region_query: str = "SELECT regions.code_2, regions_fertilizers.year, regions_fertilizers.amount \
            FROM regions_fertilizers \
            JOIN regions ON regions_fertilizers.id_region = regions.id_region \
            JOIN fertilizers ON regions_fertilizers.id_fertilizer = fertilizers.id_fertilizer \
            WHERE fertilizers.name_fertilizer = 'phosphorous_derived' AND regions.region_name = %s"

get_fertilizers_potassium_by_region_query: str = "SELECT regions.code_2, regions_fertilizers.year, regions_fertilizers.amount \
            FROM regions_fertilizers \
            JOIN regions ON regions_fertilizers.id_region = regions.id_region \
            JOIN fertilizers ON regions_fertilizers.id_fertilizer = fertilizers.id_fertilizer \
            WHERE fertilizers.name_fertilizer = 'potassium_derived' AND regions.region_name = %s"

# get_fertilizers_nitrogen_query: str = "SELECT regions.region_name, regions.code_2, regions_fertilizers.year, regions_fertilizers.amount \
#             FROM regions_fertilizers \
#             JOIN regions ON regions_fertilizers.id_region = regions.id_region \
#             JOIN fertilizers ON regions_fertilizers.id_fertilizer = fertilizers.id_fertilizer \
#             WHERE fertilizers.name_fertilizer = 'nitrogen_derived'"

get_fertilizers_phosphorous_query: str = "SELECT regions.region_name, regions.code_2, regions_fertilizers.year, regions_fertilizers.amount \
            FROM regions_fertilizers \
            JOIN regions ON regions_fertilizers.id_region = regions.id_region \
            JOIN fertilizers ON regions_fertilizers.id_fertilizer = fertilizers.id_fertilizer \
            WHERE fertilizers.name_fertilizer = 'potassium_derived'"

get_fertilizers_potassium_query: str = "SELECT regions.region_name, regions.code_2, regions_fertilizers.year, regions_fertilizers.amount \
            FROM regions_fertilizers \
            JOIN regions ON regions_fertilizers.id_region = regions.id_region \
            JOIN fertilizers ON regions_fertilizers.id_fertilizer = fertilizers.id_fertilizer \
            WHERE fertilizers.name_fertilizer = 'potassium_derived'"

get_fertilizers_regions_start_year_end_year_query: str = "SELECT regions.region_name, fertilizers.name_fertilizer, regions_fertilizers.year, regions_fertilizers.amount, regions_fertilizers.unit \
            FROM regions_fertilizers \
            JOIN regions ON regions_fertilizers.id_region = regions.id_region \
            JOIN fertilizers ON regions_fertilizers.id_fertilizer = fertilizers.id_fertilizer \
            WHERE regions.region_name = %s AND regions_fertilizers.year BETWEEN %s AND %s"


get_fertilizers_regions_and_year : str = "SELECT regions.code_2, fertilizers.name_fertilizer, regions_fertilizers.amount \
             FROM regions_fertilizers \
             JOIN regions ON regions_fertilizers.id_region = regions.id_region \
             JOIN fertilizers ON regions_fertilizers.id_fertilizer = fertilizers.id_fertilizer \
             WHERE regions.region_name = %s AND regions_fertilizers.year = %s "

get_fertilizers_regions_flora: str = "SELECT regions.region_name, regions.code_2, fertilizers.name_fertilizer, regions_fertilizers_flora.year, regions_fertilizers_flora.amount \
             FROM regions_fertilizers_flora \
             JOIN regions ON regions_fertilizers_flora.id_region = regions.id_region \
             JOIN fertilizers ON regions_fertilizers_flora.id_fertilizer = fertilizers.id_fertilizer"

get_regions: str = "SELECT region_name FROM regions"