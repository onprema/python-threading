import asyncio
import httpx # https://www.python-httpx.org/

async def fetch_data(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text

async def main():
    url1 = "https://jsonplaceholder.typicode.com/posts/1"
    url2 = "https://jsonplaceholder.typicode.com/posts/2"

    # Fetch data from two URLs concurrently
    task1 = fetch_data(url1)
    task2 = fetch_data(url2)

    # Use asyncio.gather to run both tasks concurrently
    results = await asyncio.gather(task1, task2)

    # Process the results
    for i, result in enumerate(results, 1):
        print(f"Result from Task {i}: {result}")

# Run the event loop to execute the main coroutine
asyncio.run(main())
