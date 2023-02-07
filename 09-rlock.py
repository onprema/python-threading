# Example of using RLocks
# Source: https://stackoverflow.com/a/16568426/7811791
import threading
import time


class Counter:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.lock = threading.RLock()

    def changeA(self):
        with self.lock:
            self.a = self.a + 1

    def changeB(self):
        with self.lock:
            self.b = self.b + self.a

    def changeAandB(self):
        with self.lock:
            self.changeA() # a usual lock would block at here
            self.changeB()


counter = Counter()

counter.changeA()
print(counter.a)

counter.changeB()
print(counter.b)

counter.changeAandB()
print(counter.a, counter.b)