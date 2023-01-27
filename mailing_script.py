#!/usr/bin/python

import smtplib

sender = 'wbxwrrfggwuligcwti@tmmwj.net'
receivers = ['wbxwrrfggwuligcwti@tmmwj.net']

message = """From: From Person <wbxwrrfggwuligcwti@tmmwj.net>
To: To Person <wbxwrrfggwuligcwti@tmmwj.net>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print("Successfully sent email")
except:
   print("Error: unable to send email")