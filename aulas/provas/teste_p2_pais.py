import requests

import sys
import io



# ___________________ CARACTERES ESPECIAIS ____________________________________

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# ___________________ EXTRAÇÃO DE DADOS DE 3 PAÍSES ____________________________________

    
local = input("🌎 Ecolhas o país que quer receber informações🧾: ")

url = f"https://restcountries.com/v3.1/name/{local}"
retorno =  requests.get(url)

dados = retorno.json()

dici = dados[0]
nome = dici["name"]["common"]
nomeOffi = dici["name"]["official"] 
capital = dici["capital"][0] if "capital" in dici else "N/A"
# se capital no dict mostre, se não capital marque como Not Available - Não disponível, não applicável
continente = dici["continents"][0] if "continents" in dici else "N/A"
regiao = dici["region"] if "region" in dici else "N/A"
subRegiao = dici["subregion"]if "subregion" in dici else "N/A"
populacao = dici["population"] if "population" in dici else "N/A"
area = dici["area"] if "area" in dici else "N/A"
fusoH = ", ". join(dici["timezones"]) if "timezones" in dici else "N/A" #aqui retorna lista, tive que converter para string
bandeira = dici["flags"]["png"] if "flags" in dici and "png" in dici["flags"] else "N/A"

# modeda é lista não dicionário então
moeda = list(dici["currencies"].values())[0] if "currencies" in dici else {"symbol": "N/A", "name": "N/A"}
simbo = moeda["symbol"]
nomeMoed = moeda["name"]

idioma = list(dici["languages"].values())[0] if "languages" in dici else "N/A"

print(f"Nome Oficial {nomeOffi}, Nome {nome} Capital {capital}\n Continente {continente} Região {regiao} Sub Região {subRegiao}\n Idioma {idioma} População {populacao}\n Área {area} Fuso Horário {fusoH}\n Moeda {simbo} {nomeMoed}\n Url bandeira {bandeira} ")