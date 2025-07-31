import subprocess
import pathlib
import sys

if getattr(sys, 'frozen', False):
    base = pathlib.Path(sys._MEIPASS)            # temp dir when frozen
else:
    base = pathlib.Path(__file__).parent / "data"

elevate_path = base / "elevate.ps1"

# print(base)
# time.sleep(200)

subprocess.Popen(["powershell", "-File", str(elevate_path), f"{base}", "folder_create.exe"], subprocess.DETACHED_PROCESS | subprocess.CREATE_NO_WINDOW)