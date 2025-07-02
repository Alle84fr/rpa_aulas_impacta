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

pais = "brazil"
url = f"https://restcountries.com/v3.1/name/{pais}"
resposta = requests.get(url)
dados = resposta.json()
#  requests.get retorn url

info = dados[0]
# print(f"Nome: {info["name"]["common"]}")
# print(f"Capital : {info["capital"][0]}")
# print(f"Região : {info ["region"]}")
# print(f"População : {info ["population"]}")
print(dados)

#print(f"Capital : {info["capital"]}") - retorno fica Capital : ['Brasília']
#print print(f"Capital : {info["capital"][0]}") retorno Capital : Brasília