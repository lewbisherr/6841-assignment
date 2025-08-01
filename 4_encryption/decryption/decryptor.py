# Iteration 4-2, this file decrypts what is written in the encrypted file in 4-1 and
# prints out the result to terminal

# Usage: python decryptor.py [filename]

# The following code is taken from the PyCryptoDome docs: https://www.pycryptodome.org/src/examples#generate-an-rsa-key
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
import sys
import os

private_key = RSA.import_key(open("private.pem").read(), passphrase='z5432894')

# Opens given binary file
with open(sys.argv[1], "rb") as f:
    enc_session_key = f.read(private_key.size_in_bytes())
    nonce = f.read(16)
    tag = f.read(16)
    ciphertext = f.read()

# Decrypt the session key with the private RSA key
cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(enc_session_key)

# Decrypt the data with the AES session key
cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
data = cipher_aes.decrypt_and_verify(ciphertext, tag)

with open('decrypted_text.txt', "w") as f:
    f.write(str(data))