import pandas as pd
import zipfile
import requests
from   pathlib import Path

current_dir: Path = Path(__file__).parent

url = "https://figshare.com/ndownloader/articles/19105049/versions/1"
ruta_destino: Path = current_dir

response = requests.get(url)

with open(ruta_destino, "wb") as archivo:
    archivo.write(response.content)

# with open("datos.csv", "wb") as f:
    # f.write(response.content)


data = pd.read_csv('nit_by_flora.csv')
data = data.drop(['DOI', 'Repetitions', 'Experimental.design', 'Paper', 'W_CV', 'W_LSD', 'W_SE_min', 'W_SE_Max', 'Row_Space', 'Water_applied', 'Sampling_time', 'Observation',
                  'Nobs%', 'Npred%', 'Nconc_LSD', 'Nupt_kg_ha', 'Nconc_SE_min', 'Nconc_SE_Max', 'Nupt_SE_min', 'Nupt_SE_Max', 'W_ton_ha'], axis=1)
data['Year'] = data['Year'].str.replace('Autumn ', '')
data['Year'] = data['Year'].str.replace('Early spring ', '')
data['Year'] = data['Year'].str.replace('Summer ', '')
data['Year'] = data['Year'].str.replace('Late spring ', '')
data['Year'] = data['Year'].str.split(' - ').str[0]
data['Year'] = data['Year'].str.split('-2').str[0]
data['Year'] = data['Year'].str.split('/ ').str[0]
data['Year'] = data['Year'].str.replace('/2007', '')

data = data.dropna(subset=['Year'])
data = data.dropna(subset=['Country'])
data = data.dropna(subset=['Treatment'])

data['Treatment'] = data['Treatment'].str.strip()
data['Water'] = data['Water'].fillna('No irrigation data')
data['Harvest_Date'] = data['Harvest_Date'].fillna('No harvest date data')
data['Sowing.Date'] = data['Sowing.Date'].fillna('No sowing date data')
data['Genotype'] = data['Genotype'].fillna('No genotype data')

# display(data)



data_csv = data.to_csv("nit_by_flora_ed.csv", index=False)



data.isna().any()