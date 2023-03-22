import pandas as pd

# Leer los archivos CSV
df_nitrogen = pd.read_csv("../data/Nitrogen.csv")
df_phosphorous = pd.read_csv("../data/Phosphorous.csv")
df_potassium = pd.read_csv("../data/Potassium.csv")

# Combinar las columnas de total de fosforo y total de potassio con el dataframe de nitrogeno basado en las columnas "entity", "code" y "year"
df_resultado = df_nitrogen.merge(df_phosphorous[['Entity', 'Code', 'Year', 'Total_Phosphorous']], on=['Entity', 'Code', 'Year'], how='left')
df_resultado = df_resultado.merge(df_potassium[['Entity', 'Code', 'Year', 'Total_Potassium']], on=['Entity', 'Code', 'Year'], how='left')

# Guardar el resultado en un nuevo archivo CSV
df_resultado.to_csv("fertilizers.csv", index=False)
