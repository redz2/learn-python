import socket
import time
import os
import struct
import json

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
ip_port = ('127.0.0.1', 9999)
sock.connect(ip_port) 

# server端给client端发送大数据

# 粘包现象：数据可能会合并
while 1:
    # put a.png
    cmd = input("cmd> ")
    # 上传文件信息
    local_path = cmd.split(" ")[1]
    file_size = os.path.getsize(local_path)
    file_name = os.path.basename(local_path)
    file_param = {"file_name": file_name, "file_size": file_size}
    # sock.send会将字符串编码成utf-8字节
    sock.send(json.dumps(file_param))

        