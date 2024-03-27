# Example of a multi-threaded application using ThreadPoolExecutor
from training import WEBSITES, visit_website
from concurrent.futures import ThreadPoolExecutor

if __name__ == '__main__':
    print('Main thread starting')

    # Collection of future objects
    futures = []

    with ThreadPoolExecutor(max_workers=20) as executor:
        for website in WEBSITES:
            # Submit a function and args to the pool of threads
            futures.append(executor.submit(visit_website, website))

    # Iterate over the results
    for future in futures:
        print(future.result())

    print('Main thread ending')