## cookie
***
![cookie原理](png/cookie.png)
***
1. 如何生成cookie？cookie保存在客户端
```python
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 模拟验证用户: 类似于自带的authenticate函数
        user = User.objects.filter(username=username, password=password).first()
        if user:
            # 设置认证 Cookie
            response = HttpResponseRedirect('/home/')
            # 浏览器下次请求时会设置 Cookie
            # cookie 为什么容易伪造？因为都是写用户信息
            # cookie 在服务器端无法控制，只能等待过期
            response.set_cookie('user_id', user.id, max_age=3600)  # 1小时有效期
            return response
        else:
            return HttpResponse('登录失败')
    return render(request, 'login.html')  # 假设您有一个登录页面模板
```

2. 如何进行用户认证？获取用户
    * django默认用的是session，cookie已经不怎么用了
    * 所以并没有中间件处理cookie
    * 而session有中间件去解析，得到用户
```python
def home(request):
    # 1. 在视图函数中检查是否有cookie，获取登录用户信息
    user_id = request.COOKIES.get('user_id')
    if user_id:
        user = User.objects.get(id=user_id)
        return HttpResponse(f'欢迎，{user.username}')
    else:
        return HttpResponseRedirect('/login/')
```

3. drf中如何进行认证？每个视图类方法都会通过认证类，认证后会设置request.user的值
```python
class CookieAuthentication(BaseAuthentication):
    def authenticate(self, request):
        user_id = request.COOKIES.get('user_id')
        if user_id:
            try:
                # 假设您从数据库根据用户 ID 获取用户
                user = YourUserModel.objects.get(id=user_id)  
                return (user, None)
            except YourUserModel.DoesNotExist:
                return None
        return None

class YourAPIView(APIView):
    authentication_classes = [CookieAuthentication]

    def get(self, request):
        # 认证成功后，您可以在这里访问用户信息
        user = request.user  
        return Response({'message': f'Hello, {user.username}'})

```