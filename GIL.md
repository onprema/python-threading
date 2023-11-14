# GIL (Global Interpreter Lock)

Python has _real_ threads, but they go through the GIL, so only one thread gets executed at a time.

## Why does it exist?
To simplify memory management. Without the GIL, developers would have to implement more fine-grained locking mechanisms to prevent multiple threads from simultaneously modifying Python objects, which could lead to data corruption and other concurrency issues.

## PEP703
Making the Global Interpreter Lock Optional in CPython ([link](https://peps.python.org/pep-0703/))
