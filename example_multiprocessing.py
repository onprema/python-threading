from multiprocessing import Pool
import time

COUNT = 50000000
def countdown(n):
    while n>0:
        n -= 1

if __name__ == '__main__':
    processes = 2
    pool = Pool(processes=processes)
    start = time.time()
    r1 = pool.apply_async(countdown, [COUNT//processes])
    r2 = pool.apply_async(countdown, [COUNT//processes])
    pool.close()
    pool.join()
    end = time.time()
    print('Time taken in seconds (multiprocessing) -', end - start)

    # Single process
    start = time.time()
    countdown(COUNT)
    end = time.time()
    print('Time taken in seconds (default processing) -', end - start)
