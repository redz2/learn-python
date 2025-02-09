# 异常处理 Exceptions
# drf框架在APIView中提供了异常处理，但是仅针对drf内部现有接口开发相关的异常做了处理
# drf没法处理的异常会冒泡给django

# django怎么处理404页面不存在的告警呢？

from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
"""
Returns the response that should be used for any given exception.

By default we handle the REST framework `APIException`, and also
Django's built-in `Http404` and `PermissionDenied` exceptions.

Any unhandled exceptions may return `None`, which will cause a 500 error
to be raised.
"""

# setttings中添加配置
# 'EXCEPTION_HANDLER': 'apps.components.errhandle.custom_exception_handler',
def custom_exception_handler(exc, context):
    
    """
    自定义异常函数
    exc: 异常实例对象，
    context: 字典，异常发生时python解释器收集的执行上下文信息
    所谓的执行上下文就是python解释器在执行代码时保存在内存中的变量、函数、类、对象、模块等一系列的信息组成的
    
    drf能处理的异常
    # 1. Http404 -> get_object()查询数据时抛出的Http404异常
    # 2. 权限拒绝错误，包括django的PermissionDenied -> 判断权限的异常
    # 3. 自定义的APIException错误
    """
    # 先让drf处理他能处理的异常
    response = exception_handler(exc, context)
    if response is None:
        # 如果response为None，表示当前异常drf无法处理
        # 我们可以自己处理异常，添加不同的异常类型进行不同的处理
        if isinstance(exc, Exception):
            response = Response({"detail": "我能自己处理异常了"}, status=status.HTTP_400_BAD_REQUEST)
        if isinstance(exc, Http404):
            response = Response({'detail': '对不起，您访问的资源不存在'}, status=status.HTTP_404_NOT_FOUND)
            
        # 一般我们要处理哪些异常呢？
        # http请求，数据库操作(get_object() -> 获取当个模型对象时如何处理错误？)
    return response
