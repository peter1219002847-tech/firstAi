import asyncio
import aiohttp
import time


async def fetch_url(session, url):
    start_time = time.time()
    async with session.get(url) as response:
        await response.text()
        response_time = time.time() - start_time
        return f"{url}耗时 {response_time:.2f}ms"


async def main():
    urls = [
        "https://www.baidu.com",
        "https://www.bing.com",
        "https://www.github.com"
    ]

    async with aiohttp.ClientSession() as session:
        print("\n---并发请求----")
        start_time = time.time()
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result)
        print(f"并发总耗时：{time.time() - start_time:.2f}ms")

if __name__ == "__main__":
    asyncio.run(main())