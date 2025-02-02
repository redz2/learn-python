# 如何使用中间件？
# 1. 编写中间件 -> process_request -> process_response
# 2. 注册中间件 -> settings.py -> MIDDLEWARE

from django.shortcuts import HttpResponse
from django.utils.deprecation import MiddlewareMixin

# MiddlewareMixin原理
# 原始方式
class TestMiddleware():

    def __init__(self, get_response):
        self.get_response = get_response

    # django内部默认会执行call方法
    def __call__(self, request):

        # 通过反射的机制，执行前处理和后处理函数，把代码分开了（研究一下反射: getattr和hasattr）
        # 前处理
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        response = response or self.get_response(request)
        # 后处理 
        if hasattr(self,'process_response'):
            reponse = self.process_response(request, response)
        return response

    def process_request(self, request):
        # 是否执行路由匹配
        # data = getattr(request, "resolver_match", "no data")
        # print(data)
        # print("TestMiddleware 前处理")
        # 可以不返回，也可以提前终止
        # return HttpResponse("密码错误")
        pass

    def process_view(self, request, view_func, *args, **kwargs):
        # django源码会把process_view放入列表中，依次执行
        pass

    def process_response(self, request, response):
        # print("TestMiddleware 后处理")
        # 这里一定要有返回值
        return response



class BasicMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 权限控制
        pass

    def process_response(self, request, response):
        # 浏览器限制: 同源策略，在响应头中添加字段
        return response