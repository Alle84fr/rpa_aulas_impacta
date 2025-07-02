import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import sys
import io

# ___________________ CARACTERES ESPECIAIS ____________________________________

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# ___________________ EMAIL REMETENTE __________________________________________

# https://myaccount.google.com/security
# Verificação de 2 etapas ativa, senhas de app, criar senha, outro, nome, senha
 
remetente = "allefr.rpa@gmail.com"
senha_rem = "xdjz sigs ikrw otyw " #"123456RPA"
destinatario = "celalee45@gmail.com" #por para envio e-mail do professor - 

# ___________________ "CABEÇALHO"

# objeto MIME = Multipurpose Internet Mail Extendion - classe do módulo email que permite que o email padrão possa receber HTML, .md, texto ( parte Text) PDF, imagens, (parte Image) caracteres especiais, e-mails "retalhados" (organizados por partes, não em um bloco só, que seria a parte MULTIPART) e áudios (pate Audio)
# MIME pode enviar email, pdf, etc

endereco = MIMEMultipart()
endereco["From"] = remetente
endereco["To"] = destinatario
endereco["Subject"] = "Não é entrega, é confirmação da parte 4 - Envio de Relatório por E-mail Automatizado"

# ___________________ ADD MENSAGEM 

# attach = anexar, adicionar a parte em questão ao objeto MIMe ("o email")
# plan = simples, plano, sem formatação, entendido por todos que receber. Se fosse html, deveria ser usado as tags<h1>titulo<h1/>

mensagem = "\n    A entrega será feita pelo class, mas o envio é para mostrar que funcionaou\nTrabalho Final - RPA - professor Vanderson Gomes Bossi\n\nA api escolhia foi do Studio Ghibli - https://ghibliapi.vercel.app/films - responsáveis por dois filmes que adoro, A Viagem de Chihiro e O Catelo Animado\nO projeto foi feito por partes, funções e, depois importados na main\nEnvio em anexo o pdf do relatório.\n\n\n\n   Atencionamente Alessandra 2401151\nADS - manhã - A\n "
endereco.attach(MIMEText(mensagem, "plain"))

print(mensagem)

# ___________________ ADD ARQUIVO/ VRIFICAR SE FOI ADD

# tradução do caminho de verificação - if os.path.....endereco.attach(parte)
# se no sistema operacional o caminho existir
# with = gerencia o contexto, abrindo (open(), manipula o aquivo (interativi) e fecha o arquivo automaticamente, mesmo com erro)
# rb = modo binário 
# with.open= algo assim: com o arquivo aberto em binário....
# apllication = argumento gera, pdf, zip, 
# octet-stream = para arquivos binário
# os dois junto ddiz que parte é um objeto, arquivo binário genérico
# arquivo.read = lê o conteúdo em bytes
# set_playload() = define o conteúdo como com bytes lidos
# base64 = codifica dados binários em textos, evitando corrupção (transforma em texto puro)
# add_header = como o email será interpretado
# content_disposition = conteúdo é anexo, não conteúdo

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

# smtp = Simple Mail Transfer Protocol, protocolo padrão de envio de email, define como servidores se comunicam
# smtplib = biblioteca do .py que fornece as interfaces do protocólo smmtp
# tls = para criptografar
# sendmail = envia de, para e 
# quit = finaliza

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
    
    
# Arquivo RElatorio_2401151_08-Jun-2025.pdf anexado
# Enviando email ao destinatário
# Erro ao enviar email: [Errno 11001] getaddrinfo failed
# Este erro porque .py não consegue ou não foi digitado o smtp corretamente, ou sem internet, DNS (8.8.8.8 ou 8.8.4.4), porta incorreta (usei a tls 587, a outra é ssl 465), ou acesso a app menos seguro
# erro estava na linha 82 - servidor.smtplib .... - > mstp.gmil inveti o sm e não coloquei a no gmail