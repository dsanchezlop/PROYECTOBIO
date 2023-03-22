import pandas as pd
import zipfile
import requests
from   pathlib import Path
import os

# url to download the zip with the .csv
# file route -> specifical where i go put the zip i download
# request -> download the zip
current_dir: Path = Path(__file__).parent
url = "https://figshare.com/ndownloader/articles/19105049/versions/1"
file_route: Path = current_dir/ 'download.zip'
response = requests.get(url)

with open(file_route, "wb") as handle:
    handle.write(response.content)

# unzip
with zipfile.ZipFile('download.zip', 'r') as zip_ref:
    zip_ref.extractall('download')

# name of the .zip
route_handle_zip = 'download.zip'
# remove the download.zip
os.remove(route_handle_zip)

# remove with a for all the usless files from folder "download"
folder_path = 'download'
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        continue
    else:
        os.remove(os.path.join(folder_path, filename))

# read the csv i dowloand
data = pd.read_csv('download/NNI_Database.csv')
# drop usless columns of the csv
data = data.drop(['DOI', 'Repetitions', 'Experimental.design', 'Paper', 'W_CV', 'W_LSD', 'W_SE_min', 'W_SE_Max', 'Row_Space', 'Water_applied', 'Sampling_time', 
                    'Observation','Nobs%', 'Npred%', 'Nconc_LSD', 'Nupt_kg_ha', 'Nconc_SE_min', 'Nconc_SE_Max', 'Nupt_SE_min', 'Nupt_SE_Max', 'W_ton_ha', 'Sites',
                    'Genotype', 'Sowing.Date', 'Harvest_Date'], axis=1)

# Relete unnecessary information from the year column
data['Year'] = data['Year'].str.replace('Autumn ', '')
data['Year'] = data['Year'].str.replace('Early spring ', '')
data['Year'] = data['Year'].str.replace('Summer ', '')
data['Year'] = data['Year'].str.replace('Late spring ', '')
data['Year'] = data['Year'].str.split(' - ').str[0]
data['Year'] = data['Year'].str.split('-2').str[0]
data['Year'] = data['Year'].str.split('/ ').str[0]
data['Year'] = data['Year'].str.replace('/2007', '')

# drop NA's from specific columns
data = data.dropna(subset=['Year'])
data = data.dropna(subset=['Country'])
data = data.dropna(subset=['Treatment'])

data['Treatment'] = data['Treatment'].str.strip()
data['Water'] = data['Water'].fillna('No irrigation data')
data['Nrates_kg_ha'] = data['Nrates_kg_ha'].astype(float)
data = data.rename(columns={'Treatment': 'Nitrates'})

print(data)
# export new csv
data_csv = data.to_csv("nit_by_flora_ed.csv", index=False)
