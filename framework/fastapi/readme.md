1. 安装fastapi
```
pip3 install fastapi
```

2. 安装ASGI服务器
```
pip3 install uvicorn
```

3. 启动fastapi服务
```
fastapi run do_fastapi.py 生产环境
fastapi dev do_fastapi.py 测试环境
```

4. Gunicorn vs Uvicorn vs Werkzeug vs uWSGI
* Werkzeug
    * 是一个WSGI工具库，提供一个简单的服务器，主要用于开发和测试
    * Flask内置服务器

* uWSGI
    * 支持WSG、ASGI和其他协议，更加通用

* Gunicorn（易于配置和使用）
    * 是一个Python WSGI HTTP服务器，通过使用多个进程来提供高性能的处理
    * 传统同步Web应用（django，flask）
```
gunicorn -w 1 -b 127.0.0.1:8000 app:app
```

* Uvicorn（易于配置和使用）
    * 轻量级的ASGI服务器，专为异步Web框架设计（fastapi，starlette）
    * 高性能的异步处理
```
uvicorn do_fastapi:app --host 0.0.0.0 --port 8000 --reload
```

* 综合使用Gunicorn和Uvicorn
    * gunicorn -w 4 -k uvicorn.workers.UvicornWoker app:app



