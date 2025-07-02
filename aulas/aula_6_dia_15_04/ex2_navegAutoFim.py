import requests
from bs4 import BeautifulSoup

# #corrogir caracteres especiais
# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# pagina = 1
# encontrou = True

# # não sabe quantidade de pags
# while encontrou:
#     url = f"https://books.toscrape.com/catalogue/page-{pagina}.html"
    
#     response = requests.get(url)
    
#     if response.status_code != 200:
#         break
#     # pag inexistem - fim da navegação
#     # para while
    
#     soup = BeautifulSoup(response.text, "html.parse")
#     livros = soup.find_all("h3")
    
#     # verificar se tem conteúdo
    
#     if not livros:
#         break
    
#     print(f"\n Pagina {pagina}")
    
#     for livro in livros:
#         titulo = titulo.find("a")["title"]
#         print("livros: ", titulo)
        
#     pagina += 1
    

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

pagina = 1
encontrou = True

while encontrou:
    url = f"https://books.toscrape.com/catalogue/page-{pagina}.html"
    response = requests.get(url)
    
    if response.status_code != 200:
        break  #Página inexistente,
    
    soup = BeautifulSoup(response.text, "html.parser")
    livros = soup.find_all("h3")
    
    if not livros:
        break
    
    print(f"\n Página {pagina}")
    for livro in livros:
        titulo = livro.find("a")["title"]
        print("Livro: ", titulo)
    pagina +=1