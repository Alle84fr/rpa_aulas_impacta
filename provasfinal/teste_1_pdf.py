#                     _______________________________________________________________
#                     |                                                             |
#                     |                      FUNÇÃO PDF 1/                         |
#                     |_____________________________________________________________|


#pip install reportlab

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from datetime import datetime

#devido pesquisas, resolvi usar este ao invéz do canvas, mais fácil diagramar parágrafos
 

data = datetime.now().strftime("%d-%b-%Y")
pdf = SimpleDocTemplate(f"RElatorio_2401151_{data}.pdf", pagesize = A4)

    #___________ FORMATAÇÃO TEXTO

    # ParagraphStyle() -> função de cria nova formatação de parágrafos
    # name = "center" ->  seria quase que o id da formatação, cada um tem a sua
    # parent = styles ["Normal"] -> estilo normal
    # extilos existentes ['Normal', 'BodyText', 'Italic', 'Heading1', 'Heading2', 'Heading3',  'Heading4', 'Heading5', 'Heading6', 'Bullet', 'Definition', 'Code']
    # alignment -> 0 = left/esquerda, 1 = centro/Center, 2 = direita/Right e 4 = juntificado = Justify
    #spaceAfter = esspaço depois do parágrasfo,, pular linhas -> 

formatacao = getSampleStyleSheet()

formatacao_esquerda = ParagraphStyle(name="Esquerda", parent=formatacao["Normal"], alignment=0, fontSize=12)
formatacao_direita = ParagraphStyle(name="Direita", parent=formatacao["Normal"], alignment=2, fontSize=12)
formatacao_centro = ParagraphStyle(name="Centro", parent=formatacao["Normal"], alignment=1, fontSize=12)
formatacao_titulo1 = ParagraphStyle(name="Titulo1", parent=formatacao["Heading1"], alignment=1)
formatacao_titulo2 = ParagraphStyle(name="Titulo2", parent=formatacao["Heading2"], alignment=1, spaceAfter= 180)
formatacao_titulo3 = ParagraphStyle(name="Titulo3", parent=formatacao["Heading3"], alignment=1, spaceAfter= 40)
formatacao_paragafo1 = ParagraphStyle(name="Paragrafi1", parent=formatacao["Heading2"], alignment=1, spaceAfter= 10)
formatacao_centrodata = ParagraphStyle(name="Centro", parent=formatacao["Normal"], alignment=1, fontSize=8, spaceBefore=410)



    #___________ TEXTO

paragafos = [
    Paragraph("Faculdade Impacta", formatacao_titulo1),
    Paragraph("Automação Robótica de Processo", formatacao_titulo2),
    Paragraph(f"Alessandra ", formatacao_esquerda),
    Paragraph(f" ", formatacao_titulo2),
    Paragraph(f"São Paulo {data}", formatacao_centrodata),
    Paragraph(f"📼 Requisição de dados a uma API pública 📽️ ", formatacao_titulo3),
    Paragraph(f"Para este projeto de RPA, escolhi a API dos Studios Ghibli - https://ghibliapi.vercel.app/films-", formatacao_centro),
    Paragraph(f" ", formatacao_paragafo1),
    Paragraph(f"Após analisar as apis listadas no pdf de regras do trabalho, escolhi pegar um aplicativo que dispertasse meu interesse e ideias de divisões.\nCheguei neste api por meio da DeepSeek, queria um que fossem desenhos que  gosto com imagens.\nO trabalho será dividido entre desenhos já assistidos e desenhos que estão na lista para assistir.\n Ao todo serão listados 15 desenhos no total, o que tiverem fora de alguma lista é porque não  irei assistir ou não prendeu minha atenção.\nInformações que serão mostradas:\nTitulo, Título original, ano, url imagem.", formatacao_esquerda),]

pdf.build(paragafos)   #cria o pdf

print(f" {pdf} gerado com sucesso")
   