# APIView
0. 视图函数
    * View -> APIView -> GenericAPIView(+Mixins) -> ListAPIView(视图子类)
        * 为什么必须写两个类？因为GET方法重复
        * 如果没有重复的方法，不需要viewset
        * 如果需要自定义方法，不需要mixins
        * 序列化器可以只做序列化，不一定要和模型类绑定
    * ViewSet -> GenericViewSet(+Mixins) -> ModelViewSet(ReadOnlyModelViewSet)
        * 功能增强就是不断重写as_view()方法  
        * 脑子里需要清楚，每个类就是实现5个方法，然后组合起来

1. django原生视图: View
```python
path('studentsview/', views.StudentsView.as_view()), # django原生View

class StudentsView(View):
    def get(self, request):
        # request中有啥？
        # 浏览器信息
        # django添加的信息
        return JsonResponse({"message": "ok"})
```

2. APIView: 继承自View
    * APIView重写了as_view()方法，在dispatch()进行路由分发前，添加了身份认证、权限控制、流量控制
        * authentication_classes: 身份认证
        * permission_classes: 权限控制
        * throttle_classes: 流量控制
```python
path('studentsapiview/', views.StudentsAPIView.as_view()) # APIView
re_path(r'^studentsapiview/(?P<pk>\d+)/', views.StudentsInfoAPIView.as_view()),  # APIView

# settings.py
REST_FRAMEWORK = {
    # 解析器
    # 使用content-type自动解析参数到request.data中: 
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ],
    # 响应渲染器
    # 根据请求头中的accept字段返回不同的响应
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer", # 用于API接口
        "rest_framework.renderers.BrowsableAPIRenderer", # 用于浏览器调试
    ],
}

# 内容协商: request和response进行了封装(request._request -> WSGIRequest)
# 根据客户端请求头中的消息来封装request和response
# DRF的request类 -> parser(http请求解析类) -> 识别客户端请求头中的Content-Type来完成数据转换成 -> 类字典(QueryDict，字典的子类)
# DRF的response类 -> renderer(http响应渲染类) -> 识别客户端请求头的"Accept"来提取客户端期望的返回数据格式(如果未设置，参考Content-Type) -> 转换成客户端的期望格式数据（drf有漂亮的界面）

class StudentsView(APIView):
    def get(self, request):
        # GET http://127.0.0.1:8000/studentsapiview/?name=zhouyi
        # request.GET -> QueryDict {'name': ['zhouyi']}
        # request.query_params # 查询字符串参数
        # request.path_info # 请求路径
        # request.method # 请求方法
        # request.headers # 请求头

        all_students = models.Student.objects.all()
        # 编写过滤和分页的代码
        # limit = request.query_params.get('limit', 10)
        # offset = request.query_params.get('offset', 0)
        # all_students = all_students[offset:offset+limit]    
        serializer = serializers.StudentSerializer(all_students, many=True)
        return Response(serializer.data)

    def post(self, request):
        # request.body # 请求体，原始数据
        # request.data # 解析后的请求数据
        # 如果提交的是json数据，request.data就是字典
        # 如果提交的是表单数据，request.data就是QueryDict
        serializer = serializers.StudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # You cannot call `.save()` after accessing `serializer.data` -- 防止数据被修改
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 class StudentsInfoAPIView(APIView):
    def get(self, request, pk):
        from django.http import Http404
        try:
            # 以下就是get_object()函数实现
            student = models.Student.objects.get(pk=pk)
        except models.Student.DoesNotExist:
            raise Http404("Student does not exist")
        serializer = serializers.StudentSerializer(student)
        return Response(serializer.data)
```

3. GenericAPIView: 通用视图类
    * 为啥叫通用视图类: 根据二八原则，80%都是增删改查
    * 关键点:将model和serializer提取出来(并未提供增删改查方法)
    * 这里是第一版GenericAPIView，后面包括mixins，ListAPIView其实都是基于GenericAPIView的简写
```py
path('generic/', views.StudentsGenericAPIView.as_view()),  # GenericAPIView
    re_path(r'^generic/(?P<pk>\d+)/', views.StudentsInfoGenericAPIView.as_view()),  # GenericAPIView

class StudentsGenericAPIView(GenericAPIView):
    """
    让APIView中增删改查代码复用

    提供了两个类属性: queryset和serializer_class
    提供了几个方法: get_queryset()、get_object()、get_serializer()
    """
    # lookup_field = 'pk' # 默认的主键字段
    queryset = models.Student.objects.all() # 默认为None
    serializer_class = serializers.StudentSerializer # 默认为None

    # get_queryset()方法可以重写，默认返回self.queryset
    # get_serializer_class()方法可以重写，默认返回self.serializer_class
    # 不建议直接使用queryset和serializer_class属性
    def get(self, request):
        all_students = self.get_queryset() # 获取所有学生
        serializer = self.get_serializer(all_students, many=True) # 获取序列化器，并传入对象列表
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentsInfoGenericAPIView(GenericAPIView):

    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

    def get(self, request, pk):
        instance = self.get_object() # 获取一个对象，如果没有pk，会抛出404
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def put(self, request, pk):
        instance = self.get_object() # 获取一个对象
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

4. GenericAPIView + Mixins
    * 如果都是增删改查，drf 提供了mixins，可以直接使用
    * 关键点: 提供了增删改查方法实现(方法名称不是get等)
```py
class StudentsListAPIView(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

# Mixins实现了create，retrieve，update，destroy, list方法
class StudentsInfoAPIView(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)

    def delete(self, request, pk):
        return self.destroy(request, pk=pk)
```

5. 视图子类: ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
    * 直接实现了增删改查方法，不需要再写get、post等方法
    * ListAPIView = GenericAPIView + mixins.ListModelMixin
```py
class StudentsAPIView(ListAPIView, CreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

class StudentsInfoAPIView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
```

***

6. 视图集: ViewSet
    * 为什么上面一直要写两个类？因为必然有两个get方法，同一个类中不能存在同名的方法
    * 关键点: 通过方法映射，在一个类中编写所有请求
        * 取消了方法名的限制
```py
# 目前路由还是要写两个
path('viewset/', views.StudentsViewSet.as_view({'get': 'list', 'post': 'create'}))
re_path(r'^viewset/(?P<pk>\d+)/', views.StudentsInfoViewSet.as_view(
            {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))

class StudentsViewSet(ViewSet):
    """
    ViewSet最主要的功能就是让请求方法和视图函数绑定在一起(改写as_view方法)，不需要再写get、post等方法
    下面的实现其实就是mixins的demo
    """
    def list(self, request):
        all_students = models.Student.objects.all()
        serializer = serializers.StudentSerializer(all_students, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = serializers.StudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        instance = models.Student.objects.get(pk=pk)
        serializer = serializers.StudentSerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk):
        instance = models.Student.objects.get(pk=pk)
        serializer = serializers.StudentSerializer(instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        instance = models.Student.objects.get(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

7. 通用视图集: GenericViewSet + Mixins
    * queryset和serializer_class属性: 将model和serializer提取出来
    * mixins: 实现增删改查方法(其实就是上面的五个方法)
```py
# class StudentsGenericViewSet(GenericViewSet):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer

#     def list(self, request):
#         all_students = self.get_queryset()
#         serializer = self.get_serializer(all_students, many=True)
#         return Response(serializer.data)

class StudentsGenericViewSet(GenericViewSet, 
                            mixins.ListModelMixin, 
                            mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
```

8. 模型视图集: ModelViewSet
    * 如何重写某个方法？
```py
# 如何更简单的添加路由？路由集: 自动生成路由
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
# 视图集方法一定要标准写法，不能用get、post等，只能用list、create等
router.register('students', views.StudentsModelViewSet, basename='students') # 自动生成路由
urlpatterns += router.urls

class StudentsModelViewSet(ModelViewSet):
    # ModelViewSet其实就是GenericViewSet + Mixins
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

    # 如何自定义视图函数？
    # @action(methods=['get'], detail=False)
    # # detail=False 代表不用传入pk，直接获取全部学生
    # def top(self, request):
    #     top_students = models.Student.objects.order_by('-score')[:10]
    #     serializer = serializers.StudentSerializer(top_students, many=True)
    #     return Response(serializer.data)

class ReadOnlyStudentsModelViewSet(ModelViewSet):
    # 提供只读方法
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
``` 

