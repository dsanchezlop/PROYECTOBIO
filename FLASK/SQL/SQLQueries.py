# Info Fertilizers Data

select_all_info_fertilizers_query: str = """SELECT * FROM regions_fertilizers_years"""
# get_all_fertilizers_for_region_query: str = "SELECT * FROM regions_fertilizers_years WHERE region_name = {region_name} "
# get_fertilizers_for_region_and_year_query: str = "SELECT * FROM regions_fertilizers_years WHERE region_name = {region_name} AND year = {year} "
# get_fertilizers_for_region_and_year_query: str = "SELECT * FROM regions_fertilizers_years WHERE region_name = {region_name} AND year = {year} "


# get_fertilizers_for_region_and_year_query.format(region_name = 'xxx', year=2020)

get_all_fertilizers_by_region_query: str = "SELECT * FROM regions_fertilizers_years WHERE region_name = %s"
get_all_fertilizers_by_year_query: str = "SELECT * FROM regions_fertilizers_years WHERE year = %s"
get_fertilizers_by_region_and_year_query: str = "SELECT * FROM regions_fertilizers_years WHERE region_name = %s AND year = %s "
get_fertilizers_by_region_year_start_year_end: str = "SELECT * FROM regions_fertilizers_years WHERE region_name = %s AND year BETWEEN %s AND %s "




get_all_fertilizers_by_region_query2: str = "SELECT * FROM regions_fertilizers WHERE region_name = %s"
get_all_fertilizers_by_region_query3: str = "SELECT * FROM regions WHERE region_name = %s"

# get_all_fertilizers_by_region_query4: str = "SELECT regions.region_name, regions_fertilizers_flora.year, fertilizers.name_fertilizer, flora.name_flora, regions_fertilizers_flora.amount, regions_fertilizers_flora.unit \
#             FROM regions_fertilizers_flora \
#             JOIN regions ON regions_fertilizers_flora.id_region = regions.id_region \
#             JOIN fertilizers ON regions_fertilizers_flora.id_fertilizer = fertilizers.id_fertilizer \
#             JOIN flora ON regions_fertilizers_flora.id_flora = flora.id_flora"




get_all_fertilizers_by_region_query4: str = "SELECT regions.region_name, regions_fertilizers_flora.year, fertilizers.name_fertilizer, flora.name_flora, regions_fertilizers_flora.amount, regions_fertilizers_flora.unit FROM regions_fertilizers_flora JOIN regions ON regions_fertilizers_flora.id_region = regions.id_region  JOIN fertilizers ON regions_fertilizers_flora.id_fertilizer = fertilizers.id_fertilizer JOIN flora ON regions_fertilizers_flora.id_flora = flora.id_flora"

