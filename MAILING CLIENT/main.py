import smtplib
from email import encoders, message
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP("smtp-mail.outlook.com.",25)

server.ehlo()
server.starttls()
server.ehlo()

with open("password.txt","r") as f:
    password = f.read()

server.login("Your Mail","Your Password")
# or
# server.login("Your Mail",password)

msg = MIMEMultipart()
msg["From"] = "Zeref"
msg["To"] = "Recevers Mail"
msg["Subject"] = "Just Testing"

with open("message.txt","r") as f:
    message = f.read()

msg.attach(MIMEText(message,"plain"))

filename = "hacking.jpg"

attachment = open(filename,'rb')

p = MIMEBase("application","octet-stream")
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header("Content-Diposition",f'attachment; filename={filename}')
msg.attach(p)

text1 = msg.as_string()
server.sendmail("Your Mail","Recevers Mail",text1)

# note
# your mail the mail which you want to login to SMTP server cannot be gmail
# It will give you a error
# Google gmail doesn't allow third party software or scripts to login with only password and email
# so you can use either outlook or any other domain