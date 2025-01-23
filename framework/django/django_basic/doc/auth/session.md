## Session
### 启用admin后台管理后多了啥？如何让浏览器能带session id？
1. 生成了Users、Roles、Permissions这几张表（如何自定义User？）
2. 自动生成用户管理的视图函数: login、logout
3. 针对注册的app，自动生成增删改查的接口

### django session 认证流程？需要知道是谁在访问
1. session中间件: 从cookie中获取sessionID，保存到request.session
2. authentication中间件: 通过sessionID获取User对象，保存到request.user
3. django中如何设置未登录用户不能访问视图函数？判断request对象中是否有user属性
    * request.user.is_authenticated
    * @login_required() 检查用户是否登录
4. drf中的SessionAuthentication认证模块，完全使用django中session中间件认证流程
    * 判断是否登录（解析并获取User）
    * 如果所有的视图函数都需要用户登录，可以在认证模块中抛出异常

### 如果不用session，换成token呢？整个过程是一样的，不过需要我们自己实现（生成token，校验token）

* django自带的auth模块: https://www.cnblogs.com/wcwnina/p/9246228.html
```python
from django.contrib.auth import authenticate, login, logout

# 用户登录 -> 验证账号密码是否正确 -> session id -> 浏览器
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # 1. 用户认证: 验证用户名和密码，返回User对象（可以自定义认证过程）
        # 只有第一次需要用户名密码校验，后面只需要查看session表中是否存在
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # 2. 生成sessionID并保存
            # login函数:
            # 如果用户认证通过，会生成Session数据(包含用户信息)，把SessionID写入cookie，并记录到数据库中
            # 后续请求，AuthenticationMiddleware会通过cookie中的SessionID
            # 通过查询数据库得到用户信息，添加到request.user中（当然会进行密码校验）
            # 在视图函数中通过request.user获取当前登录用户
            # 如果请求中没有cookie，那么就会重定向到登录页面
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

# django默认使用session，login和logout用来管理session
def logout_view(request):
    # 内置的logout()函数，清除Session id
    logout(request)
    return redirect('login')

# 用户登录过后才能访问视图函数
# 通过认证并不意味着用户有任何权限
def home(request):
    # 如果是真正的User对象，is_authenticated()返回True
    # 通过中间件判断请求中是否带sessionID，并从存放session的数据库中获取用户信息
    if request.user.is_authenticated:
        return render(request, 'home.html', {'username': request.user.username})
    else:
        return redirect('login')

@login_required
def my_view(request):
    pass
```

```python
# django维护一个认证类列表，调用django.contrib.auth.authenticate()，会进行认证
# 当经过authentication中间件，会对用户密码进行校验，返回User

# setttings中配置认证类
AUTHENTICATION_BACKENDS = ['yourfilepath.CustomBackend']
# 如何自定义认证类？login_view -> authenticate(user, password)
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
# 继承ModelBackend类，重写authenticate()方法
class CustomBackend(ModelBackend):
    """
    自定义用户验证后端：支持用户名或邮箱登录。
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        # return: User or None
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None
```

* 自定义auth模块的User模型
```py
# settings.py中添加配置
AUTH_USER_MODEL = "app名.UserInfo"

from django.contrib.auth.models import AbstractUser

# 继承AbstractUser类
class UserInfo(AbstractUser):　　　　
    """
    用户信息表
    """
    nid = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=11, null=True, unique=True)
    
    def __str__(self):
        return self.username
```