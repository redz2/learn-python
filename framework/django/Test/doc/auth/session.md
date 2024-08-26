## Session

### 对于浏览器来说，只有是否登录两种状态，那登录后浏览器获得了什么？-> session id or token or cookie 有还是没有

### 启用admin后台管理后多了啥？如何让浏览器能带session id？
1. 生成了Users、Roles、Permissions这几张表
2. 写了login视图函数 -> is_authenticated() -> login() -> session id -> 返回给浏览器

### django session 认证流程？需要知道是谁在访问
1. session中间件 -> 从COOKIE中获取session id -> request.session
2. authentication中间件 -> 基于session id获取User对象 -> request.user
3. django中如何设置未登录用户不能访问视图函数？
    * request.user.is_authenticated
    * @login_required() 检查用户是否登录
4. drf中的SessionAuthentication，完全使用django中session认证流程
    * 如果所有的视图函数都需要用户登录，可以在认证模块中抛出异常

### 如果不用session，换成token呢？整个过程其实是一样的


```
from django.contrib.auth import authenticate, login, logout

# 用户登录 -> 验证账号密码是否正确 -> session id -> 浏览器
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # 验证用户名和密码，返回User对象
        user = authenticate(request, username=username, password=password)
        if user is not None:

            # 内置login()函数 -> 生成Session数据，存入user_id，然后把Session id写入Cookie
            # 后续每一次请求，AuthenticationMiddleware中的process_request方法会根据user_id获取User对象，添加到request.user中
            # 视图函数 -> 通过request.user获取当前登录用户
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):

    # 内置的logout()函数，清除Session id
    logout(request)
    return redirect('login')

# 用户登录过后才能访问视图函数
def home(request):

    # 如果是真正的User对象，is_authenticated()返回True
    # 通过认证并不意味着用户有任何权限
    if request.user.is_authenticated:
        return render(request, 'home.html', {'username': request.user.username})
    else:
        return redirect('login')

@login_required
def my_view(request):
    pass
```