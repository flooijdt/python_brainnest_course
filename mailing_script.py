import smtplib

port = 1025
smtp_server = "localhost"
sender_email = "paratestes868@gmail.com"
receiver_email = "paratestes868@gmail.com"

message = f"""\
Sender: {sender_email}
Receiver: {receiver_email}
Subject: automating e-mail sending

This is the body of the email."""

with smtplib.SMTP(smtp_server, port) as server:
    server.sendmail(sender_email, receiver_email, message)
