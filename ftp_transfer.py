#!/bin/python3
# Intormation to access the public FTP server used
# are available at https://dlptest.com/ftp-test/.
# be sure to visit the site since the password changes
# from time to time.
import ftplib
import os
# import shutil
# import ntpath
import time
import logging
import schedule

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

time_to_run = "14:38"

# starts logging the program status.
logging.basicConfig(filename="log_ftp.txt", level=logging.DEBUG,
                    format="%(asctime)s %(message)s")


def ftp_transfer(
    hostname=hostname,
    username=username,
    password=password,
    filenames=filenames
):
    # Read file in binary mode
    for filename in filenames:
        with open(filename, "rb") as file:
            # Upload the file "STOR filename"
            ftp_server.storbinary(f"STOR {filename}", file)

    logging.info("Files updated to ftp server successfully.")
    # Get list of files
    ftp_server.dir()

    # Creates ftp_files folder to store files there.
    os.makedirs("./ftp_files", exist_ok=True)
    script_dir = os.path.dirname(__file__)

    # Write file in binary mode
    for filename in filenames:
        rel_path = f"ftp_files/{filename}"
        abs_file_path = os.path.join(script_dir, rel_path)
        # dest_network = ntpath.join("dav://linux.local")
        with open(abs_file_path, "wb") as file:
            # Download the file "RETR filename"
            ftp_server.retrbinary(f"RETR {filename}", file.write)
        # shutil.copyfile(abs_file_path, dest_network)

    logging.info("files copied to ftp_files successfully.")
    # Close the Connection
    ftp_server.quit()


schedule.every().day.at(time_to_run).do(ftp_transfer)
logging.info("Schedulling happened successfully.")
# Creates a infinite loop that will refresh every 60 seconds:
while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(60)
