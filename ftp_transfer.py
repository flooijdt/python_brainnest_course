#!/bin/python3
# Intormation to access the public FTP server used
# are available at https://dlptest.com/ftp-test/.
# be sure to visit the site since the password changes
# from time to time.
import ftplib

# FTP server information:
hostname = "ftp.dlptest.com"
username = "dlpuser"
password = "rNrKYTX9g7z3RgJRmxWuGHbeu"

# Create server
ftp_server = ftplib.FTP(hostname, username, password)

# force UTF-8 encoding
ftp_server.encoding = "utf-8"

# Enter filename to store with extension
filename = "attachment.txt"

# Read file in binary mode
with open(filename, "rb") as file:
    # Upload the file "STOR filename"
    ftp_server.storbinary(f"STOR {filename}", file)

# Get list of files
ftp_server.dir()

# Enter filename to retrieve
filename = "attachment.txt"

# Write file in binary mode
with open(filename, "wb") as file:
    # Download the file "RETR filename"
    ftp_server.retrbinary(f"RETR {filename}", file.write)

# Display the content of downloaded file
file = open(filename, "r")
print('File Content:', file.read())

# Close the Connection
ftp_server.quit()
