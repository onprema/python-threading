# Example of using daemon threads to terminate threads when the main thread terminates
from training import WEBSITES, visit_website
import threading
import sys
import time


if __name__ == '__main__':
    # Create a forced timeout option
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} TIMEOUT')
        sys.exit()

    print('Main thread starting')

    # The program will end after `timeout` seconds
    timeout = int(sys.argv[1])

    for website in WEBSITES:
        # Create and start some daemon threads
        t = threading.Thread(target=visit_website, args=[website], daemon=True)
        t.start()
    
    # Force the program to end after timeout
    time.sleep(timeout)

    print('Main thread ending')