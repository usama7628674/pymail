#!/usr/bin/python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import getpass
from os import system
import time
import sys
  
class colors:
	OKGREEN = '\033[92m'
        BLUE = '\033[94m'


system('clear')
  

msg = MIMEMultipart()

print colors.BLUE + 'To send an email you must have less secure apps enabled in your account \nhttps://myaccount.google.com/lesssecureapps'
 
 
msg['From'] = raw_input (colors.OKGREEN + '\nYour Email: ')  

user = msg['From']

passwd = getpass.getpass(colors.OKGREEN + 'Password: ') 

print colors.BLUE + '\nTo send an email to multiple receipents use comma(,) followed by mail address'

msg['To'] = raw_input (colors.OKGREEN + '\nTo: ')

to = msg['TO'].split(",")
 
subject = raw_input (colors.OKGREEN + 'Subject: ')
 

body = raw_input (colors.OKGREEN + 'Message: ') 

message = 'From: ' + user + '\nSubject: ' + subject + '\n' + body

msg.attach(MIMEText(message, 'plain'))

check = raw_input (colors.OKGREEN + "Do you want to attach files [y/n] ")
if check == 'y':	
	
		
		system('python -m zipfile -c attachment attachments/*')                 
		attachment = open('attachment', "rb")
                p = MIMEBase('application', 'zip')
                p.set_payload((attachment).read())
                encoders.encode_base64(p)
                p.add_header('Content-Disposition', "attachment; filename= attachment")
 		msg.attach(p)

elif check == 'n':		
		             
		print 'This email will be sent without any attachment'
else:
	print 'Wrong selection'
	sys.exit()
        	
s = smtplib.SMTP('smtp.gmail.com', 587)
 
s.starttls()
 
s.login(user, passwd)
 
text = msg.as_string()

nomes = input(colors.OKGREEN + 'No. of email(s) to send: ')
no = 0 	
while no != nomes:
	s.sendmail(user, to, text)
	print colors.BLUE + 'successfully sent ' + str(no+1) + ' emails'
	no += 1
	time.sleep(.8)
system('rm attachment 2> /dev/null')
s.quit()			
