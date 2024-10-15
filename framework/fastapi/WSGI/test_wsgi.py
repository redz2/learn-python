# WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求
# pre-fork worker model
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']

# 从wsgiref模块导入，这个WSGI服务器只能用于开发测试
from wsgiref.simple_server import make_server

# 创建一个服务器，IP地址为空，端口是8002，处理函数是application:
httpd = make_server('', 8002, application)
print('Serving HTTP on port 8002...')
# 开始监听HTTP请求:
httpd.serve_forever()

# WEB应用的本质
#   浏览器发送一个HTTP请求
#   服务器收到请求，生成一个HTML文档
#   服务器把HTML文档作为HTTP响应的Body发送给浏览器
#   浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示

# 其中接受HTTP请求、解析HTTP请求、发送HTTP响应都是苦力活，都交给WSGI
# WSGI服务器接收客户端请求，转发给WebAPP，APP处理完成后把响应返回给WSGI服务器，由WSGI服务器返回给客户端

# WEB SERVER <---> WEB APP
# WSGI是进程内代码调用规范，不是进程间通信协议
# 在WSGI之上，再抽象出Web框架，进一步简化开发，所以python的web框架比如django，fastapi都是WEBAPP，WSGI服务器是WEBSERVER



