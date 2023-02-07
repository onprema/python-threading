# Example of a multi-threaded application using start() and join() with a timeout
from training import WEBSITES, visit_website
import threading


if __name__ == '__main__':
    print('Main thread starting')
    for website in WEBSITES:
        # Create, start and join a daemon thread that times out
        t = threading.Thread(target=visit_website, args=[website], daemon=True)
        t.start()
        t.join(timeout=1)
    print('Main thread ending')