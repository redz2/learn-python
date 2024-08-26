import asyncio
import aioredis


# 如果异步耗时操作只有一次，其实用不用区别不大

async def main():
    # Redis client bound to single connection (no auto reconnection).
    redis = aioredis.from_url(
        "redis://localhost", encoding="utf-8", decode_responses=True
    )
    async with redis.client() as conn:
        await conn.set("my-key", "value")
        val = await conn.get("my-key")
    print(val)

async def redis_pool():
    # Redis client bound to pool of connections (auto-reconnecting).
    redis = aioredis.from_url(
        "redis://localhost", encoding="utf-8", decode_responses=True
    )
    await redis.set("my-key", "value")
    val = await redis.get("my-key")
    print(val)

if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(redis_pool())