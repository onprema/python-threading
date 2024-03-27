# GIL (Global Interpreter Lock)

Python has _real_ threads, but only one thread can hold the GIL at a time, so only one thread gets executed at a time.

`sys.getswitchinterval()` shows how often the Python interpreter pauses the current thread (how often the GIL gets released).

> Every Python standard library function that makes a syscall releases the GIL. This includes all functions that perform disk I/O, network I/O, and time.sleep()

> The effect of the GIL on network programming with Python threads is relatively small, because the I/O functions release the GIL, and reading or writing to the network always implies high latency—compared to reading and writing to memory.

## Why does it exist?
To simplify memory management. Without the GIL, developers would have to implement more fine-grained locking mechanisms to prevent multiple threads from simultaneously modifying Python objects, which could lead to data corruption and other concurrency issues.

## PEP703
Making the Global Interpreter Lock Optional in CPython ([link](https://peps.python.org/pep-0703/))
