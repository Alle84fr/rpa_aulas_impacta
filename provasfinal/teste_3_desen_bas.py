#                     _______________________________________________________________
#                     |                                                             |
#                     |                   FUNÇÃO GERAR DADOS  3/                  |
#                     |_____________________________________________________________|

import requests
import sqlite3
import sys
import io
import pandas as pd
from openpyxl import load_workbook, Workbook
from openpyxl.styles import Font, Alignment
from bs4 import BeautifulSoup
from datetime import datetime

# ___________________ CARACTERES ESPECIAIS ____________________________________

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# _______________________ EXTRAÇÃO DE DADOS____________________________________

def desenhos_base():
    
    '''Função que irá percorer pela api do Studio Ghibli e coletar os 15 primeiros titulos.
        Será armazenado apenas o Título, Título original, Ano e imagem'''

    url = "https://ghibliapi.vercel.app/films"
    
    retorno = requests.get(url)
    dados = retorno.json()

    desenhos_base = []
    
    for desenho in dados[:16]:
        titulo = desenho["title"]
        titulo_oficial = desenho["original_title_romanised"]
        ano = desenho["release_date"]
        imagem = desenho["image"]

        desenhos_base.append((titulo, titulo_oficial, ano, imagem))
    #print(f"\nTítulo: {titulo}\nTítulo Origonal: {titulo_oficial}\nAno: {ano}\nUrl da Imagem: {imagem}\n")
    
    return desenhos_base

