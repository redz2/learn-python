# 中间件
1. 中间件: 本质
    * 初始化一个类 -> 执行__call__ -> 执行process_request -> 执行get_response -> 获取下一个中间件
                    -> 如果有重复上面的步骤
                        -> 执行process_request
                        -> 执行get_response -> 获取下一个中间件
                    -> 如果没有执行视图函数
                        -> 执行process_response（最后的中间件）
                            -> 执行process_response
```python
class MyMiddleware(Object):
    def __init__(self, get_response):
        self.get_resposne = get_response

    def __call__(self, request):
        # 前处理
        if hasattr(self, "process_request"):
            self.process_request(request)
        response = get_response(request)
        # 后处理
        if hasattr(self, "process_response"):
            self.process_response(request, response)
        return response
```
2. MiddlewareMixin: 实际编写
    * 定义一个类，继承MiddlewareMixin，实现process_request和process_response
    * Minin: 提供方法
    * 通过类来编排、扩展处理流程
```python
class MyMiddleware(MiddlewareMixin):

    """
    1. 需要明白中间件的执行过程？
    2. 使用场景有哪些？
    """
    def process_request(self, request):
        """还未进行路由匹配，不知道执行哪个视图函数"""
        do_something_with_request(request)
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        执行完所有中间件的process_request，并且执行完路由匹，会依次执行中间件中的process_view，然后再执行视图函数
        """
        ...
    
    def process_response(self, request, responses):
        response = do_something_with_response(request, response)
        return response

    def process_exception(self, request, exception):
        """视图函数抛出异常时，会捕获异常，我们可以自定义异常页面"""
        ...

    def process_template_response():
        """视图函数中返回的是TemplateResponse对象: 有一个render方法"""
        ...
```
3. 中间件的应用场景
    * 用户登录: 通过process_request解析token或者cookie，将用户信息添加到request.User
    * 跨域: 浏览器限制: 同源策略，在响应头中添加字段，通过process_response添加响应头