#requeste faz requisição, todo conteúdo do site

import requests


#fazer uma requisição para uma api rest

url = "https:api.agify.io/?name=AulaREst"
resposta1 = requests.get(url)

dados = resposta1.json()
print(dados)

# site para teste - https://httpbin.org/post