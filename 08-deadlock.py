# Example of a deadlock situation
import threading


if __name__ == '__main__':

    # Create a lock
    lock = threading.Lock()
    print(lock)

    # Acquire a lock 
    lock.acquire()
    print(lock)

    # Acquire a lock again -- deadlock!
    lock.acquire()
    print(lock)

    # Release the lock
    lock.release()
    print(lock)

    """

    lock = threading.Lock()

    SHARED_DATA = 1

    def func():
        
        lock.acquire() <-- another thread tries to access SHARED_DATA
        lock.acquire()
        SHARED_DATA += 1
        lock.release()

    """
