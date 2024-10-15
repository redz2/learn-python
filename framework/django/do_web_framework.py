"""
基于socket手撸一个web框架

uwsgi + web框架
wsgiref + django
werkzeug + flask
"""

import socket
from loguru import logger
import subprocess
import struct

# 1. 构建套接字对象
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# 2. 绑定IP和端口并监听端口
ip_port = ('127.0.0.1', 9999)
sock.bind(ip_port)
sock.listen(5)

while 1:
    # 3. 等待浏览器来连接
    conn, addr = sock.accept() # 阻塞函数
    logger.info(f"from client {addr}")
    
    # 4. 接收浏览器发送的消息
    buf = conn.recv(2048)
    print(buf)
    
    # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # 
    # Web框架: 提取请求头、请求体、url地址，处理业务
    # 
    # url ---> function
    # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # 
    
    # 5. 给浏览器返回数据
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
    conn.send(b"Hello World!")
    
    # 断开连接
    conn.close()
    
# 停止服务端程序
# sock.close()
    
