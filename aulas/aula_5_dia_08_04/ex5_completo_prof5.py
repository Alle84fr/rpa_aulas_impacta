'''
Buscar notícias no site:
https://g1.globo.com
'''
import requests
from bs4 import BeautifulSoup

url = 'https://g1.globo.com' # Sites reais pode exigir headers
resposta = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(resposta.text,'html.parser')

for manchete in soup.find_all('a',class_='feed-post-link'):
    print(manchete.text.strip())