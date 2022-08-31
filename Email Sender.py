#Email Sender

from email.message import EmailMessage
#Library
import ssl
import smtplib
email_sender = '2min0min19@gmail.com'
email_password = 'qgosqhewdxuoyate'
email_recevier = 'fiyor89797@lurenwu.com'


subject = "Friends"
body = "Love you my friend"

emailmessage = EmailMessage()
emailmessage['From'] = email_sender
emailmessage['To'] = email_recevier
emailmessage['Subject'] = subject

emailmessage.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465, context = context ) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_recevier, emailmessage.as_string())

