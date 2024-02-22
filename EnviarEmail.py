import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def EnviarEmail(remetente, assunto, corpo):
    try:
        port = 587  # For starttls
        smtp_server = "smtp.seusmtp.com"
        sender_email = "Seu email aqui"
        # receiver_email = "bruno.martins@idtech.org.br"
        receiver_email = remetente
        password = 'senha'


        #Para criar a mensagem, utilize este formato
        msg = MIMEMultipart("alternative")
        msg["Subject"] = assunto
        msg.attach( MIMEText(corpo, "plain", "utf-8" ) )
        msg = msg.as_string().encode('ascii')

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg)
            return True
    except:
        return False
# print(EnviarEmail('teste@teste.com', 'titulo', 'teste um dois três'))