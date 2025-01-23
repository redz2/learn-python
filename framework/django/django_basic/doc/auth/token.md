# token
[token](png/token.png)

## 和cookie、session的相同处
* 都是把东西给浏览器，不过是给不同的东西
1. 如何生成token？login -> token（当然也可以使用第三方平台生成token）
2. 如何验证token？middleware -> 获取token -> 解析用户（这篇文章并没有涉及）

## JWT Token: 如何生成token？如何更新token？
官网地址: https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html
```python
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