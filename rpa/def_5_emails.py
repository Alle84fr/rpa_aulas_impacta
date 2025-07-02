import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os


# ___________________ EMAIL REMETENTE __________________________________________

# https://myaccount.google.com/security
# Verificação de 2 etapas ativa, senhas de app, criar senha, outro, nome, senha

def emails(): 
    
    """Função de criação de email com remetente, destinatário, assunto, corpo e anexo"""
    
    remetente = "allefr.rpa@gmail.com"
    senha_rem = "senha " 
    destinatario = "celalee45@gmail.com" 

    # ___________________ "CABEÇALHO"

    endereco = MIMEMultipart()
    endereco["From"] = remetente
    endereco["To"] = destinatario
    endereco["Subject"] = "Relatório por E-mail Automatizado"

    # ___________________ ADD MENSAGEM 

   
    mensagem = "\n    A entrega será feita pelo class, mas o envio é para mostrar que funcionaou\nTrabalho Final - RPA - professor Vanderson Gomes Bossi\n\nA api escolhia foi do Studio Ghibli - https://ghibliapi.vercel.app/films - responsáveis por dois filmes que adoro, A Viagem de Chihiro e O Catelo Animado\nO projeto foi feito por partes, funções e, depois importados na main\nEnvio em anexo o pdf do relatório.\n\n\n\n   Atencionamente Alessandra 24\nADS - manhã - A\n "
    endereco.attach(MIMEText(mensagem, "plain"))

    print(mensagem)

    # ___________________ ADD ARQUIVO/ VRIFICAR SE FOI ADD

    caminho_arq = "relatorio_2401151_09-Jun-2025.pdf"

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
        
