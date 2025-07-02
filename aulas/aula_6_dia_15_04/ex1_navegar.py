import requests
from bs4 import BeautifulSoup

base_url = "https//books.toscrape.com/catalogue/page-{}.hrml"

#visitar as 3 primeiras pags

for pag in range(1,4):
    url = base_url.format(pag)
    print(f"\n página {pag} - {url}")
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parse")
    
    livros = soup.find_all("h3")
    for livro in livros:
        titulo = livro.find("a")["title"]
        print("Titulo", titulo)