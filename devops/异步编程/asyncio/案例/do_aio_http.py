# aiohttp
# httpx

import asyncio

import aiohttp
import httpx

async def aiohttp_demo():
    print("start: aiohttp")
    async with aiohttp.ClientSession() as session:
        async with session.get('http://www.baidu.com') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")

async def httpx_demo():
    print("start: httpx")
    async with httpx.AsyncClient() as client:
        resp = await client.get('http://www.baidu.com')
        print("status-code:", resp.status_code)
        print(resp.text)


async def main():
    tasks = [
        asyncio.create_task(aiohttp_demo()),
        asyncio.create_task(httpx_demo())
    ]
    done, pending = await asyncio.wait(tasks)

# 不能这么写
# sys:1: RuntimeWarning: coroutine 'aiohttp_demo' was never awaited
# sys:1: RuntimeWarning: coroutine 'httpx_demo' was never awaited
# tasks = [
#     httpx_demo(),
#     aiohttp_demo()    
#     这里肯定不能写task，因为事件循环还未启动   
# ]
# asyncio.run(asyncio.wait(tasks))

asyncio.run(main())