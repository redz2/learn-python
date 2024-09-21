import socket
import time
import struct

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
ip_port = ('127.0.0.1', 9999)
sock.connect(ip_port) 

# server端给client端发送大数据

# 粘包现象：数据可能会合并
while 1:
    cmd = input("cmd> ")
    if cmd == "quit":
        break
    # 把数据发送给服务器
    sock.send(f"{cmd}".encode())
    # 等待服务器返回数据
    time.sleep(1)
    # 如何解决粘包问题？
    # client客户端去socket中获取数据时，len和data都已经发送过来了，sock.recv(1024)会直接拿到所有的数据
    # 让len固定为4个字节，client就只取4个字节
    cmd_len_bytes = sock.recv(4) # 阻塞
    total_size = struct.unpack("i", cmd_len_bytes)[0]
    current_len = 0
    # 再接收数据
    while current_len < total_size:
        data = sock.recv(1024)
        print(data.decode())
        current_len += 1024
        