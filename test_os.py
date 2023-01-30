import os

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


