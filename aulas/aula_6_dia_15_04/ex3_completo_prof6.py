#Exemplo 3 – Navegar e extrair links de detalhes de cada item

import requests
from bs4 import BeautifulSoup

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
detalhes_base = "https://books.toscrape.com/catalogue/"

for pagina in range(1, 3):  # apenas 2 páginas para exemplo
    url = base_url.format(pagina)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    print(f"\n🌍 Página {pagina}")

    livros = soup.find_all("h3")
    for livro in livros:
        link = livro.find("a")["href"]
        titulo = livro.find("a")["title"]

        # Ajuste do link relativo
        detalhe_url = detalhes_base + link
        print(f"🔗 {titulo} → {detalhe_url}")