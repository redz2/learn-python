from typing import Union, Optional, List, Tuple, Dict
from fastapi import FastAPI, Request

app = FastAPI()

# 自定义中间件
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    # 前处理
    start_time = time.perf_counter()
    # 处理请求
    response = await call_next(request)
    # 后处理
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# CORS中间件
# 处理跨域请求
from fastapi.middleware.cors import CORSMiddleware

# 哪些域名可以跨域访问
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    # "*",
]

app.add_middleware(
    CORSMiddleware,
    # Access-Control-Request-Headers: <field-name>[, <field-name>]*
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 如何使用其他中间件？
# 和CORS类似


# 静态文件
from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"))

"""
1. fastapi支持各种请求方法
@app.get()
@app.post()
@app.put()
@app.patch()
@app.delete()
@app.options()
@app.head()
@app.trace()
"""
@app.get("/")
def read_root(request: Request):
    """
    需要用到request再传入
    """
    return {
        "request_url": request.url,
        "request_host": request.client.host,
        "request_headers": request.headers.get("user-agent"),
        "request_cookies": request.cookies,
    }

# 自带接口文档
# http://127.0.0.1:8000/docs/
# 接口文档描述
@app.get("/home", tags=["this is tag"],
        summary="this is summary", description="this is description",
        response_description="this is response description",
        deprecated=True
        )
def home():
    return {"user_id": 1}


# http://127.0.0.1:8000/items/1?q=test
# 路径参数?查询参数
# 请求头
# 请求体
@app.get("/items/{item_id}")
def read_item(item_id: int, 
              r: int, # 如果没有默认值，必须要传参数
              q: Union[str, None] = None, # 如果有默认值，可以不传参数
              k: Optional[str] = None, # Union[str, None]简写
              ): # type hint 会自动做类型转换（TMD，默认值和类型不匹配就没事）
    """
    函数参数 = 路径参数 + 查询参数（非路径参数都会被认为是查询参数）
    函数参数的类型转换是fastapi做的
    """
    return {"item_id": item_id, "r": r, "q": q, "k": k}


"""
2. 路由分发: include.router
"""
# 框架默认会把main.py所在目录设置环境变量
from apps.app01.urls import user
from jinja.urls import jj
app.include_router(user, prefix="/user", tags=["app01 tag"])
app.include_router(jj, prefix="/jinja", tags=["jinja tag"])



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("do_fastapi:app", port=8000, reload=True)