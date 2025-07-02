## <center> Atividade Treino RPA</center>

#### Regras
Desafio é desenvolver um sistema de automação que
seja capaz de coletar informações atualizadas sobre países do mundo, armazenar os dados
de forma estruturada em um banco de dados e gerar relatórios personalizados com as
principais características de cada nação.

1. Solicite ao usuário a entrada de três países para consulta;
2. Utilize a API pública disponível em https://restcountries.com/v3.1/name/{pais} para
coletar as seguintes informações:
- Nome comum e nome oficial
- Capital
- Continente
- Região e sub-região
- População
- Área total (em km2)
- Moeda principal (nome e símbolo)
- Idioma principal
- Fuso horário
- URL da bandeira
3. Armazene os dados coletados em um banco de dados SQLite local, em uma tabela
chamada 'paises';
4. Gere um relatório automatizado com todas as informações extraídas em Excel ou Word.

#### Passos

No terminal - pip install python-docx
No file from dock


#### mais

A variável pais recebe um input do usuário, que será um país

requests = biblioteca do .py que faz requisição http - a solicitação vai para servidores web e recebe respostas

A variável url recebe um url que receberá a variável pais, para poder retornar o que se deseja, no caso, informação sobre um País.

variável resposta recebe a biblioteca request com requisição tipo get (pegar, apenas retorno) da variável url. A resposta virá no formato Json - em texto bruto, que para o py é uma longa string

A variável dados irá receber a variável resposta
.json é um método transforma a respostas em dados no formato entendido pelo .py, neste caso em dicionário.
Forma de converter, por exemplo: {} vira dict, [] vira list, "string" vira str e assim vai

A variável info recebe a variável dados, que está no formato de dicionário (quer recebe requisição json para python, vindas da url). [0] diz que será acessado, a partir da 1° posição, todo o dicionário 
Resumindo - info é o dicionário completo do país
url emcaminha:
{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"name": {
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"common": "Eritrea",
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"official": "State of Eritrea",
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"nativeName": {
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"ara": {
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"official": "دولة إرتريا",
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"svg": "https://mainfacts.com/media/images/coats_of_arms/er.svg"
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;},
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"startOfWeek": "monday",
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"capitalInfo": {
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"latlng": [15.33, 38.93]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;},
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"postalCode": {
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"format": null,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"regex": null
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
},

Para ter resultado "دولة إرتريا", deve:
nomeNat = info["name"]["nativeName"]["ara"]["official"] ->1° sub-dicionário/chave que leva a outro dict, 2° chave, 3°chave e 4° chave

<span style="color: #E06D06 ;"><b> Atenção</b></span>

nomeNat = info["name"]["nativeName"]["ara"]["official"] -> estava forma irá quebrar se não tiver algum resultado

<span style="color: #4f772d;"><b> nomeNat = info.get("name", {}).get("nativeName", {}).get("ara", {}).get("official", "N/A")</b></span>

info.get("name", {}) - pega(get) no dicionário info a chave name, caso não tenha, retornará dicionário vazio. Tendo a chave

nome_comum = info.get("name", {}).get("common", "N/A") - pega nome comum

N/A = Not Available = não disponível = ausência de dados (não é vazio é ausênte, não sei explicar)

O {} está relacionado ao N/A - se não tiver a chave name, o retorno é lista vazia, e se ela é vazi então não está disponível o common

Agora se tem chave name, e tem common, retorna o valor