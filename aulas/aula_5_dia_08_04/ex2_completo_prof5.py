import requests
'''url = 'https://google.com'
resposta = requests.get(url)

print(resposta.text)'''

#Requisição a uma API
'''url = 'https://api.agify.io/?name=Vanderson'
resposta = requests.get(url)

dados = resposta.json()
print(dados)'''

#Enviar dados - POST
'''url = 'https://httpbin.org/post'
dados = {'nome': 'Maria', 'idade':25}

resposta = requests.post(url,dados)
print(resposta.json())'''

#Verificar o status do site (online/offline)
url = 'https://google.com'
resposta = requests.get(url)

if resposta.status_code == 200:
    print("Site está online!")
else:
    print("Erro ao acessar o site!")