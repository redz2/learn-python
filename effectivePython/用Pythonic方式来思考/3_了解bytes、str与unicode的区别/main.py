"""
python3
bytes ===> 包含8位值的字节序列
str ===> 包含Unicode字符的序列（一个Unicode字符有多大）

python2
str ===> 包含8位值的序列
unicode ===> 包含Unicode字符的序列

# print只认Unicode
计算机内存（Unicode字符） <--->  计算机存储与网络传输（使用UTF-8编码的字节序列 --> bytes）
计算机内存（对象） <--->  计算机存储与网络传输（Json字符串）
"""

a = '中文'
print(len(a))

a.encode('utf-8') 
a.encode('ascii') # 无法显示为ascii的字符，用\x##表示


