# Example of a multi-threaded application using daemon threads
from training import WEBSITES, log_website
import threading
import time


if __name__ == '__main__':
    print('Main thread starting')
    for website in WEBSITES:
        # Create a Thread object with target and args
        t = threading.Thread(target=log_website, args=[website], daemon=False)
        # Start the thread
        t.start()
    print('Main thread ending')