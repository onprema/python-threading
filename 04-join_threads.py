# Example of a multi-threaded application using start() and join()
from training import WEBSITES, visit_website
import threading


if __name__ == '__main__':
    print('Main thread starting')
    for website in WEBSITES:
        # Create, start, and join a thread
        t = threading.Thread(target=visit_website, args=[website])
        t.start()
        t.join()
    print('Main thread ending')