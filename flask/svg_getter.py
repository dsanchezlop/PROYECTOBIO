import xml.etree.ElementTree as ET
import json

# Open the SVG file
svg_file = open('world.svg', 'r')

# Parse the SVG file
tree = ET.parse(svg_file)
root = tree.getroot()

# Create an empty dictionary to store the country information
country_data = {}

# Loop through all the <path> elements in the SVG file
for path in root.iter('{http://www.w3.org/2000/svg}path'):
    # Get the country name and ID attributes
    name = path.get('data-name')
    id = path.get('id')
    # Get the path data
    path_data = path.get('d')
    # Add the country information to the dictionary
    country_data[id] = {
        'name': name,
        'path': path_data
    }

# Close the SVG file
svg_file.close()

# Write the country data to a JSON file
with open('countries.json', 'w') as outfile:
    json.dump(country_data, outfile)
