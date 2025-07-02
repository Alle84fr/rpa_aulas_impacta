# repostlab permite formatar e gerar pdf

import requests
from bs4 import BeautifulSoup
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# função extrair dados de livros da pag web
def extrairLivros (pag):
    try:
        url = f"https://books.toscrape.com/catalogue/page-{pag}.html"
        response = requests.get(url)
        
        if response.status_code != 200:
            return [] #lista vazia
        soup = BeautifulSoup(response.text, "html.parser")  # estava sem r no final soup = BeautifulSoup(response.text, "html.parse")
        livros = [] #crei lista vazia para dar append dos dados
        
        for artigo in soup.find_all("article", class_="product_pod"): #percorre o soup, pega o quee tem no articulo e 
            titulo = artigo.h3.a["title"]
            preco = artigo.find("p", class_="price_color").text.strip()
            disponibilidade = artigo.find("p", class_="instock availabitity").text.strip()
            livros.append({
                "titulo": titulo,
                "preço": preco,
                "Disponibilidade": disponibilidade
            })
        return livros
    
    except Exception as e:
        print(f"Erro na extração da pag {pag}: {e}")
        return []
    
# fora da função

print(extrairLivros(5)) # chama função e pega pag 5