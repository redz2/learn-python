## cookie

![cookie原理](png/cookie.png)

### 是不是可以给Cookie也写个中间件，把用户信息 -> request.user

1. 登录以后如何设置cookie？客户端会存储cookie信息
```
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 模拟验证用户
        user = User.objects.filter(username=username, password=password).first()

        if user:

            # 设置认证 Cookie
            response = HttpResponseRedirect('/home/')
            # 浏览器下次请求时会设置 Cookie
            # cookie 为什么容易伪造？因为都是写用户信息
            # cookie 在服务器端无法控制，只能等待过期
            response.set_cookie('user_id', user.id, max_age=3600)  # 1 小时有效期
            return response
        else:
            return HttpResponse('登录失败')
    return render(request, 'login.html')  # 假设您有一个登录页面模板
```

2. django中如何进行认证？在视图函数中获取Cookie，从而获取用户信息；或者写一个认证的中间件，设置request.user的值为登录用户
```
def home(request):

    # 检查认证 Cookie
    user_id = request.COOKIES.get('user_id')
    if user_id:
        user = User.objects.get(id=user_id)
        return HttpResponse(f'欢迎，{user.username}')
    else:
        return HttpResponseRedirect('/login/')
```

3. drf中如何进行认证？每个视图类方法都会通过认证类，认证后会设置request.user的值
```
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