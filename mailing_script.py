import smtplib, ssl, os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# The programs default inputs. the port is the default for gmail 465,
# and the server is also gmail's default smtp server:
port = 465
smtp_server = "smtp.gmail.com"
sender_email = "paratestes868@gmail.com"
receiver_email = "paratestes868@gmail.com"
# by default the attachments names are attachment.txt and
# attachment2.csv
attachment_file = "attachment"

def send_email(port, smtp_server, sender_email, receiver_email, attachment_file):
    # the password is given via input as a security measure.
    password = input("input the password: ")

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

    context = ssl.create_default_context()
    # Creates smtp server.
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Email sended successfully.")


send_email(port, smtp_server, sender_email, receiver_email, attachment_file)
