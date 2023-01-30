#!/bin/python3
# This is a script, remember to make the file executable.
# in Unix this is done by the chmod comand:
# chmod 744 "name of this file"
import smtplib
import ssl
import os
import schedule
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# The programs default inputs. the port is the default for gmail 465,
# and the server is also gmail's default smtp server:
port = 465
smtp_server = "smtp.gmail.com"
sender_email = "paratestes868@gmail.com"
# A list with every receiver's email:
receiver_email_list = [
    "paratestes868@gmail.com",
    # 10 minute mail created for test:
    "sijlxsufsbmfluchxv@tmmcv.net"
]
# by default the attachments names are attachment.txt and
# attachment2.csv. As the name declared here will acctually be
# matched in a globbing fashion with the names of files in
# the programs folder, it is "attachment", wich will match both archives.
attachment_file = "attachment"
# the password is given via input as a security measure.
password = input("Input the account's password: ")
# time to daily run the program
time_to_run = "17:33"


def send_email(
    port,
    smtp_server,
    sender_email,
    receiver_email,
    attachment_file
):

    # creates a multipart message object for the email message:
    message = MIMEMultipart("alternative")
    message["Subject"] = "This is the Subject of the e-mail."
    message["From"] = sender_email
    message["To"] = receiver_email

    # plain-text and HTML version of message:
    text = """\
    Hi Arsalan,
    How are you?
    My Signature."""

    html = """\
    <html>
      <body>
        <p>Hi, Arsalan<br>
           How are you?<br>
           My Signature.
        </p>
      </body>
    </html>
    """

    # turns these into plain/html MIMEText objects:
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # opens the attachments and encode them in order to send them
    # with the message:
    for file in os.listdir('.'):
        if file.startswith(attachment_file):
            try:
                with open(file, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    # Add header as key/value pair to file part
                    part.add_header(
                        "Content-Disposition",
                        f"file; filename= {file}",
                    )

                    # Add file to message and convert message to string
                    message.attach(part)
                    text = message.as_string()
            except:
                ("Error: Could not attach or encode files.")

    context = ssl.create_default_context()
    # Creates server:
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
        except smtplib.SMTPConnectError:
            print("SMTPConnectError: Could connect to sender email\
                 with given password.")
        try:
            server.sendmail(sender_email, receiver_email, message.as_string())
        except smtplib.SMTPAuthenticationError:
            print("SMTPAuthenticationError: \
                could not authenticate the sender.")

    print(f"Email sended successfully to {receiver_email}")


# Function to send email to everyone in receiver_email_list:
def send_email_to_everyone():
    for receiver_email in receiver_email_list:
        send_email(
            port,
            smtp_server,
            sender_email,
            receiver_email,
            attachment_file
        )


# Calls send_email_to_everyone() function daily at
# the time given to the time_to_run variable:
schedule.every().day.at(time_to_run).do(send_email_to_everyone)

# Creates a infinite loop that will refresh every 60 seconds:
while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(60)
