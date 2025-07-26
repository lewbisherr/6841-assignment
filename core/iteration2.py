# Iteration 2: Logs all keystrokes to a file

import keyboard

# Opens a file called output.txt, listens to logs and writes to the file
with open("output.txt", "w") as log_file:
    print('Starting record! Press ESC to exit!')
    events = keyboard.record(until='escape')
    
    for event in events:
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            log_file.write(f"{key}")