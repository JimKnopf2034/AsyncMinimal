import asyncio
import aiohttp
import time


@asyncio.coroutine
def google():
    res = yield from aiohttp.request('GET', 'http://localhost:9090/hello')
    assert(res.status == 200)
    content = yield from res.text()
    return res.status


@asyncio.coroutine
def main():
    res = yield from google()
    print(res)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = []
    for i in range(2):
        tasks.append(main())

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
