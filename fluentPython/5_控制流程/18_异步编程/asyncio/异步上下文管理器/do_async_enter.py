import asyncio

# 用处是什么
class ContextManager:
    def __init__(self):
        self.conn = None

    async def action(self):
        return self.conn
    
    async def do_something(self):
        await asyncio.sleep(5)
        return 666

    async def __aenter__(self):
        print("aenter")
        # 连接数据库
        await self.do_something()
        self.conn = "OK"
        return self

    async def __aexit__(self, exc_type, exc, tb):
        # 关闭数据库连接
        print("aexit")
        self.conn = "CLOSE"

async def main():
    async with ContextManager() as cm:
        result = await cm.action()
        print(result)

asyncio.run(main())