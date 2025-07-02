# ___________________ PIP INSTALL ____________________________________

# pyautogui
# pynput
# requests
# reportlab

# ___________________ IMPORTS ____________________________________

import pyautogui
from pynput import mouse
import time 
import requests
import sqlite3
import sys
import io                       # fluxo de dados
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib.pagesizes import A4



#                     _______________________________________________________________
#                     |                                                             |
#                     |   CARACTERES ESPECIAIS  USADO EM QUASE TODAS FUNÇÕES        |
#                     |_____________________________________________________________|


salvando_stdout_restauro = sys.stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


#                     _______________________________________________________________
#                     |                                                             |
#                     |                   FUNÇÃO CAPTURA TELA                       |
#                     |_____________________________________________________________|

def print_tela ():
    
    """Função sem retorno
    Para por nas funlções e tirar print"""
    salvando_stdout_restauro = sys.stdout
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

    # ___________________ FUNÇÃO PRINT AUTOMATICO

    sys.__stdout__.write("\Print 📸 da tela em ⏰ 2 segundo")
    sys.__stdout__.flush()
    time.sleep(2)
                    
    printando = pyautogui.screenshot()
    intervalo = time.strftime("%d-%b-%Y")
    nome_print = f"Print_tela_{intervalo}.png"
    printando.save(nome_print)
        
    sys.__stdout__.write(f"\n print {nome_print} salvo")
    sys.__stdout__.flush()

    sys.stdout = salvando_stdout_restauro

    

#                     _______________________________________________________________
#                     |                                                             |
#                     |                   FUNÇÃO GERAR DADOS                        |
#                     |_____________________________________________________________|



# _______________________ EXTRAÇÃO DE DADOS____________________________________

def desenhos_base():
    
    '''Função que irá percorer pela api do Studio Ghibli e coletar os 15 primeiros titulos.
        Será armazenado apenas o Título, Título original, Ano e imagem'''

    url = "https://ghibliapi.vercel.app/films"
    
    retorno = requests.get(url)
    dados = retorno.json()

    desenhos_base = []
    
    for desenho in dados[:16]:
        titulo = desenho["title"]
        titulo_oficial = desenho["original_title_romanised"]
        ano = desenho["release_date"]
        imagem = desenho["image"]

        desenhos_base.append((titulo, titulo_oficial, ano, imagem))
    
    
    return desenhos_base

#                     _______________________________________________________________
#                     |                                                             |
#                     |                   FUNÇÃO BANCO DE DADOS                     |
#                     |_____________________________________________________________|



# ___________________ BD ___________________________________
def bd_desenho(desenhos_base):
    try:
        data_file= datetime.now().strftime("%d-%b-%Y")     
        nome_aquiv = f"desenhos_geral_{data_file}.db"
        
        with sqlite3.connect(nome_aquiv) as juncao:
            solicitacao = juncao.cursor()      
        
            solicitacao.execute('''
            CREATE TABLE IF NOT EXISTS desenhos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT,
                    titulo_oficial TEXT,
                    ano INTEGER,
                    imagem TEXT)''')

            for i, desenho in enumerate(16):
                heranca = desenhos_base()
                solicitacao.execute('INSERT INTO desenhos (titulo, titulo_oficial, ano, imagem) VALUES (?, ?, ?, ?)',heranca)  
                print(f"heranca {i+1}: {heranca}")
                
            print("dados criados")
            print(heranca)
        
    except sqlite3.Error as e:
        print(f" Erro no banco de dados do SQLite: {e}")

    except Exception as e:
        print(f"Erro fora do SQL: {e}")
    
    finally:
        sys.stdout = salvando_stdout_restauro
        
    return heranca


#                     _______________________________________________________________
#                     |                                                             |
#                     |                   FUNÇÃO EMAIL                              |
#                     |_____________________________________________________________|

# ___________________ EMAIL REMETENTE 

def emails():
    remetente = "allefr.rpa@gmail.com"
    senha_rem = "xdjz sigs ikrw otyw " 
    destinatario = "celalee45@gmail.com" 

    # ___________________ "CABEÇALHO"

    endereco = MIMEMultipart()
    endereco["From"] = remetente
    endereco["To"] = destinatario
    endereco["Subject"] = "Não é entrega, é confirmação da parte 4 - Envio de Relatório por E-mail Automatizado"

    # ___________________ ADD MENSAGEM 

    mensagem = "\n    A entrega será feita pelo class, mas o envio é para mostrar que funcionaou\nTrabalho Final - RPA - professor Vanderson Gomes Bossi\n\nA api escolhia foi do Studio Ghibli - https://ghibliapi.vercel.app/films - responsáveis por dois filmes que adoro, A Viagem de Chihiro e O Catelo Animado\nO projeto foi feito por partes, funções e, depois importados na main\nEnvio em anexo o pdf do relatório.\n\n\n\n   Atencionamente Alessandra 2401151\nADS - manhã - A\n "
    endereco.attach(MIMEText(mensagem, "plain"))

    print(mensagem)

    # ___________________ ADD ARQUIVO/ VRIFICAR SE FOI ADD

    caminho_arq = "Relatorio_2401151_08-Jun-2025.pdf"

    if os.path.exists(caminho_arq):      
        with open(caminho_arq, "rb") as arquivo:
            parte = MIMEBase("apllication", "octet-stream")
            parte.set_payload(arquivo.read())
            encoders.encode_base64(parte)
            parte.add_header("Content-Disposition", f"attachment; filename = {os.path.basename(caminho_arq)}") 
            endereco.attach(parte)
        print(f"Arquivo {caminho_arq} anexado")
    else:
        print(f"o Arquivo {caminho_arq} não foi encontrado")
        
    # ___________________ ENVIAR EMAIL

    try:
        print("Enviando email ao destinatário")
        servidor = smtplib.SMTP("smtp.gmail.com", 587)     
        servidor.starttls()
        servidor.login(remetente, senha_rem)
        servidor.sendmail(remetente, destinatario, endereco.as_string())
        servidor.quit()
        print(f"Email enviado a o destinatário {destinatario} com sucesso")
        
    except Exception as e:
        print(f"Erro ao enviar email: {e}\n")
    
#                     _______________________________________________________________
#                     |                                                             |
#                     |                      FUNÇÃO PDF                             |
#                     |_____________________________________________________________|


def build_pdf():
    data = datetime.now().strftime("%d-%b-%Y")
    pdf = SimpleDocTemplate(f"RElatorio_2401151_{data}.pdf", pagesize = A4)

    #___________ FORMATAÇÃO TEXTO

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

    pdf.build(paragafos)   

    print(f" {pdf} gerado com sucesso")
    
    return pdf

#                     _______________________________________________________________
#                     |                                                             |
#                     |                      FUNÇÃO MAIN                            |
#                     |_____________________________________________________________|

def main():
    print()
    emails()
    build_pdf()

#                     _______________________________________________________________
#                     |                                                             |
#                     |                      MAIN                                   |
#                     |_____________________________________________________________|

if __name__ == "__main__":
    main()