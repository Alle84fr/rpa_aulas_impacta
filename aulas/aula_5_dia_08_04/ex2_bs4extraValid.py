#validar se pag está carregando corretamente
#mostra estatus de retorno - se tiver tudo certo 200
# para ver se a pag está ou não online

import requests

# verificar status da pag web

url = "https://google.com"
#url de quem quero validar

resposta = requests.get(url)

#agora que tem requests ver o que quero fazer com a resposta
# se o status code for igual a 200 então sigo cód, caso contrário
# https://httpstatusdogs.com/
# https://http.cat/
# estes são sites que mostram os cód de erros

if resposta.status_code == 200:
    print({"mensagem": "ok", "retorno": "página online"}), 200
    # ERRO RECORRETE
    # print("mensagem": "ok", "retorno": "página online") - dá erro porque está retornando um dict, deve ter {}
else:
    print({"mensagem": "Not Found", "retorno": "pagina não encontrada"})

