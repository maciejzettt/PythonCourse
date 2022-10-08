import smtplib

host = 'smtp.gmail.com'
port = 465
user = 'm.zaranek.wczt'
pwd = '13WCZT!@'
msg = u""" From: WCZT - dział analiz
Subject: Dostępne pliki do pobrania

Analizy zostały zakończone i dostępne są pliki do pobrania.
"""
msg = smtplib._fix_eols(msg).encode('utf-8')
# try:
gmail = smtplib.SMTP_SSL(host, port)
gmail.ehlo()
gmail.login(user, pwd)
gmail.sendmail(user, 'maciejzetor@gmail.com', msg)
gmail.close()
# except:
#    print("Error sending message", )
