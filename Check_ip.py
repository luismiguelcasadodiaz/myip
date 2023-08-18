#!/usr/bin python
# -*- coding: utf-8 -*-

import os
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from urllib.request import urlopen
def query_ip():
    """ Read value returned by ident.me
    """

    url="http://ident.me"
    ip = urlopen(url).read().decode('utf-8')
    return ip

def verify_ip(ip):
    with open(os.path.join(sys.path[0], "actual_ip.txt"), "r") as f:
        actual_ip=f.read()
    if ip == actual_ip:
        print("sin cambios")
    else:
        print("con cambios")
        with open(os.path.join(sys.path[0], "actual_ip.txt"), "w") as f:
            f.write(ip)

def send_mail_with_new_ip(ip):
    mail_content = '''Hello,
    This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
    Thank You'''
    #The mail addresses and password
    sender_address = 'chiverato@gmail.com'
    sender_pass = 'lu15ca5ad0'
    receiver_address = 'luimiguelcasadodiaz@gmail.com'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'new ip' + ip   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    #session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session = smtplib.SMTP('smtp.gmail.com', 465) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

ip=query_ip()
verify_ip(ip)
send_mail_with_new_ip(ip)