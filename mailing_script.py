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

# Creates smtp server.
with smtplib.SMTP(smtp_server, port) as server:
    server.sendmail(sender_email, receiver_email, message)
