import socket
from loguru import logger
import subprocess
import struct

# 构建套接字对象
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# IP和端口
ip_port = ('127.0.0.1', 9999)
sock.bind(ip_port)
sock.listen(5)

def my_cmd(cmd):
    # cmd = "ifconfig"
    logger.info("run cmd")
    output = subprocess.getoutput(cmd)
    return output

while 1:
    # 建立连接
    conn, addr = sock.accept() # 阻塞函数
    logger.info(f"from client {addr}")
    
    while 1:
        # 接收数据
        data_bytes = conn.recv(1024) # 阻塞函数，最大1024字节
        # 执行cmd
        cmd = data_bytes.decode()
        # client意外退出或者主动退出
        if cmd == "quit":
            break
        # 处理数据
        res = my_cmd(cmd)
        data = res.encode()
        # server返回给client的数据可能比较大，需要先发送数据长度，再发送数据本身
        # 分两次发送就会出现粘包问题：可能会一起send
        # 如何解决粘包问题？客户端先接收一个固定长度的字节，解析出数据长度，再循环接收数据
        cmd_len_bytes = struct.pack("i", len(data))
        conn.send(cmd_len_bytes)
        # 再返回数据
        conn.send(data)