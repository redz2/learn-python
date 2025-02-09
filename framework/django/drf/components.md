# 组件
0. 如何使用组件？组件何时执行？
    * django中间件 -> APIView ->as_view() -> dispatch() -> initial() -> 执行认证、权限、限流等操作 -> 调用get()等方法
```py
class StudentViewSet(viewsets.ModelViewSet):
    # 为什么局部比全局优先？
    # 局部配置优先级高于全局配置，局部配置可以覆盖全局配置
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

1. 认证类: 识别用户身份
    * 这些其实都可以看做是中间件，只是drf单独抽出来了
    * 登录需要验证账号密码，认证是识别用户信息
```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
       'rest_framework.authentication.TokenAuthentication',
       'rest_framework.authentication.SessionAuthentication',
       'myapp.authentication.CustomAuthentication',
    ],
}
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import NotAuthenticated, Unauthorized, PermissionDenied
# 自定义认证逻辑
class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        """
        1. 如果验证成功，返回用户信息
        2. 如果验证失败，应该抛出异常
        3. 一旦验证成功，drf会将user存储到request中
        """
        user = request.query_params.get("user")
        password = request.query_params.get("password")
        if user:
            try:
                # 如何知道使用哪个用户模型？
                # settings.py中配置: AUTH_USER_MODEL = 'app.User'
                user = get_user_model().objects.get(username=user, password=password)
                return (user, None) # 返回元组，第一个元素是用户对象，第二个元素是None
            except User.DoesNotExist:
                raise NotAuthenticated("认证失败", 401)
        else:
            return None
```

2. 权限类: 基于用户判断用户是否有权限访问某个资源
```python
# settings.py: 全局配置
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
       'rest_framework.permissions.IsAuthenticated',
       'myapp.permissions.CustomPermission',
    ],
}

# 如何字定义权限类？
class CustomPermission(BasePermission):
    
    def has_permission(self, request, view):
        # 判断视图函数是否有权限访问
        # 基于用户来判断是否可以访问视图函数
        # 如果用户不是该条记录的所有者，只有只读权限，通过方法来判断
        if request.method in SAFE_METHODS:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # 判断用户是否有权限访问某个对象
        if request.method in SAFE_METHODS:
            return True
        else:
            return False

# 如何使用权限类？
class PermissionViewSets(ModelViewSet):
    # 按照列表中的权限类依次判断，如果有权限，则执行视图函数
    # 局部配置
    permission_classes = [IsAdminUser, CustomPermission]
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
```

3. 限流类
```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
       'rest_framework.throttling.AnonRateThrottle', # 未认证用户，使用IP区分
       'rest_framework.throttling.UserRateThrottle', # 已认证用户，使用用户ID区分
       'rest_framework.throttling.ScopedRateThrottle', # 按视图函数区分
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10/minute',
        'user': '100/minute',
        'scope': '20/minute',
    },
}

# 如何使用限流类？
class ThrottleViewSets(ModelViewSet):
    # 按照列表中的限流类依次判断，如果有限流，则执行视图函数
    # 局部配置
    throttle_classes = [AnonRateThrottle, UserRateThrottle, ScopedRateThrottle]
    queryset = Throttle.objects.all()
    serializer_class = ThrottleSerializer
```

4. 错误处理类
    * 大概是在dispatch()中统一处理异常，返回统一的错误响应
```py
from rest_framework.exceptions import APIException
class CustomException(APIException):
    ...

# settings.py
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'myapp.exceptions.custom_exception_handler',
}

# myapp/exceptions.py
from rest_framework.views import exception_handler
from myapp.exceptions import CustomException

"""
drf能处理的异常
1. 自定义的APIException
2. ParseError
3. AuthenticationFailed
4. NotAuthenticated
5. PermissionDenied
6. NotFound
7. MethodNotAllowed
8. NotAcceptable
9. Throttled
10. ValidationError
11. UnsupportedMediaType
"""
def custom_exception_handler(exc, context):
    """
    exc: 异常对象
    context: 异常上下文
    """
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if response is not None:
        if isinstance(exc, Http404):
            response = Response({'detail': '对不起，您访问的资源不存在'}, status=status.HTTP_404_NOT_FOUND)
        if isinstance(exc, PermissionDenied):
            response = Response({'detail': '您没有权限访问该资源'}, status=status.HTTP_403_FORBIDDEN)
        if isinstance(exc, CustomException):
            response = Response({'detail': '自定义异常'}, status=status.HTTP_400_BAD_REQUEST)
    return response
```

5. 分页类
```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'myapp.pagination.CustomPagination',
    'PAGE_SIZE': 10, # 默认每页显示10条数据
}

# GET /api/pagination/?page=1&page_size=20
class CustomPagination(PageNumberPagination):
    page_size = 20 # 自定义每页显示20条数据
    page_size_query_param = 'page_size' # 自定义每页显示数量参数名
    page_query_param = 'page' # 自定义页码参数名
    max_page_size = 100 # 自定义最大每页显示数量

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10 # 默认每页显示10条数据
    limit_query_param = 'limit' # 自定义每页显示数量参数名
    offset_query_param = 'offset' # 自定义偏移量参数名
    max_limit = 100 # 自定义最大每页显示数量

# 如何使用分页类？
class PaginationViewSets(ModelViewSet):
    # 局部配置
    pagination_class = CustomPagination
    queryset = Pagination.objects.all()
    serializer_class = PaginationSerializer
```

6. 过滤类
```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
       'rest_framework.filters.SearchFilter', # 全局搜索
       'myapp.filters.CustomFilter', # 自定义过滤
    ],    
}

# 如何使用过滤类？
class FilterViewSets(ModelViewSet):
    # 局部配置
    filter_backends = [SearchFilter, CustomFilter]
    search_fields = ['name', 'age'] # 全局搜索
    queryset = Filter.objects.all()
    serializer_class = FilterSerializer

class CustomFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        # 自定义过滤逻辑
        # 例如：根据用户ID过滤
        user_id = request.query_params.get('user_id')
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset
```

