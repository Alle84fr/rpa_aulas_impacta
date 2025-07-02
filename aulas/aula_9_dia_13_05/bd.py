# 1° importar bibliotecas
import requests
# pega requisição e retorna - get
import sqlite3
# banco de dados sqlite - vem com py, então não tem pip - banco relacional 

# para reconhecer/corrigir caracteres especiais
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# requisição e guarda dos dados
pais = "japan"
url = f"https://restcountries.com/v3.1/name/{pais}"
resposta = requests.get(url)
dados = resposta.json()

info = dados[0]
nome = info["name"]["common"]
capital = info["capital"][0] if "capital" in info else "N/A" 
# ERRO capital = info["capital"],[0] if "capital" in info else "N/A" NÃO TEM VIRGULA ENTRE CHAVE E POSIÇÃO
regiao = info["region"]
populacao = info["population"]
print(f"""Dados extraidos da api:
Nome: {nome}
Capital {capital}
Região: {regiao}
População: {populacao}""")

# 2° criar e conectar com bd

# criar um arquivo vazio
conexao = sqlite3.connect("paises.bd")
cursor = conexao.cursor() 

# criar tabela - somente se não tiver a tabela
cursor.execute ("""
                CREATE TABLE IF NOT EXISTS paises(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    capital TEXT,
                    regiao TEXT,
                    populacao INTEGER)""")                              #executa comando sql
# EXISTS com S no final

# Inserir informações coletadas
cursor.execute ("""
                INSERT INTO paises(
                    nome,
                    capital,
                    regiao,
                    populacao)
                VALUES(?,?,?,?)""",(nome, capital, regiao, populacao))
                                              #geralemente coloca ? nos valores, estes valores são parâmetros, o ? é para parâmetro, após
                                              # VALUES COM S NO FINAL
conexao.commit() # efetivar a ação

print("\nDados inseridos no banco - executar select")
cursor.execute("SELECT * FROM paises")
for linha in cursor.fetchall():
    print(linha)

#fehando conexão
conexao.close

# consultar os dados inseridos







#  requests.get retorn url

#percorrer todos os paises

for pais in dados:
    nome = pais ["name"]["common"]
    capital = pais.get("capital", ["Sem capital"])[0]         #caso não ter capital - ["Sem capital"]
    print(f"Paises: {nome} - Capital: {capital} ")


#print(f"Capital : {info["capital"]}") - retorno fica Capital : ['Brasília']
#print print(f"Capital : {info["capital"][0]}") retorno Capital : Brasília