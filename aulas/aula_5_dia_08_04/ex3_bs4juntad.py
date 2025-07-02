import requests
from bs4 import BeautifulSoup

#buscar notícias em sites simples, pag principal

url = "https://g1.globo.com"

resposta = requests.get(url, headers={"User-Agent": {Mozilla/5.0}})
soup = BeautifulSoup(resposta.text, "html.parser")

# ao trazer informalções do status_code traz headers - cabeçalho da pag(status, como acessar a pag(get, put), informações de como é acessado (geralmnete usa agente para acessar que é user.agent - vai passar este, e nele interpreta o que tem no site))
# então request carrega o url e no headers, pegar o user-agent - mozia faz a conversão (acha apertando f12 ou 2, ver - ir em network e ver headers)
#soup carrega tudo
#para ler manchete(variável) - para cada manchete no soup.find_all("a", class="feed-post-link") todas tags a, verificar se tem classe a classe feed-post-link e retornar - vê no cód fonte do link aberto

for manchete in soup.find_all("a", class_ = "feed-post-link"):
    print(manchete.text.strip())