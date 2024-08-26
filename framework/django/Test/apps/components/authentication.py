from rest_framework.authentication import BaseAuthentication
from django.contrib.auth import get_user_model # 获取当前系统中用户表对应的用户模型
from rest_framework.exceptions import APIException,PermissionDenied,NotAuthenticated,AuthenticationFailed
from rest_framework.response import Response
    
###### 认证 ######
# 前提: 服务器需要生成cookie、session、token，返回给客户端（浏览器自动会携带认证信息）
# 目的: 服务器想要识别访问者的身份（什么叫已登录呢？判断request.user是否有值）
    
# 如何进行用户认证？
# 组件: django中间件 or drf的认证模块
# 方式: 通过客户端携带的认证信息（cookie，session，token）获取当前登录用户 -> request.user
# 细节: 怎么获取到当前用户，具体实现各不相同


class CustomAuthentication(BaseAuthentication):
    
    """自定义认证方法"""

    def authenticate(self, request):
        """
        1. 如果验证成功，返回用户信息
        2. 如果验证失败，应该抛出异常
        3. 一旦验证成功，drf会将user存储到request中
        """
        # http://127.0.0.1:8000/components/students/?user=admin&pwd=admin
        # 如何开个后门？？？
        # print(request._request.user)
        user = request.query_params.get("user")
        password = request.query_params.get("pwd")
        if user != "admin" or password != "admin":
            # 认证不通过，不能返回Response，只能抛出异常
            # 最好应该在permission中设置认证不通过
            # raise NotAuthenticated("认证不通过", 401)
            # 直接返回
            return None
        user = get_user_model().objects.first()
        return (user, None) # 固定格式 (用户对象, None) -> 设置 request.user
    
# 401 Unauthorized 未认证
# 403 Permission Denied 权限被禁止
        
    