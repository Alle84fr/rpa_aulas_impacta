#Exemplo 2 – Navegação automática até acabar as páginas

import requests
from bs4 import BeautifulSoup

pagina = 1
encontrou_livros = True

while encontrou_livros:
    url = f"https://books.toscrape.com/catalogue/page-{pagina}.html"
    response = requests.get(url)

    if response.status_code != 200:
        break  # Página inexistente, fim da navegação

    soup = BeautifulSoup(response.text, "html.parser")
    livros = soup.find_all("h3")

    if not livros:
        break

    print(f"\n🔵 Página {pagina}")
    for livro in livros:
        titulo = livro.find("a")["title"]
        print("📕", titulo)

    pagina += 1