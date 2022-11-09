import getpass
import ssl
import smtplib
from email.message import EmailMessage

email_send = input("Enter email please: ")
password = getpass.getpass(
    "FOR GMAIL ONLY PLEASE ENABLE TWO STEP VERIFIACTION AND ENTER IN APP PASSWORD ONLY: ")
email_recieve = input("Enter To Address Please: ")

subject = input('Enter subject: ')
body = input("Please enter body: ")

em = EmailMessage()
em['From'] = email_send
em['To'] = email_recieve
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_send, password)
    smtp.sendmail(email_send, email_recieve, em.as_string())
