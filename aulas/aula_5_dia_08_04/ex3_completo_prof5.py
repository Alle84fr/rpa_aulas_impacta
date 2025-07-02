'''
Coletar as citações de um site
https://quotes.toscrape.com/
'''
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
resposta = requests.get(url)
soup = BeautifulSoup(resposta.text,'html.parser')

for frase in soup.find_all('span', class_='text'):
    print(frase.text)