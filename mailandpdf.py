import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os



gmail_user = "ratb4u@gmail.com"
gmail_pwd = "9433154747"

msg = 'This is an automated mail from the user!!! yaay cheers'

toaddrs ='banerjee.soumyajyoti4@gmail.com'
server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(gmail_user,gmail_pwd)
server.sendmail(gmail_user, toaddrs, msg)

