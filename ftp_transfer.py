#!/bin/python3
# Intormation to access the public FTP server used
# are available at https://dlptest.com/ftp-test/.
# be sure to visit the site since the password changes
# from time to time.
import ftplib
import os

# FTP server information:
hostname = "ftp.dlptest.com"
username = "dlpuser"
password = "rNrKYTX9g7z3RgJRmxWuGHbeu"

# Create server
ftp_server = ftplib.FTP(hostname, username, password)

# force UTF-8 encoding
ftp_server.encoding = "utf-8"

# Enter filename to store with extension
filenames = ["attachment.txt", "attachment2.csv"]

# Read file in binary mode
for filename in filenames:
    with open(filename, "rb") as file:
        # Upload the file "STOR filename"
        ftp_server.storbinary(f"STOR {filename}", file)

# Get list of files
ftp_server.dir()

# Creates ftp_files folder to store files there.
os.mkdir("./ftp_files")
script_dir = os.path.dirname(__file__)

# Write file in binary mode
for filename in filenames:
    rel_path = f"ftp_files/{filename}"
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path, "wb") as file:
        # Download the file "RETR filename"
        ftp_server.retrbinary(f"RETR {filename}", file.write)

# Close the Connection
ftp_server.quit()
