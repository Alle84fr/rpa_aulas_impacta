#Bibliotecas usadas: requests, BeautifulSoup, pandas, openpyxl
#importando as bibliotecas
import requests
import pandas as pd
from bs4 import BeautifulSoup
from openpyxl import load_workbook
from openpyxl.styles import Font

#Função para extrair as informações da página web
def extrair_dados(url_base, url_pagina):
    reposta = requests.get(url_base + url_pagina)
    soup = BeautifulSoup(reposta.text, 'html.parser')
    
    livros = soup.find_all('article', class_='product_pod')
    
    dados = []
    for livro in livros:
        titulo = livro.h3.a['title']
        preco = livro.find('p', class_='price_color').text
        disponibilidade = livro.find('p', class_='instock availability').text
        link = url_base + livro.h3.a['href']
        
        dados.append({
            'Título': titulo,
            'Preço': preco,
            'Disponibilidade':disponibilidade,
            'Link': link
        })
    return dados

#1 URL base
url_base = 'https://books.toscrape.com/'
todos_os_livros = []

for pagina in range(1,4):
    if pagina == 1:
        url_pagina = 'index.html'
    else:
        url_pagina = f'catalogue/page-{pagina}.html'
    livros_pagina = extrair_dados(url_base,url_pagina)
    todos_os_livros.extend(livros_pagina)

##- Criar um dataframe
df = pd.DataFrame(todos_os_livros)

#5- Salvar Excel
df.to_excel('Relatorio_livros.xlsx',index=False, engine='openpyxl')
print("Arquivo Salvo")
