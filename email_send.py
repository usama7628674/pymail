#!/usr/bin/python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import getpass
import time
import sys
import os
import platform

class colors:
        OKGREEN = '\033[92m'
        BLUE = '\033[94m'


if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')



msg = MIMEMultipart()

print(colors.BLUE + 'To send an email you must have less secure apps enabled in your account \nhttps://myaccount.google.com/lesssecureapps')


msg['From'] = input (colors.OKGREEN + '\nYour Email: ')

passwd = getpass.getpass(colors.OKGREEN + 'Password: ')

print(colors.BLUE + '\nTo send an email to multiple receipents use comma(,) followed by mail address')

msg['To'] = input (colors.OKGREEN + '\nTo: ')

to = msg['TO'].split(",")

msg['subject'] = input (colors.OKGREEN + 'Subject: ')


body = input (colors.OKGREEN + 'Message: ')


msg.attach(MIMEText(body, 'plain'))

def check_attach():
    check = input (colors.OKGREEN + "Do you want to attach files [y/n] ")
    if check == 'y':
        os.system('python -m zipfile -c attachment.zip attachments')
        attachment = open('attachment.zip', "rb")
        p = MIMEBase('application', 'zip')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= attachment.zip")
        msg.attach(p)
        attachment.close()

    elif check == 'n':
        print('This email will be sent without any attachment')
    else:
	       print('Wrong selection')
	       check_attach()
check_attach()

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login(msg['From'], passwd)

text = msg.as_string()

nomes = int(input(colors.OKGREEN + 'No. of email(s) to send: '))
no = 0

while no != nomes:
	s.sendmail(msg['From'], to, text)
	print(colors.BLUE + 'successfully sent ' + str(no+1) + ' emails')
	no += 1
	time.sleep(.8)
s.close()

if platform.system() == 'Windows':
    if os.path.exists('attachment.zip'):
        os.remove('attachment.zip')
    else:
        pass
else:
    os.system('rm attachment.zip 2> /dev/null')
