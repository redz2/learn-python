# Web框架
* 浏览器 ---> socket ---> Web框架 ---> 业务逻辑
* 主流框架对比
    * 功能集成
        * django: 相对大
        * 其他（flask,fastapi）: 相对小
    * 同步框架 vs 异步框架
        * 异步非阻塞: tornado、sanic、fastapi、django
        * 同步: django、flask、bottle、web.py
    * fastapi如何处理多个请求？
        * 单线程处理（基于事件循环，处理IO耗时任务）
        * IO多路复用（请求列表，任务列表...）
    * django如何处理多个请求？
        * 通过多线程处理
        * celery（IO或非IO耗时）
            * 默认多进程

# Django
1. 安装django
```
pip3 install django
```

2. 创建django项目
```
django-admin startproject myproject  # 直接创建项目会生成如下目录结构

myproject
|-- manage.py [项目管理工具]
|-- myproject
    |-- __init__.py
    |-- settings.py [配置文件，先读取django源码内配置，再读取settings配置，会覆盖]
    |-- urls.py [主路由]
    |-- asgi.py [异步]
    |-- wsgi.py [同步]
```

3. 创建venv虚拟环境（不要随便改项目的名称和目录，虚拟环境activate会失效）
```
cd myproject
python -m venv .venv
source .venv/bin/activate
```

```
pip3 install django
django-admin startproject myproject . # 这样就可以在当前目录中创建项目了，项目名称和目录名称最好要一致！
```

4. 创建多app（建议这么放）
```
cd myproject
mkdir apps
cd apps
python3 ../manage.py startapp myapp
```

5. Http请求的生命周期
    * 路由
        1. 传统写法
        2. 正则写法
        3. 分组
    * 视图
    * 模板
    * 静态文件和媒体文件
    * 中间件
    * ORM