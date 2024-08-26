[TOC]



为了方便接下来的学习，我们创建一个新的子应用 component

```python
python manage.py startapp component
```

component/urls.py，子路由代码：

```python
from django.urls import path
from . import views

urlpatterns = [
    
]
```

注册子应用，settings.py，代码：

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'stuapi',    # 不使用drf编写api接口
    'students',  # 使用了drf编写api接口
    'sers',      # 演示序列化的使用
    'req',       # drf提供的http请求与响应
    'demo',      # drf提供的提供的视图类
    'component', # drf提供的组件功能
]

```

总路由，代码：

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("stuapi.urls")),
    path('api/', include("students.urls")),
    path('sers/', include("sers.urls")),
    path("req/", include("req.urls")),
    path("demo/", include("demo.urls")),
    path("component/", include("component.urls")),
]

```

因为接下来的认证组件中需要使用到登陆功能，所以我们使用django内置admin站点并创建一个管理员.

admin运营站点的访问地址：http://127.0.0.1:8000/admin

```shell
python manage.py createsuperuser
# 如果之前有账号，但是忘了，可以通过终端下的命令修改指定用户的密码，这里的密码必须8位长度以上的
python manage.py changepassword 用户名
```

![1557276390641](assets/1557276390641.png)

创建管理员以后，访问admin站点，先修改站点的语言配置

settings.py

```
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'
```

![1553043081445](assets/1553043081445.png)

访问admin 站点效果：

![1553043054133](assets/1553043054133.png)

# 1. 认证Authentication

可以在配置文件中配置全局默认的认证方式/认证方案。

开发中常见的认证方式：cookie、**session**、**token**

rest_framework/settings.py 默认配置文件

```python
REST_FRAMEWORK = {
    # 配置认证方式的选项
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication', # session认证
        'rest_framework.authentication.BasicAuthentication',   # basic认证[基于账号密码]
    )
}
```

可以在具体的视图类中通过设置类属性authentication_classess来设置单独的不同的认证方式

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# Create your views here.
class AuthenticationAPIView(APIView):
    # 局部的认证方式，支持多个认证方法
    authentication_classes = [SessionAuthentication]
    def get(self,request):
        print(request.user)
        # AnonymousUser 就是在request.user无法识别当前访问的客户端时的游客用户对象
        return Response("ok")
```

认证失败会有两种可能的返回值，这个需要我们配合权限组件来使用：

- 401 Unauthorized 未认证
- 403 Permission Denied 权限被禁止

自定义认证，`component/authentication.py`，代码：

```python
from rest_framework.authentication import BaseAuthentication
from django.contrib.auth import get_user_model  # 自动识别当前django系统中的系统用户模型


class CustomAuthentication(BaseAuthentication):
    """
    自定义认证方式
    """
    def authenticate(self, request):
        """核心认证方法"""
        user = request.query_params.get("user")
        pwd = request.query_params.get("pwd")
        if user != "root" or pwd != "houmen":
            return None

        # get_user_model获取当前系统中用户表对应的用户模型类
        user = get_user_model().objects.filter(is_superuser=1, is_active=1).first()
        return (user, None)  # 按照固定的返回格式填写 （用户模型对象, None）

```

视图调用自定义认证，视图代码：

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .authentication import CustomAuthentication

# Create your views here.
class AuthenticationAPIView(APIView):
    # 局部的认证方式，支持多个认证方法
    authentication_classes = [CustomAuthentication]
    def get(self,request):
        print(request.user)
        # AnonymousUser 就是在request.user无法识别当前访问的客户端时的游客用户对象
        return Response("ok")

```

当然也可以注释掉上面视图中的配置，改成全局配置。settings.py，代码：

```python
"""drf配置信息必须全部写在REST_FRAMEWORK配置项中"""
REST_FRAMEWORK = {
    # 配置认证方式的选项【drf的认证是内部循环遍历每一个注册的认证类，一旦认证通过识别到用户身份，则不会继续循环】
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'drfdemo.authentication.CustomAuthentication',            # 自定义认证
        'rest_framework.authentication.SessionAuthentication',  # session认证
        'rest_framework.authentication.BasicAuthentication',      # 基本认证
    )
}
```

# 2. 权限Permissions

权限控制可以限制用户对于视图的访问和对于具有模型对象的访问。

- 在APIView视图的dispatch()方法中调用initial方法中先进行视图访问权限的判断

  `self.check_permissions(request)`

- 在GenericAPIView通过get_object()获取具体模型对象时，会进行模型对象访问权限的判断

  `self.check_object_permissions(self.request, obj)`

## 使用

可以在配置文件restframework/settings.py中默认的**全局设置**了权限管理类，源码：

```python
REST_FRAMEWORK = {
    ....
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',  # AllowAny 表示允许任何用户访问站点视图
    ],
}
```

如果要在项目覆盖默认配置rest_framework/settings.py的设置，则可以在项目配置文件中，settings.py，代码：

```python
"""drf的配置"""
# from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
REST_FRAMEWORK = {
    # 配置认证方式的选项[全局配置]
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication', # session认证
        'rest_framework.authentication.BasicAuthentication',   # basic认证[基于账号密码]
    ],
    # 配置权限的选项[全局配置]
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
```

也可以在具体的视图类中通过类属性permission_classes来进行**局部设置**，如

```python

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from demo.serializers import StudentModelSerializer, Student
class PermissionAPIView(ModelViewSet):
    authentication_classes = [CustomAuthentication]
    permission_classes = [AllowAny]  # 针对封闭内部系统，登录页面时谁都可以访问。
    # permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
```

## 提供的权限

- AllowAny 允许所有用户进行操作访问，默认权限
- IsAuthenticated 仅通过登录认证的用户进行操作访问
- IsAdminUser 仅允许管理员用户进行操作访问
- IsAuthenticatedOrReadOnly 已经登陆认证的用户可以对数据进行增删改操作，没有登陆认证的游客只能查看数据。

打开浏览器的无痕模式：Ctrl+Shift+N

## 举例

视图代码：

```python
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from demo.serializers import StudentModelSerializer, Student
class PermissionAPIView(ModelViewSet):
    # authentication_classes = [CustomAuthentication]
    # permission_classes = [AllowAny]  # 针对封闭内部系统，登录页面时谁都可以访问。
    permission_classes = [IsAdminUser]  # 设置当前视图，只有是管理员可以访问操作。
    # permission_classes = [IsAuthenticatedOrReadOnly]  # 登录用户可以操作，而游客只能查看数据
    # permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

```

路由代码：

```python
from django.urls import path, re_path
from . import views

urlpatterns = [
    path("auth", views.AuthenticationAPIView.as_view()),
    path("pess/", views.PermissionAPIView.as_view({"get": "list", "post": "create"})),
    re_path("^pess/(?P<pk>\d+)/$", views.PermissionAPIView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
]
```



## 自定义权限

如需自定义权限，需继承rest_framework.permissions.BasePermission父类，并实现以下两个任何一个方法或全部

- `.has_permission(self, request, view)`

  是否可以访问视图， view表示当前视图对象，request可以通过user属性获取当前用户

- `.has_object_permission(self, request, view, obj)`

  是否可以访问模型对象， view表示当前视图， obj为模型数据对象，request可以通过user属性获取当前用户

例如：

在当前子应用下，创建一个权限文件permissions.py中声明自定义权限类：

```python
from rest_framework.permissions import BasePermission


class VVIPPermission(BasePermission):
    """
    VVIP权限
    自定义权限，可用于全局配置，也可以用于局部配置
    """

    def has_permission(self, request, view):
        """
        视图权限
        返回结果未True则表示允许访问视图类
        request: 本次客户端提交的请求对象
        view: 本次客户端访问的视图类
        """
        # # 写在自己要实现认证的代码过程。
        identity = request.query_params.get("identity")
        # # 返回值为True，则表示通行
        return identity == "vvip"

    def has_object_permission(self, request, view, obj):
        """
        模型权限，写了视图权限(has_permission)方法，一般就不需要写这个了。
        返回结果未True则表示允许操作模型对象
        """
        from stuapi.models import Student
        if isinstance(obj, Student):
            # 限制只有小明才能操作Student模型
            identity = request.query_params.get("identity")
            return identity == "vvip"  # 如果身份不是vvip，返回值为False，不能操作
        else:
            # 操作其他模型，直接放行
            return True

```

局部配置自定义权限，视图代码：

```python
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from demo.serializers import StudentModelSerializer, Student
from .permissions import VVIPPermission


class PermissionAPIView(ModelViewSet):
    # authentication_classes = [CustomAuthentication]
    # permission_classes = [AllowAny]  # 针对封闭内部系统，登录页面时谁都可以访问。
    # permission_classes = [IsAdminUser]  # 设置当前视图，只有是管理员可以访问操作。
    # permission_classes = [IsAuthenticatedOrReadOnly]  # 登录用户可以操作，而游客只能查看数据
    # permission_classes = [IsAuthenticated]
    permission_classes = [VVIPPermission]
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

```

settings.py，全局配置，代码：

```python

"""drf的配置"""
# from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
REST_FRAMEWORK = {
    # 配置认证方式的选项[全局配置]
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication', # session认证
        'rest_framework.authentication.BasicAuthentication',   # basic认证[基于账号密码]
    ],
    # 配置权限的选项[全局配置]
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',  # 如果将来的站点时封闭内部系统，则设置IsAuthenticated
        # 'rest_framework.permissions.AllowAny',         # 如果将来的站点时开放外部系统，则设置AllowAny
        'component.permissions.VVIPPermission'
    ]
}
```

访问地址：http://127.0.0.1:8000/component/pess/?identity=vvip

访问地址：http://127.0.0.1:8000/component/pess/



> 认证主要的作用就是识别客户端的访问者的身份，但是不能拦截客户端的访问。
>
> 权限是基于认证来实现的，但是权限可以针对不同身份的用户，进行拦截用户对视图、模型的访问操作。



# 3. 限流Throttling

可以对接口访问的频次进行限制，以减轻服务器压力，或者实现特定的业务。

一般用于付费购买次数,投票等场景使用。

## 基本使用

可以在配置文件中，使用`DEFAULT_THROTTLE_CLASSES` 和 `DEFAULT_THROTTLE_RATES`进行全局配置，

```python
REST_FRAMEWORK = {
    # 限流全局配置
    # 'DEFAULT_THROTTLE_CLASSES':[ # 限流配置类
    #     'rest_framework.throttling.AnonRateThrottle', # 未认证用户[未登录用户]
    #     'rest_framework.throttling.UserRateThrottle', # 已认证用户[已登录用户]
    # ],
    'DEFAULT_THROTTLE_RATES':{ # 频率配置
        'anon': '2/day',  # 针对游客的访问频率进行限制，实际上，drf只是识别首字母，但是为了提高代码的维护性，建议写完整单词
        'user': '5/day', # 针对会员的访问频率进行限制，
    }
}
```

`DEFAULT_THROTTLE_RATES` 可以使用 `second`, `minute`, `hour` 或`day`来指明周期。

也可以在具体视图中通过throttle_classess属性来配置，如

```python
from rest_framework.throttling import UserRateThrottle
class Student2ModelViewSet(ModelViewSet):
    queryset = Student.objects
    serializer_class = StudentModelSerializer
    # 限流局部配置[这里需要配合在全局配置中的DEFAULT_THROTTLE_RATES来设置频率]
    throttle_classes = [UserRateThrottle]
```

## 可选限流类

1） AnonRateThrottle

限制所有匿名未认证用户，使用IP区分用户。【很多公司这样的，IP结合设备信息来判断，当然比IP要靠谱一点点而已】

使用`DEFAULT_THROTTLE_RATES['anon']` 来设置频次

2）UserRateThrottle

限制认证用户，使用User模型的 id主键 来区分。

使用`DEFAULT_THROTTLE_RATES['user']` 来设置频次

3）ScopedRateThrottle

限制用户对于每个视图的访问频次，使用ip或user id。

settings.py，代码：

```python
"""drf配置信息必须全部写在REST_FRAMEWORK配置项中"""
REST_FRAMEWORK = {
    # 配置认证方式的选项【drf的认证是内部循环遍历每一个注册的认证类，一旦认证通过识别到用户身份，则不会继续循环】
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'drfdemo.authentication.CustomAuthentication',          # 自定义认证
        'rest_framework.authentication.SessionAuthentication',  # session认证
        'rest_framework.authentication.BasicAuthentication',    # 基本认证
    ),
    # 权限设置[全局配置，在视图中可以通过permission_classes进行局部配置，局部配置优先级高于全局配置]
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',
        'drfdemo.permissions.IsXiaoMingPermission',
    ),
    # 限流全局配置
    'DEFAULT_THROTTLE_CLASSES':[  # 限流配置类
    #     'rest_framework.throttling.AnonRateThrottle',  # 未认证用户[未登录用户]
    #     'rest_framework.throttling.UserRateThrottle',  # 已认证用户[已登录用户]
        'rest_framework.throttling.ScopedRateThrottle',  # 基于自定义的命名空间来限流
    ],
    'DEFAULT_THROTTLE_RATES': {  # 频率配置
        'anon': '1/s',  # 针对游客的访问频率进行限制，实际上，drf只是识别首字母，但是为了提高代码的维护性，建议写完整单词
        'user': '1/s',  # 针对会员的访问频率进行限制，
        'Hom3': '3/m',  # 针对自定义命名空间，进行限流
    }
}
```

视图代码：

```python
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
class Hom3APIView(APIView):
    # authentication_classes = [CustomAuthentication]  # 调用自定义认证
    # 局部配置限流
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # 配置自定义限流
    throttle_scope = "Hom3"   # 自定义命名空间[少用，因为对于大部分的集体环境下都是公用一个IP地址]
    def get(self,request):
        return Response(f"访问了视图")
```

# 4. 过滤Filtering

对于列表数据可能需要根据字段进行过滤，我们可以通过添加django-fitlter扩展来增强支持。

```shel
pip install django-filter
```

settings.py，代码：

```python
INSTALLED_APPS = [
    # ....
    'django_filters',
]
```

在配置文件中增加过滤器类的全局设置：

```python
"""drf配置信息必须全部写在REST_FRAMEWORK配置项中"""
REST_FRAMEWORK = {
    # ....代码省略。。。
    
    # 过滤查询，全局配置
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
}
```

在视图类中添加类属性filter_fields，指定可以过滤的字段

```python
class Hom4APIView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    filter_fields = ["sex","classmate"]
    # list方法中进行调用->调用了GenericAPIView中声明的filter_queryset方法---> 配置中的过滤器类的filter_queryset---> filter_fields
    
# 单个字段过滤
# http://127.0.0.1:8000/opt/s4/?classmate=301
# http://127.0.0.1:8000/opt/s4/?sex=1
# 多个字段过滤
# http://127.0.0.1:8000/opt/s4/?classmate=502&sex=2
```

路由代码：

```python
from django.urls import path,include
from . import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("s2", views.Hom2APIView, "s2")
router.register("s4", views.Hom4APIView, "s4")

urlpatterns = [
    path("s1/", views.HomeAPIView.as_view()),
    path("", include(router.urls)),  # 等价于  urlpatterns += router.urls
    path("s3/", views.Hom3APIView.as_view()),
    path("s3/", views.Hom3APIView.as_view()),
]
```



局部设置，直接在视图中，指定当前视图类中调用的过滤器类

```bash
# 先注释掉settings中的全局过滤配置
from rest_framework.viewsets import ModelViewSet
from students.models import Student
from students.serializers import StudentModelSerializer
# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
class Hom4APIView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ["sex","classmate"]
    # list方法中进行调用->调用了GenericAPIView中声明的filter_queryset方法---> 配置中的过滤器类的filter_queryset---> filter_fields
```



# 5. 排序Ordering

对于列表数据，REST framework提供了**OrderingFilter**过滤器来帮助我们快速指明数据按照指定字段进行排序。

使用方法：

在类视图中设置filter_backends，使用`rest_framework.filters.OrderingFilter`过滤器，REST framework会在请求的查询字符串参数中检查是否包含了ordering参数，如果包含了ordering参数，则按照ordering参数指明的排序字段对数据集进行排序。

前端可以传递的ordering参数的可选字段值需要在ordering_fields中指明。

配置文件，settings.py，代码：

```python
"""drf配置信息必须全部写在REST_FRAMEWORK配置项中"""
REST_FRAMEWORK = {
    # 。。。代码省略
    # 过滤查询，全局配置
    # 过滤和排序使用了一个公用的配置项，所以2个组件要么一起全局配置，要么就一起局部配置
    'DEFAULT_FILTER_BACKENDS': [
    #     'django_filters.rest_framework.DjangoFilterBackend',  # 过滤
        'rest_framework.filters.OrderingFilter',  # 排序
    ],
}
```

视图代码：

```python
from rest_framework.viewsets import ModelViewSet
from students.models import Student
from students.serializers import StudentModelSerializer
# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
class Hom4APIView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    # 局部过滤
    # filter_backends = [DjangoFilterBackend, OrderingFilter]
    # 过滤字段
    # filter_fields = ["sex","classmate"]
    # 数据排序
    ordering_fields = ['id', 'age']

# 127.0.0.1:8000/books/?ordering=-age
# -id 表示针对id字段进行倒序排序
# id  表示针对id字段进行升序排序
```



上面提到，因为过滤和排序公用了一个配置项，所以排序和过滤要一起使用，则必须整个项目，要么一起全局过滤排序，要么一起局部过滤排序。决不能出现，一个全局，一个局部的这种情况，局部会覆盖全局的配置。

```python
from rest_framework.viewsets import ModelViewSet
from students.models import Student
from students.serializers import StudentModelSerializer
# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
class Hom4APIView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    # 局部过滤
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # 过滤字段
    filter_fields = ["sex","classmate"]
    # list方法中进行调用->调用了GenericAPIView中声明的filter_queryset方法---> 配置中的过滤器类的filter_queryset---> filter_fields

    # 数据排序
    ordering_fields = ['id', 'age']
    
# http://127.0.0.1:8000/opt/demo4/?ordering=id&classmate=301
```

# 6. 分页Pagination

因为django默认提供的分页器主要使用于前后端不分离的业务场景，所以REST framework也提供了分页的支持。

我们可以在配置文件中设置全局的分页方式，如：

```python
REST_FRAMEWORK = {
    # 分页，全局配置
    # 页码分页器，  ?page=页码&page_size=单页数据量
    # 'DEFAULT_PAGINATION_CLASS':  'rest_framework.pagination.PageNumberPagination',
    # 偏移量分页器， ?limit=单页数据量&offset=数据开始下标
    'DEFAULT_PAGINATION_CLASS':  'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10  # 每页数目，如果不设置，则没有进行分配
}
```

```python
# 如果在settings.py配置文件中， 设置了全局分页，那么在drf中凡是调用了ListModelMixin的list()，都会自动分页。如果项目中出现大量需要分页的数据，只有少数部分的不需要分页，则可以在少部分的视图类中关闭分页功能。
# 另外，视图类在使用过分页以后，务必在编写queryset属性时，模型.objects后面调用结果。例如：
# Student.objects.all()
class Hom5APIView(ListAPIView):
	pagination_class = None
```

也可通过自定义Pagination类，来为视图添加不同分页行为。在视图中通过`pagination_clas`属性来指明。

## 可选分页器

1） **PageNumberPagination**

前端访问网址形式：

```http
GET  http://127.0.0.1:8000/students/?page=4
```

可以在子类中定义的属性：

- page_size 每页数目
- page_query_param 前端发送的页数关键字名，默认为"page"
- page_size_query_param 前端发送的每页数目关键字名，默认为None
- max_page_size 前端最多能设置的每页数量

分页器类，`paginations`，代码：

```python
from  rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
# PageNumberPagination，以页码作为分页条件
# page=1&page_size=10      第1页
# page=2&page_size=10      第2页
# ...
# LimitOffsetPagination，以数据库查询的limit和offset数值作为分页条件
# limit=10&offset=0   第1页
# limit=10&offset=10  第2页
# ...

# 自定义分页器，PageNumberPagination
class StudentPageNumberPagination(PageNumberPagination):
    page_query_param = "page" # 查询字符串中代表页码的变量名
    page_size_query_param = "size" # 查询字符串中代表每一页数据的变量名
    page_size = 2 # 每一页的数据量
    max_page_size = 4 # 允许客户端通过查询字符串调整的最大单页数据量
```

视图，`views` ，代码：

```python

from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

# 分页类往往会单独的保存到一个独立的模块，例如：当前子应用目录下创建一个pagination.py保存，使用时导包
class Hom5PageNumberPagination(PageNumberPagination):
    page_size = 10                  # 默认分页的每一页数据量
    max_page_size = 20              # 设置允许客户端通过地址栏参数调整的最大单页数据量
    page_query_param = "pn"         # 地址栏上代表页码的变量名，默认是 page
    page_size_query_param = "size"  # 地址栏上代表单页数据量的变量名，默认是page_size

class Hom5APIView(ModelViewSet):
    # queryset = Student.objects  # 这句话在没有进行分页时不会报错，调用了分页则会报错！
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    # 局部分页
    # pagination_class = None  # 关闭分页功能
    # 局部分页往往采用自定义分页类，进行分页数据量的配置
    pagination_class = Hom5PageNumberPagination

    def list(self, request, *args, **kwargs):
        # 获取django的配置项
        from django.conf import settings

        # 获取rest_framework的配置项
        # from rest_framework.settings import api_settings
        # print(api_settings.DEFAULT_PAGINATION_CLASS)
        return super().list(request, *args, **kwargs)
```



2）**LimitOffsetPagination**

前端访问网址形式：

```http
GET http://127.0.0.1/four/students/?limit=100&offset=100
```

可以在子类中定义的属性：

- default_limit 默认限制，默认值与`PAGE_SIZE`设置一直
- limit_query_param limit参数名，默认'limit'
- offset_query_param offset参数名，默认'offset'
- max_limit 最大limit限制，默认None

分页类，代码：

```python
from  rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
# PageNumberPagination，以页码作为分页条件
# page=1&size=10      第1页
# page=2&size=10      第2页
# LimitOffsetPagination，以数据库查询的limit和offset数值作为分页条件
# limit=10&offset=0   第1页
# limit=10&offset=10  第2页

# LimitOffsetPagination
class StudentLimitOffsetPagination(LimitOffsetPagination):
    limit_query_param = "limit" # 查询字符串中代表每一页数据的变量名
    offset_query_param = "offset" # 查询字符串中代表页码的变量名
    default_limit = 2 # 每一页的数据量
    max_limit = 4 # 允许客户端通过查询字符串调整的最大单页数据量
```

视图，`views`，代码：

```python
from .paginations import StudentPageNumberPagination,StudentLimitOffsetPagination
class Student3ModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    # 取消当前视图类的分页效果
    # pagination_class = None
    # 局部分页
    pagination_class = StudentLimitOffsetPagination
```

# 7. 异常处理 Exceptions

REST framework本身在APIView提供了异常处理，但是仅针对drf内部现有的接口开发相关的异常进行格式处理，但是开发中我们还会使用到各种的数据或者进行各种网络请求，这些都有可能导致出现异常，这些异常在drf中是没有进行处理的，所以就会冒泡给django框架了，django框架会进行组织错误信息，作为html页面返回给客户端，所在在前后端分离项目中，可能js无法理解或者无法接收到这种数据，甚至导致js出现错误的情况。因此为了避免出现这种情况，我们可以自定义一个属于自己的异常处理函数，对于drf无法处理的异常，我们自己编写异常处理的代码逻辑。

针对于现有的drf的异常处理进行额外添加属于开发者自己的逻辑代码，一般我们编写的异常处理函数，会写一个公共的目录下或者主应用目录下。这里主应用下直接创建一个excepitions.py，代码：

```python
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
# 针对mysql、mongoDB、redis、第三方数据接口
def custom_exception_handler(exc, context):
    """
    自定义异常函数
    exc: 异常实例对象，发生异常时实例化出来的
    context: 字典，异常发生时python解释器收集的执行上下文信息。
             所谓的执行上下文就是python解释器在执行代码时保存在内存中的变量、函数、类、对象、模块等一系列的信息组成的环境信息。
    """
    response = exception_handler(exc, context)

    if response is None:
        """当前异常，drf无法处理"""
        if isinstance(exc, ZeroDivisionError):
            response = Response({"detail":"数学老师还有30秒达到战场，0不能作为除数！"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return response
```

在配置文件中声明自定义的异常处理，`settings`，代码：

```python
REST_FRAMEWORK = {
    # 异常配置
    'EXCEPTION_HANDLER': 'drfdemo.exceptions.custom_exception_handler'
}
```

如果未声明自定义异常的话，drf会采用默认的方式，使用自己封装的异常处理函数，rest_frame/settings.py

```python
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler'
}
```

例如：

补充上处理关于数据库的异常，这里使用其他异常来举例：

`主应用.exceptions`，代码：

```python
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.db import DatabaseError
# 针对mysql、mongoDB、redis、第三方数据接口
def custom_exception_handler(exc, context):
    """
    自定义异常函数
    exc: 异常实例对象，发生异常时实例化出来的
    context: 字典，异常发生时python解释器收集的执行上下文信息。
             所谓的执行上下文就是python解释器在执行代码时保存在内存中的变量、函数、类、对象、模块等一系列的信息组成的环境信息。
    """
    response = exception_handler(exc, context)
    print(f"context={context}")
    if response is None:
        """当前异常，drf无法处理"""
        view = context["view"] # 获取异常发生时的视图类
        request = context["request"] # 获取异常发生时的客户端请求对象
        if isinstance(exc, ZeroDivisionError):
            response = Response({"detail":"数学老师还有30秒达到战场，0不能作为除数！"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if isinstance(exc, TypeError):
            print('[%s]: %s' % (view, exc))
            response = Response({'detail': '服务器内部错误'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response
```

视图中，故意报错：

```python
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

class Hom5PageNumberPagination(PageNumberPagination):
    page_size = 10                  # 默认分页的每一页数据量
    max_page_size = 20              # 设置允许客户端通过地址栏参数调整的最大单页数据量
    page_query_param = "pn"         # 地址栏上代表页码的变量名，默认是 page
    page_size_query_param = "size"  # 地址栏上代表单页数据量的变量名，默认是page_size

class Hom5APIView(ModelViewSet):
    queryset = Student.objects  # 这句话在没有进行分页时不会报错，调用了分页则会报错，所以会进入异常处理！
    # queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    # 局部分页
    # pagination_class = None  # 关闭分页功能
    # 局部分页往往采用自定义分页类，进行分页数据量的配置
    pagination_class = Hom5PageNumberPagination

    def list(self, request, *args, **kwargs):
        # 获取django的配置项
        from django.conf import settings

        # 获取rest_framework的配置项
        # from rest_framework.settings import api_settings
        # print(api_settings.DEFAULT_PAGINATION_CLASS)
        return super().list(request, *args, **kwargs)
```



## REST framework定义的异常

- APIException 所有异常的父类
- ParseError 解析错误
- AuthenticationFailed 认证失败
- NotAuthenticated 尚未认证
- PermissionDenied 权限拒绝
- NotFound 404 未找到
- MethodNotAllowed 请求方式不支持
- NotAcceptable 要获取的数据格式不支持
- Throttled 超过限流次数
- ValidationError 校验失败

也就是说，很多的没有在上面列出来的异常，就需要我们在自定义异常中自己处理了。

# 8. 自动生成接口文档

REST framework可以自动帮助我们生成接口文档。

接口文档以网页的方式呈现。

自动接口文档能生成的是继承自`APIView`及其子类的视图。

## coreapi

### 安装依赖

REST framewrok生成接口文档需要`coreapi`库的支持。

```python
pip install coreapi
```

### 设置接口文档访问路径

在总路由中添加接口文档路径。

文档路由对应的视图配置为`rest_framework.documentation.include_docs_urls`，

参数`title`为接口文档网站的标题。总路由urls.py，代码：

```python
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    ...
    path('docs/', include_docs_urls(title='站点页面标题'))
]
```

在settings.py中配置接口文档。

```python
INSTALLED_APPS = [
 
    'coreapi',


]
REST_FRAMEWORK = {
    # 。。。 其他选项
    # 接口文档
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.AutoSchema',
}
```



8.3. 文档描述说明的定义位置

1） 单一方法的视图，可直接使用类视图的文档字符串，如

```python
class BookListView(generics.ListAPIView):
    """
    返回所有图书信息
    """
```

2）包含多个方法的视图，在类视图的文档字符串中，分开方法定义，如

```python
class BookListCreateView(generics.ListCreateAPIView):
    """
    get:
    返回所有图书信息.

    post:
    新建图书.
    """
```

3）对于视图集ViewSet，仍在类视图的文档字符串中封开定义，但是应使用action名称区分，如

```python
class BookInfoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    """
    list:
    返回图书列表数据

    retrieve:
    返回图书详情数据

    latest:
    返回最新的图书数据

    read:
    修改图书的阅读量
    """
```

### 访问接口文档网页

浏览器访问 127.0.0.1:8000/docs/，即可看到自动生成的接口文档。

![æ¥å£ææ¡£ç½é¡µ](assets/接口文档页面.png)

两点说明：

1） 视图集ViewSet中的retrieve名称，在接口文档网站中叫做read

2）参数的Description需要在模型类或序列化器类的字段中以help_text选项定义，如：

```python
class Student(models.Model):
    ...
    age = models.IntegerField(default=0, verbose_name='年龄', help_text='年龄')
    ...
```

或

```python
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        extra_kwargs = {
            'age': {
                'required': True,
                'help_text': '年龄'
            }
        }
```



## yasg

安装

```bash
pip install drf-yasg
```

配置，settings.py，代码：

```python
INSTALLED_APPS = [

    'drf_yasg',  # 接口文档drf_yasg

]
```

总路由，

```python
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

# yasg的视图配置类，用于生成a'pi
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="drf接口文档",  # 必传
        default_version='v1.0,0',  # 必传
        description="描述信息",
        terms_of_service='',
        contact=openapi.Contact(email="649641514@qq.com"),
        license=openapi.License(name="协议版本")
    ),
    public=True,
    # permission_classes=(rest_framework.permissions.AllowAny)  # 权限类
)


urlpatterns = [
    # 文档路由
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger'),
    path('docs/', include_docs_urls(title='站点页面标题')),
    path('admin/', admin.site.urls),
    path('students/', include("students.urls")),
    path('sers/', include("sers.urls")),
    path('school/', include("school.urls")),
    path("req/", include("req.urls")),
    path("demo/", include("demo.urls")),
    path("opt/", include("opt.urls")),
]

```

http://127.0.0.1:8000/doc/，访问效果：

![image-20210901182801990](assets/image-20210901182801990.png)

![image-20210901182739563](assets/image-20210901182739563.png)

