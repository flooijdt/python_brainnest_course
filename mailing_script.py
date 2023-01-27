import smtplib

port = 1025
smtp_server = "localhost"
sender_email = "paratestes868@gmail.com"
receiver_email = "paratestes868@gmail.com"
password = input("Type your password and press enter: ")

message = """\
Subject: Hi there

This message is sent from Python."""

with smtplib.SMTP(smtp_server, port) as server:
    server.sendmail(sender_email, receiver_email, message)
