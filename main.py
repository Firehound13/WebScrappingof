import csv
from config import URL, URL_BASE
import requests
from bs4 import BeautifulSoup

pagina = requests.get(URL)
soup = BeautifulSoup(pagina.text, 'html-parser')
print(soup)

# Remover links inferiores
ultimos_links = soup.find(class='AlphaNav')
ultimos_links.decompose()

# Pegar o conteúdo da body text
bloco_nome_artistas = soup.find(class_='BodyText')

lista_nomes_artistas = bloco_nome_artistas.find_all('a')

print()
print(nome_artista)

print()
print(lista_nome_artistas)

for nome_artista in lista_nomes_artistas:
    nomes = nome_artista.contents[0]
    links = f"{URL_BASE}{nome_artista.get('href')}"
    print(nomes)

# Criando um arquivo csv
arquivo_csv = csv.writer(open('nome_artistas_z.csv', 'w', newline='\n'))
arquivo_csv.writerow(['Nomes_Artistas', 'URL_Artistas'])
for num_page in range(1, 5):
    paginas.append(f'https://www.nga.gov/collection/artists.html?const_startLetter=z&pageSize=30&pageNumber=1&lastFacet=const_startLetter{num_page}.htm')
arquivo_csv.writerow([nomes, links])
print(nomes)
print(links)

for url_por_pagina in paginas:
    pagina = requests.get(url_por_pagina)
    soup = BeautifulSoup(pagina.text, 'html.parser')