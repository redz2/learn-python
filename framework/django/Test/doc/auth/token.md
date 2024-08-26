# token
[token](png/token.png)

## 和cookie、session的相同处

都是把东西给浏览器，不过是给不同的东西
1. 如何生成token？login -> token
2. 如何验证token？middleware -> authentication -> """request.user""" -> 是否可以访问视图函数


## JWT Token: 如何生成token？如何更新token？
官网地址: https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html
```
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# 自定义 TokenObtainPairSerializer 以添加额外数据
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # 在此添加自定义数据到 token
        token['username'] = user.username
        return token

# 自定义获取 token 的视图
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# 在 urls.py 中配置路由
from django.urls import path

urlpatterns = [
    # 他怎么知道去哪张表中获取用户名和密码
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


```