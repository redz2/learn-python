# FastAPI会对路径操作函数(path operation function)和依赖(dependencies)进行特殊处理。
# 这个特殊处理是：
# 如果你把函数定义为def而不是async def，那么FastAPI会把它放到单独的线程池中，异步执行，这就是FastAPI精彩的地方。
# 就像官方所说，如果你不清楚你函数里面的调用是不是异步(能不能用await)，那么就把它定义为普通函数，FastAPI会采用多线程的方式处理。
# 乱用async，在async里面有同步调用，则会变成串行，Fast秒变Slow。
# 而对于其他函数，FastAPI则不会管，def就是同步调用，立马返回结果。
# 现在回过头来看前面的那句话：就是无论你是否使用async，FastAPI都将异步工作，以达到"Fast"的运行速度。应该更加明白了。


from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

# 启动fastapi
# uvicorn main:app --reload --host 127.0.0.1 --port 1234