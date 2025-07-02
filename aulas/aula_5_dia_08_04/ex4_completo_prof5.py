'''
Coletar os títulos dos livros
'''

import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com'
resposta = requests.get(url)
soup = BeautifulSoup(resposta.text,'html.parser')

titulos = soup.find_all('h3')
for titulo in titulos:
    print(titulo.a['title'])
