from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

# 子路由接口对象
jj = APIRouter()

templates = Jinja2Templates(directory="jinja/templates")

@jj.get("/test")
def jinja_test(request: Request):
    # 1. 从数据库中获取数据
    # 2. 通过模板文件生成结果(前后端不分离，谁来渲染页面)
    # 3. 直接返回json(前后端分离)
    return templates.TemplateResponse(
        "index.html", # 模板文件
        {
            "request": request,
            "name": "zhouyi",
            "age": 20,
            "books": [
                "水浒传",
                "三国演义",
                "红楼梦",
                "西游记",
            ]
        }, # context上下文对象
    )