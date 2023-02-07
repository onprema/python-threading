# Example of a multi-threaded application using ThreadPoolExecutor
from training import WEBSITES, visit_website
from concurrent.futures import ThreadPoolExecutor


if __name__ == '__main__':
    print('Main thread starting')
    # Use the ThreadPoolExecutor context manager to manage threads
    with ThreadPoolExecutor(max_workers=3) as executor:
        for website in WEBSITES:
            # Submit a function and args to the pool of threads
            executor.submit(visit_website, website)
    print('Main thread ending')