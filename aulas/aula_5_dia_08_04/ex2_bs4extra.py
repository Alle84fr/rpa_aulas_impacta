#requeste faz requisição, todo conteúdo do site

import requests

# #sempre que passar url por protocolo http ou https (se não sabe, entra no site e vê)
url = "https://google.com/"

# #resposta trará um get - retono apenas de dados
resposta = requests.get(url)

print(resposta.text)

# resposta é algo muito grande, este está funcionando

#fazer uma requisição para uma api rest

url = "https:api.agify.io/?name=AulaREst"
resposta1 = requests.get(url)

dados = resposta1.json()
print(dados)

# site para teste - https://httpbin.org/post