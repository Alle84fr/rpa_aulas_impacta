import imaplib
import email
from email.header import decode_header

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Informações de login
usuario = "seuemail@gmail.com"
senha = "sua_senha_de_app"

# Conectando ao servidor do Gmail via IMAP
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(usuario, senha)

# Seleciona a caixa de entrada
mail.select("inbox")

# Busca e-mails não lidos
status, mensagens = mail.search(None, '(UNSEEN)')  # UNSEEN = não lido

# Divide os IDs dos e-mails
email_ids = mensagens[0].split()

print(f"🔍 {len(email_ids)} e-mails não lidos encontrados.\n")

# Lê os primeiros 5 e-mails não lidos (ou todos se forem menos)
for i in email_ids[:5]:
    status, dados = mail.fetch(i, "(RFC822)")
    raw_email = dados[0][1]
    mensagem = email.message_from_bytes(raw_email)

    # Pega o assunto
    assunto, encoding = decode_header(mensagem["Subject"])[0]
    if isinstance(assunto, bytes):
        assunto = assunto.decode(encoding or "utf-8")

    # Pega o remetente
    remetente = mensagem["From"]

    print(f"📨 De: {remetente}")
    print(f"📌 Assunto: {assunto}")
    print("—" * 40)

mail.logout()