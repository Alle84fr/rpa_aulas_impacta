import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Informações do remetente e destinatário
remetente = 'seuemail@gmail.com'
senha = 'sua_senha_de_app'  # Recomendado: use senha de app, não a senha normal
destinatario = 'xxxxxxxxxx@hotmail.com'

# Criação da mensagem
mensagem = MIMEMultipart()
mensagem['From'] = remetente
mensagem['To'] = destinatario
mensagem['Subject'] = 'E-mail com anexo enviado por Python'

# Corpo do e-mail
corpo = 'Olá! Este e-mail contém um anexo enviado automaticamente com Python.'
mensagem.attach(MIMEText(corpo, 'plain'))

# Caminho do arquivo a ser anexado
caminho_anexo = 'AC2-TEC-20251.pdf'  # Substitua pelo nome real do arquivo

# Verifica se o arquivo existe
if os.path.exists(caminho_anexo):
    with open(caminho_anexo, 'rb') as arquivo:
        parte = MIMEBase('application', 'octet-stream')
        parte.set_payload(arquivo.read())
        encoders.encode_base64(parte)
        parte.add_header('Content-Disposition', f'attachment; filename={os.path.basename(caminho_anexo)}')
        mensagem.attach(parte)
else:
    print("⚠️ Arquivo não encontrado. Enviando e-mail sem anexo.")

try:
    print("⏳ Enviando e-mail...")
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(remetente, senha)
    servidor.sendmail(remetente, destinatario, mensagem.as_string())
    servidor.quit()
    print("✅ E-mail enviado com sucesso!")

except Exception as e:
    print(f"❌ Erro ao enviar e-mail: {e}")