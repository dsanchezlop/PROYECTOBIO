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


# import requests
# from bs4 import BeautifulSoup
# import re

# url = "https://ourworldindata.org/fertilizers#potash-fertilizer"

# # Función para descargar y guardar archivos CSV
# def download_and_save_csv(csv_url, filename):
#     response = requests.get(csv_url)
#     with open(filename, 'w', encoding='utf-8') as f:
#         f.write(response.text)

# # Realizar solicitud a la página web
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")

# # Encontrar el enlace al dataset de Nitrogen en la sección "DOWNLOAD"
# nitrogen_link = None
# pattern = re.compile(r"https:\/\/.*\/nitrogen.*\.csv", re.IGNORECASE)

# for link in soup.find_all("a", href=True):
#     match = pattern.search(link["href"])
#     if match:
#         nitrogen_link = match.group()
#         break

# if nitrogen_link:
#     print(f"Descargando nitrogen desde {nitrogen_link}")
#     download_and_save_csv(nitrogen_link, "nitrogen_fertilizer.csv")
#     print("nitrogen_fertilizer.csv guardado correctamente")
# else:
#     print("No se pudo encontrar el archivo CSV de nitrogen")



# import requests
# from bs4 import BeautifulSoup

# url = "https://ourworldindata.org/fertilizers#potash-fertilizer"

# # Función para descargar y guardar archivos CSV
# def download_and_save_csv(csv_url, filename):
#     response = requests.get(csv_url)
#     with open(filename, 'w', encoding='utf-8') as f:
#         f.write(response.text)

# # Realizar solicitud a la página web
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")

# # Encontrar el enlace al dataset de Nitrogen en la sección "DOWNLOAD"
# download_section = soup.find("section", {"id": "downloads"})
# nitrogen_link = None

# for link in download_section.find_all("a", href=True):
#     if "nitrogen" in link["href"].lower():
#         nitrogen_link = link["href"]
#         break

# if nitrogen_link:
#     print(f"Descargando nitrogen desde {nitrogen_link}")
#     download_and_save_csv(nitrogen_link, "nitrogen_fertilizer.csv")
#     print("nitrogen_fertilizer.csv guardado correctamente")
# else:
#     print("No se pudo encontrar el archivo CSV de nitrogen")


# import requests
# from bs4 import BeautifulSoup

# url = "https://ourworldindata.org/fertilizers#potash-fertilizer"

# # Función para descargar y guardar archivos CSV
# def download_and_save_csv(csv_url, filename):
#     response = requests.get(csv_url)
#     with open(filename, 'w', encoding='utf-8') as f:
#         f.write(response.text)

# # Realizar solicitud a la página web
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")

# # Encontrar el botón "DOWNLOAD" y obtener el enlace de la página de descarga
# download_button = soup.find("a", class_="nav-link", href=True, text="Download")
# download_page_url = download_button["href"]

# # Realizar solicitud a la página de descarga
# download_response = requests.get(download_page_url)
# download_soup = BeautifulSoup(download_response.content, "html.parser")

# # Encontrar los enlaces CSV de Nitrogen, Phosphorous y Potassium
# csv_links = {}
# anchor_tags = download_soup.find_all("a", href=True)

# for tag in anchor_tags:
#     if 'nitrogen' in tag['href'].lower():
#         csv_links['nitrogen'] = tag['href']
#     elif 'phosphorous' in tag['href'].lower():
#         csv_links['phosphorous'] = tag['href']
#     elif 'potassium' in tag['href'].lower() or 'potash' in tag['href'].lower():
#         csv_links['potassium'] = tag['href']

# # Descargar y guardar los archivos CSV
# for key, value in csv_links.items():
#     print(f"Descargando {key} desde {value}")
#     download_and_save_csv(value, f"{key}_fertilizer.csv")
#     print(f"{key}_fertilizer.csv guardado correctamente")

# import requests
# from bs4 import BeautifulSoup
# import re

# url = "https://ourworldindata.org/fertilizers#potash-fertilizer"

# # Función para descargar y guardar archivos CSV
# def download_and_save_csv(csv_url, filename):
#     response = requests.get(csv_url)
#     with open(filename, 'w', encoding='utf-8') as f:
#         f.write(response.text)

# # Realizar solicitud a la página web
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")

# # Encontrar los enlaces CSV
# anchor_tags = soup.find_all('a', href=re.compile('.*\.csv$'))

# # Identificar los enlaces CSV de Nitrogen, Phosphorous y Potassium
# csv_links = {}
# for tag in anchor_tags:
#     if 'nitrogen' in tag['href'].lower():
#         csv_links['nitrogen'] = tag['href']
#     elif 'phosphorous' in tag['href'].lower():
#         csv_links['phosphorous'] = tag['href']
#     elif 'potassium' in tag['href'].lower() or 'potash' in tag['href'].lower():
#         csv_links['potassium'] = tag['href']

# # Descargar y guardar los archivos CSV
# for key, value in csv_links.items():
#     print(f"Descargando {key} desde {value}")
#     download_and_save_csv(value, f"{key}_fertilizer.csv")
#     print(f"{key}_fertilizer.csv guardado correctamente")


# import requests
# from bs4 import BeautifulSoup

# # Obtener la página web
# url = 'https://ourworldindata.org/fertilizers#potash-fertilizer'
# page = requests.get(url)
# soup = BeautifulSoup(page.content, 'html.parser')

# # Encontrar los enlaces a los archivos CSV
# csv_links = {}
# for link in soup.find_all('a'):
#     href = link.get('href')
#     if href.endswith('.csv') and ('Nitrogen' in href or 'Phosphorous' in href or 'Potassium' in href):
#         csv_links[href] = link.text

# # Descargar los archivos CSV
# for href, name in csv_links.items():
#     response = requests.get(href)
#     with open(name, 'wb') as f:
#         f.write(response.content)
#         print(f'Se ha descargado el archivo {name}')
