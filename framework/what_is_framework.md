# what is framework?

1. socket 编程

- 基于 socket 手撸一个 web 框架

```python
import socket
from loguru import logger
import subprocess
import struct

# 1. 构建套接字对象
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# 2. 绑定IP和端口
ip_port = ('127.0.0.1', 9999)
sock.bind(ip_port)

# 3. 开始监听
sock.listen(5)

while 1:
    # 4. 等待浏览器来连接
    conn, addr = sock.accept() # 阻塞函数
    logger.info(f"from client {addr}")

    # 5. 接收浏览器发送的消息
    buf = conn.recv(2048)
    print(buf)

    # # # # # # # # # # # # # # # # # # # # # # # # # #
    #
    # Web框架: 解析请求、处理请求
    #
    # url ---> function
    #
    # # # # # # # # # # # # # # # # # # # # # # # # # #

    # 6. 给浏览器返回数据
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
    conn.send(b"Hello World!")

    # 7. 断开连接
    conn.close()

# 8. 停止服务端程序
sock.close()
```

- 几个要素

  - uwsgi: 提供 web 服务（封装 request、response，下面是一个最简单的 wsgi 的实现）

  ```python
  from wsgiref.simple_server import make_server

  def run_server(environ, start_response):
      """
      WSGI协议规范
      environ: 请求信息
      start_response: 生成响应头
      return: 返回请求体
      """
      start_response('200 OK', [('Content-Type', 'text/html')])
      return [bytes('<hl>Hello, web!</hl>', encoding='utf-8'),]

  if __name__  == "__main__":
      httpd = make_server('127.0.0.1', 8000, run_server)
      httpd.serve_forever()
  ```

  - WSGI: 接口规范（web 框架需要遵循）

  - web 框架: 基于 WSGI 构建，提供了一个 WSGI 应用程序对象（如何解析一个请求？如何处理一个请求？）
    1. django + wsgiref（框架自带 WSGI 实现，生产一般用 uwsgi）
    2. flask + werkzeug

2. 主流 web 框架对比

- 功能集成
  - django: 相对大
  - 其他（flask,fastapi）: 相对小
- 同步框架 vs 异步框架
  - 异步非阻塞: tornado、sanic、fastapi、django
  - 同步: django、flask、bottle、web.py
- fastapi 如何处理多个请求？异步非阻塞
  - 单线程处理（基于事件循环，去处理请求）
  - IO 多路复用（请求列表、任务列表...: 如何处理 IO 耗时任务？）
    - 单线程会从请求列表中处理每个请求，并在处理请求时，将耗时操作放到任务列表中（例如 IO 操作，绝对不能占用单线程的时间）
    - 问题: 如果同一时刻有百万级的访问量，单线程就不太来得及处理了
      - 多起几个线程一起处理
- django 如何处理多个请求？同步阻塞
  - 通过多线程处理
  - celery（IO 耗时或非 IO 耗时）: 任务队列 + worker + 结果队列
