#                     _______________________________________________________________
#                     |                                                             |
#                     |                   FUNÇÃO GERAR DADOS  3/                  |
#                     |_____________________________________________________________|

import requests
import sys
import io
from def_2_print_atom import print_tela

# ___________________ CARACTERES ESPECIAIS ____________________________________

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

print_tela()

# _______________________ EXTRAÇÃO DE DADOS____________________________________

def desenhos_base():
    
    '''Função que irá percorer pela api do Studio Ghibli e coletar os 15 primeiros titulos.
        Será armazenado apenas o Título, Título original, Ano e imagem'''

    url = "https://ghibliapi.vercel.app/films"
    
    retorno = requests.get(url)
    dados = retorno.json()

    desenhos_base = []
    
    for i, desenho in enumerate(dados[:15]):
        titulo = desenho["title"]
        titulo_oficial = desenho["original_title_romanised"]
        ano = desenho["release_date"]
        imagem = desenho["image"]

        desenhos_base.append((titulo, titulo_oficial, ano, imagem))
        
    #print(f"\nTítulo: {titulo}\nTítulo Origonal: {titulo_oficial}\nAno: {ano}\nUrl da Imagem: {imagem}\n")
    
    # print da tela
    print_tela()
    
    return desenhos_base

