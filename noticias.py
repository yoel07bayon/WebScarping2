"""import requests
from bs4 import BeautifulSoup
import csv
import codecs

# URL de la página de noticias que deseas scrapear
url = 'https://www.losandes.com.pe/'

# Realiza una solicitud GET a la página
response = requests.get(url)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    # Parsea el HTML de la página
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encuentra los elementos HTML que contienen las noticias
    noticias = soup.find_all('div', class_='noticia')  # Ajusta la clase según la estructura de la página

    # Crea un archivo CSV para escribir los datos
    with open('noticias.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        # Escribe las cabeceras del CSV
        csv_writer.writerow(['Titulo', 'Fecha'])
        
        # Itera a través de las noticias y extrae el titulo y la fecha
        for noticia in noticias:
            titulo = noticia.find('h2').text.strip()
            fecha = noticia.find('span', class_='fecha').text.strip()
            
            # Escribe los datos en el CSV
            
            csv_writer.writerow([titulo, fecha])
            
    print('Datos exportados a noticias.csv')"""



import requests
from bs4 import BeautifulSoup
import csv
import codecs

# URL de la página de noticias que deseas scrapear
url = 'https://www.losandes.com.pe/'

# Realiza una solicitud GET a la página
response = requests.get(url)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    # Parsea el HTML de la página
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encuentra los elementos HTML que contienen las noticias
    noticias = soup.find_all('article', class_='jeg_post')  # Ajusta la clase según la estructura de la página

    # Crea un archivo CSV para escribir los datos
    with open('noticias.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        # Escribe las cabeceras del CSV
        csv_writer.writerow(['Titulo', 'Fecha'])
        
        # Itera a través de las noticias y extrae el titulo y la fecha
        for noticia in noticias:
            # print(noticia)
            hx = noticia.find('h2')
            if not hx:
                hx = noticia.find('h3')
            titulo = hx.text.strip()
            if not titulo:
                continue
            fecha = noticia.find('div', class_='jeg_meta_date').text.strip()
            
            # Escribe los datos en el CSV
            
            csv_writer.writerow([titulo, fecha])
            
    print('Datos exportados a noticias.csv')