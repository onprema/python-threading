# Source: https://learning.oreilly.com/library/view/fluent-python-2nd/9781492056348/ch19.html#idm46582392974816
import itertools
import time
from threading import Event, Thread


def spin(msg: str, done: Event) -> None:
    """
    This function will run in a separate thread. The done argument is an instance of threading.Event, a simple object to synchronize threads.
    """
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(.1):
            break # Exit the infinite loop.
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

def slow() -> int:
    """
    slow() will be called by the main thread. Imagine this is a slow API call over the network. Calling sleep blocks the main thread, but the GIL is released so the spinner thread can proceed.
    """
    time.sleep(3)
    return 42

def supervisor() -> int:
    done = Event()
    spinner = Thread(target=spin, args=('Thinking...', done))
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result

def main() -> None:
    result = supervisor()
    print(f'Answer: {result}')

if __name__ == '__main__':
    main()