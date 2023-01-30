import smtplib, ssl, os
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "paratestes868@gmail.com"
receiver_email = "paratestes868@gmail.com"
password = input("input the password: ")


message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
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

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

for file in os.listdir('.'):
    if file.startswith('attachment'):
        print(file)
        part = MIMEBase("application", "octet-stream")
        part.set_payload(file.read())
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
