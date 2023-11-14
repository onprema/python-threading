"""
asyncio example:
- Utilizes coroutines in a single-threaded event loop
"""
import asyncio

# coroutine functions use the `async` and `await` keywords
async def task1():
    print("Task 1 started")
    await asyncio.sleep(5)  # Simulate a non-blocking operation
    print("Task 1 completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(2)  # Simulate another non-blocking operation
    print("Task 2 completed")

async def main():
    # Run both tasks concurrently
    await asyncio.gather(task1(), task2())

# Run the event loop to execute the asynchronous tasks
asyncio.run(main(), debug=True)
