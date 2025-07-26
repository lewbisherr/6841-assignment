# Iteration 1: Logs all keystrokes to terminal

import keyboard

# Prints all keystrokes to terminal
def print_key(e):
    print(e.name)
    
keyboard.on_press()
keyboard.wait()