# navega r extrair os links

import requests
from bs4 import BeautifulSoup

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


base_url = "https://books.toscrape.com/catalogue/page-{}.html"  # navegação

detalhes_base = "https://books.toscrape.com/catalogue"  #criar link de acesso

for pag in range(1,6):  #percorre da pag 1 a 5
    #percorrer a pag, pegar o título e ao clicar nele irá concatenar com /titulodolivro
    url = base_url.format(pag)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parse")
    print(f"\n Página {pag}")
    
    livros = soup.find_all("h3")
    for livro in livros:
        link = livro.find("a")["href"]
        titulo = livro.find("a")["title"]
        
        # ajuste da rota
        
        detalhe_url = detalhes_base + link
        print(f"{titulo} --> {detalhe_url}")
        
        
# titulo do livro é um link -> https://books.toscrape.com/catalogue/ -> url dada anteriormente
# a-light-in-the-attic_1000/index.html - rota para este livro, é o título do livro