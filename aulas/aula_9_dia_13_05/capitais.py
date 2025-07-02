# https://restcountries.com/
# api rest - softwares e sitres dão informações em formato json, para consulta
# na lateral são os endpoints que o site dá
# https://restcountries.com/v3.1/all - informações sobre paises

import requests
#pega requisição e retorna - get
import sys
import io
# para reconhecer caracteres especiais

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


url = f"https://restcountries.com/v3.1/all"
resposta = requests.get(url)
dados = resposta.json()
#  requests.get retorn url

#percorrer todos os paises

for pais in dados:
    nome = pais ["name"]["common"]
    capital = pais.get("capital", ["Sem capital"])[0]         #caso não ter capital - ["Sem capital"]
    print(f"Paises: {nome} - Capital: {capital} ")


#print(f"Capital : {info["capital"]}") - retorno fica Capital : ['Brasília']
#print print(f"Capital : {info["capital"][0]}") retorno Capital : Brasília