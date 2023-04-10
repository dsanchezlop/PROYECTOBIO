import requests
from bs4 import BeautifulSoup

url = "https://ourworldindata.org/fertilizers" #canviar

# Función para descargar y guardar archivos CSV
def download_and_save_csv(csv_url, filename):
    response = requests.get(csv_url)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(response.text)

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Encontrar el enlace al dataset de Nitrogen en la sección "DOWNLOAD"
download_section = soup.find("details", {"id": "downloads"})
download_section = download_section.find_next("ul")
nitrogen_link = None

# for link in download_section.find_all("a", href=True):
#     if "nitrogen" in link["href"].lower(): #justificar metode amb clau
#         nitrogen_link = link["href"]
#         break

if nitrogen_link:
    print(f"Descargando nitrogen desde {nitrogen_link}")
    download_and_save_csv(nitrogen_link, "nitrogen_fertilizer.csv")
    print("nitrogen_fertilizer.csv guardado correctamente")
else:
    print("No se pudo encontrar el archivo CSV de nitrogen")



