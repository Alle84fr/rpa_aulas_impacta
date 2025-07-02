import imaplib
import email
from email.header import decode_header

# Configurações de acesso
usuario = "seuemail@gmail.com"
senha = "sua_senha_de_app"

# Conexão segura com o servidor IMAP do Gmail
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(usuario, senha)
mail.select("inbox")

# Busca os e-mails não lidos
status, mensagens = mail.search(None, '(UNSEEN)')
email_ids = mensagens[0].split()

print(f"🔍 Foram encontrados {len(email_ids)} e-mails não lidos.\n")

# Loop nos primeiros 10 e-mails não lidos
for i in email_ids[:10]:
    status, dados = mail.fetch(i, "(RFC822)")
    raw_email = dados[0][1]
    mensagem = email.message_from_bytes(raw_email)

    # Decodifica o assunto
    assunto, encoding = decode_header(mensagem["Subject"])[0]
    if isinstance(assunto, bytes):
        assunto = assunto.decode(encoding or "utf-8", errors="ignore")

    # Remetente
    remetente = mensagem["From"]

    # Conteúdo
    corpo = ""
    if mensagem.is_multipart():
        for parte in mensagem.walk():
            content_type = parte.get_content_type()
            content_disposition = str(parte.get("Content-Disposition"))

            if content_type == "text/plain" and "attachment" not in content_disposition:
                try:
                    corpo = parte.get_payload(decode=True).decode()
                except:
                    corpo = "[Erro ao decodificar o corpo do e-mail]"
                break
    else:
        corpo = mensagem.get_payload(decode=True).decode()

    # Exibição
    print("📨 De:", remetente)
    print("📌 Assunto:", assunto)
    print("📃 Corpo:\n", corpo[:300], "..." if len(corpo) > 300 else "")  # Mostra os primeiros 300 caracteres
    print("—" * 60)

# Encerra a sessão
mail.logout()