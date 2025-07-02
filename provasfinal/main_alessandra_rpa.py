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

# ___________________ IMPORTS FILES ________________________________

from def_0_char_esp import char_espec
from def_1_build_pdf import build_pdf
from def_2_print_atom import print_tela
from def_3_desen_bas import desenhos_base
from def_4_bd_desen import bd_geral
from def_5_emails import emails


# ___________________ DEF MAIN_________________________________________

def main():
    """função principal que inicia o programa e chama as funções as funções em outras files"""
    
    print("\n\n🪄Bem vindo querido professor!👨‍🏫\nPegue uma 🎸 🍿 pipoca e guaraná 🥤 pois a surpresa será legal!🎹\n ")
       
    char_espec()
    # configuração do stdout

    todosDes = desenhos_base()
    bd_geral (todosDes)

    data = datetime.now().strftime("%d de %b de %Y")
    build_pdf (data)

    emails()

    print("\n\n🎷Eu quero ver o 10 pular, 10 no rpa, sou aluna de rpa 📺\n Espero que tenha gostado\n Programa finalizado\n ")
    
    print_tela()
    
# ___________________ INICIALIZAR ARQ MAIN_________________________________________________

if __name__ == "__main__":
    main()