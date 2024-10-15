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

while 1:
    # 建立连接
    conn, addr = sock.accept() # 阻塞函数
    logger.info(f"from client {addr}")
    
    while 1:
        data_json_str = conn.recv(1024)
        file_params = json.loads(data_json_str.decode())
        file_size = file_params.get("file_size")
        file_name = file_params.get("file_name")
        
        with open(f"./uploads/{file_name}", "wb") as f:
            receive_data_len = 0
            while receive_data_len < file_size:
                sock.recv(5096)
                f.write(sock)
        
            
        
        
        
        
