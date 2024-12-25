"""
最简单、最基础的wsgi服务
"""
from wsgiref.simple_server import make_server

def run_server(environ, start_response):
    """
    遵循WSGI协议
    environ: 请求信息
    start_response: 生成响应头
    return: 返回请求体
    """
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [bytes('<hl>Hello, web!</hl>', encoding='utf-8'),]
           
if __name__  == "__main__":
    httpd = make_server('127.0.0.1', 8000, run_server)
    httpd.serve_forever()
