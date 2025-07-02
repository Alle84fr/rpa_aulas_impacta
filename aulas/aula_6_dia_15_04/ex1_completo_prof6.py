#dependencia
# pip install requests beautifulsoup4 pandas reportlab openpyxl

#Exemplo 1 – Navegar entre várias páginas e coletar livros

import requests
from bs4 import BeautifulSoup

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

# Vamos visitar as 3 primeiras páginas
for pagina in range(1, 4):
    url = base_url.format(pagina)
    print(f"\n🟢 Página {pagina} - {url}")

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    livros = soup.find_all("h3")

    for livro in livros:
        titulo = livro.find("a")["title"]
        print("📘", titulo)