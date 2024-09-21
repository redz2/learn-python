## Async Routes
1. IO密集型任务(e.g. open file, db call, external API call)
* sync routes runs in threadpool
* async routes runs in event loop
* 线程的花销比协程大
```
@router.get("/terrible-ping")
async def terrible_ping():
    time.sleep(10) # I/O blocking operation for 10 seconds, the whole process will be blocked
    return {"pong": True}

@router.get("/good-ping")
def good_ping():
    time.sleep(10) # I/O blocking operation for 10 seconds, but in a separate thread for the whole `good_ping` route
    return {"pong": True}

@router.get("/perfect-ping")
async def perfect_ping():
    await asyncio.sleep(10) # non-blocking I/O operation
    return {"pong": True}
```

2. CPU密集型任务
* send task to another process
