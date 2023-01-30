import smtplib, ssl

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "paratestes868@gmail.com"
receiver_email = "paratestes868@gmail.com"
password = input("input the password: ")


message = f"""\
Sender: {sender_email}
Receiver: {receiver_email}
Subject: automating e-mail sending

This is the body of the email."""

context = ssl.ccreate_default_context()
# Creates smtp server.
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
