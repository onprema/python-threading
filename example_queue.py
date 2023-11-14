"""
Example of a thread-safe queue that uses multiple threads.
"""
import queue
import threading

def put_numbers(q):
    for number in range(5):
        q.put(number)

def put_strings(q):
    for letter in ['a', 'b', 'c']:
        q.put(letter)

def consumer(q):
    while True:
        data = q.get()
        if data is None:
            break
        print(f"Consumed: {data}")

q = queue.Queue()
numbers_thread = threading.Thread(target=put_numbers, args=(q,))
strings_thread = threading.Thread(target=put_strings, args=(q,))
consumer_thread = threading.Thread(target=consumer, args=(q,))

numbers_thread.start()
strings_thread.start()
consumer_thread.start()

numbers_thread.join()
strings_thread.join()
q.put(None)  # signal the consumer to exit
consumer_thread.join()
