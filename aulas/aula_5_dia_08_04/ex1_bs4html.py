# bibliotecas para manipular site
#automação de tarefas repetitivas , 
# web scraping - extrair informaçõe de pg - ex, pegar preço, notícias, informações - é mais para pag estáticas
# beathifulSpup - extrair dados de html e css - NAVEGA PELOS COMPONENTES, TAG, ATRIBUTOS, SELETORES CSS - deve conhecer um pouco de html
# request - protocolo http - utilização de get, post, delete, put
# response - devolução da respota do url
# beathiful pega a resposta do request edivide e depois podemos pesquisar e usar como desejamos
# bs4 - beathiful soup só usa html o que não está no html o request retorna - tem que ter html pronto

from bs4 import BeautifulSoup

html = '''
    <htm>
        <bodu>
            <h1> Saluton Mondo do RPA </h1>
            <p> Analisando a biblioteca de exxtração de dados bsp4 </p>
            <p> Analisando soup.find("p").text - pega apenas 1° p </p>
            <p> Analisando soup.findall("p").text - pega todos os p </p>
        </bodu> 
    </htm>
'''
#as '''como se fosse comentário, para carregar texto formatdo ''' 

soup = BeautifulSoup(html, "html.parser")

#html-parser irá divir a html e ler atributos, tags, etc
#html é a estrutura usada

print(" ")
print(soup.h1.text)
print(" ")
print(soup.find("p").text)    
#procura a tag p - pega apenas a 1° ocorrência da tag, lendo de cima para baixo
# findall - pega todas as 
print(" ")

todos = soup.find_all('p') 

print(todos)
#retorno na forma de lista, que é o que é o todos 