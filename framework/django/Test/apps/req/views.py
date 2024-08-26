# # Create your views here.

import django.urls
from django.views import View
from django.http.response import JsonResponse

# View(django) -> APIView -> GenericAPIView -> GenericAPIView+Mixins -> 视图子类 
# -> ViewSet -> GenericViewSet -> GenericViewSet+Mixins -> ModelViewSet or ReadOnlyModelViewSet

# 如果没有重复的方法，且不需要写在一个类中，不需要使用ViewSet
# 如果需要自定义方法内容，不需要使用Mixins
# 序列化器也可以只做字段验证，不一定非要和模型类一起用
# drf可以处理80%增删改查的场景

########################################################################################################################
# 
# 1. View
# 
########################################################################################################################

"""django的原生视图类"""
class StudentsView(View):
    
    # WSGIRequest
    def get(self, request):
        # request中有什么？
        # 1. 浏览器中的数据
        # 2. django添加的数据
        return JsonResponse({"message": "ok"})

import rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

########################################################################################################################
# 
# 2. APIView
# 
########################################################################################################################

# 继承自Django的View，是drf其他视图类的基类

"""drf提供的APIView"""
# 什么是内容协商？
# DRF的request类 -> parser(http请求解析类) -> 识别客户端请求头中的Content-Type来完成数据转换成 -> 类字典(QueryDict，字典的子类)
# DRF的response类 -> renderer(http响应渲染类) -> 识别客户端请求头的"Accept"来提取客户端期望的返回数据格式(如果未设置，参考Content-Type) -> 转换成客户端的期望格式数据

# 和View的区别: 使用drf提供的request和response，使用序列化器

from apps.drf.models import Student
from apps.drf.serializers import StudentSerializer
from .models import StudentSerializer,Student

# 为什么要分成两个类，因为方法的参数不同

class StudentsAPIView(APIView):
    
    """APIView"""
    
    # APIView类中的request对象是drf单独声明的，包含了django中的request对象
    # request._request -> WSGIRequest
    
    def get(self, request):
        # GET http://127.0.0.1:8000/req/stuapi/?name=zhouyi
        # request.GET -> <QueryDict: {'name': ['zhouyi']}>
        # request.query_params # 查询字符串，本质上就是request.GET（不区分请求方法，View中有歧义，现在名称更加准确）
        # request.path_info -> /req/stuapi/
        # request.method -> GET
        # request.headers -> {'Content-Length': '', 'Content-Type': 'text/plain', 'Host': '127.0.0.1:8000', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:128.0) Gecko/20100101 Firefox/128.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8', 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Connection': 'keep-alive', 'Cookie': 'csrftoken=hLD7jM1aa6hlIWSHlzBYXBheq3qC7s7P', 'Upgrade-Insecure-Requests': '1', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'none', 'Sec-Fetch-User': '?1', 'Priority': 'u=0, i'}
        # request.headers -> request.COOKIES(django加工数据) -> {'csrftoken': 'hLD7jM1aa6hlIWSHlzBYXBheq3qC7s7P'}
        
        # 如果需要过滤或者需要分页，是不是在这里进行操作？
        instance_list = Student.objects.all()
        serializers = StudentSerializer(instance=instance_list, many=True)
        return Response(serializers.data)
    
    def post(self, request):
        # 简单点说，request.data是drf加工过的数据
        # request.body（原始数据） ---> request.data（Parser解析之后的请求体数据，类似于django中的request.POST和request.FILE）
        
        # 只有请求头和数据格式正确，django才会把body中的数据存入POST或FILE
        # request.POST content-type:application/x-www-form-urlencoded
        # request.FILE multipart/form-data
            
        # 如果客户端提交的是json数据，则request.data得到的数据是一个字典 -> {'name': 'xiaoming', 'age': 18, 'description': 'xxxxx'}
        # 如果客户端提交的是表单数据，则request.data得到的QueryDict类字典 -> <QueryDict: {'name': ['xiaohong'], 'age': ['20']}>
        # request.data -> 字典
        
        # 构造方式
        # Response(data, status=None, template_name=None, headers=None, content_type=None)
        # data: python基本数据类型
        # status: 状态码
        # headers: 响应头
        # content_type: 一般不用设置
        from rest_framework import status
        
        # 好处: 浏览器会有一个漂亮的界面
        serializers = StudentSerializer(data=request.data)
        # 如果验证失败，‌DRF会抛出serializers.ValidationError异常，这个异常会被drf捕获，‌并作为HTTP 400 Bad Request响应发送回前端
        serializers.is_valid(raise_exception=True)
        
        # 验证失败的话，下面的代码都不会执行了
        
        # You cannot call `.save()` after accessing `serializer.data`
        # 数据的验证，修改都应该在序列化器中，防止数据被修改
        serializers.save()
        
        # 添加学生信息
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    
    
    
    
# APIView重新声明as_view()方法，在dispatch()进行路由分发时，会对客户端进行身份认证、权限检查、流量控制
# 新增了3个属性: authentication_classes、permission_classes、throttle_classes
# 和常规的类视图View一样，也需要实现get()，post()方法
from rest_framework.exceptions import APIException
class NotFound(APIException):
    pass

class StudentsInfoAPIView(APIView):
    
    def get(self, request, pk):
        """获取一个学生信息"""
        # 自己如何添加错误处理
        from django.http import Http404
        try:
            instance = Student.objects.get(pk=pk)
        except:
            # raise Http404("drf会捕获异常，返回给前端")
            raise NotFound("我自己抛出的错误")
            # *** drf可以捕获哪些错误？***
            # 1. Http404
            # 2. 权限拒绝错误，包括django的PermissionDenied
            # 3. 自定义的APIException错误
        serializers = StudentSerializer(instance=instance)
        return Response(serializers.data)
    
    def put(self, request, pk):
        """更新一个学生信息"""
        instance = Student.objects.get(pk=pk)
        serializers = StudentSerializer(instance=instance, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        """删除一个学生信息"""
        instance = Student.objects.filter(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
       
########################################################################################################################     
#
# 3. GenericAPIView: 通用视图类
#
########################################################################################################################

# 为啥要叫通用视图类呢？为了让代码更加通用，二八定律，大部分都是增删改查
# 以下的方式，其实本质上都是GenericAPIView的简写

# 需要定义 queryset 和 serializer_class
# 
# 增加操作序列化器和数据库查询的方法，通过视图混入类（Mixin类），给自己写的视图类添加方法

# serializer_class 视图使用的序列化器
# get_serializer_class() 默认返回serializer_class，可以重写
# get_serializer()

# queryset: 指明数据查询的结果集
# get_queryset(): 默认返回queryset，可以重写，根据情况返回不同的序列化器
# get_object(): 返回详情视图一个模型对象的数据 -> check_object_permissions

# GenericAPIView中基本上不会查询数据库的语句了，那怎么实现特殊的查询需求呢？
# pagination_class: 分页
# filter_backends: 客户端传递参数，过滤数据

from rest_framework.generics import GenericAPIView

class StudentsGenericAPIView(GenericAPIView):
    
    """
    GenericAPIView: APIView中增删改查的代码可以复用
    
    提供了两个类属性: queryset、serializer_class
    提供了几个方法: get_queryset()、get_object()、get_serializer()
    """
    
    # 这两个属性默认设置为None
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request):
        
        # 不建议直接使用query_set和serializer_class
        # instance_list = self.queryset
        instance_list = self.get_queryset()
        
        # serializers = self.serializer_class(instance_list, many=True)
        serializer = self.get_serializer(instance_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class StudentsInfoGenericAPIView(GenericAPIView):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    # lookup_field = "id" # 不建议修改
    
    def get(self, request, pk):
        # instance = self.get_queryset().get(pk=pk)
        # get_object() -> get_queryset() -> 权限检查 -> queryset -> 返回instance（默认是pk，如何修改成其他值？lookup_field）       
        instance = self.get_object() # 如果未查询到对象，抛出Http404，
        
        # get_serializer() -> get_serializer_class() -> 属性中包含serializer_class或重写get_serializer_class()
        serializer = self.get_serializer(instance=instance) # get_serializer()获取到serializer_class后会使用传入的参数，进行实例化，返回一个序列化器对象
        return Response(serializer.data)
    
    def put(self, request, pk):
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def delete(self, request, pk):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 
########################################################################################################################
#
# 4. GenericAPIView: Mixins
# 
########################################################################################################################

# drf提供了Mixins类，如果我们编写的视图属于这5类，可以添加相应的混入类（Mixins类提前帮我们写好了视图函数）
# Mixins类包含了增删改查的方法，不过方法名称不是get、post、put、delete

from rest_framework import mixins

class StudentListAPIView(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request):
        # ListModelMixin提供list方法
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class StudentRetrieveAPIView(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request, pk):
        """查询一个学生信息"""
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        """更新一个学生信息"""
        return self.update(request, pk)
    
    def delete(self, request, pk):
        """删除一个学生信息"""
        return self.destroy(request, pk)

########################################################################################################################
#
# 5. 视图子类 = 通用视图类 + Mixins
#
########################################################################################################################

# 只需要继承视图子类，就实现了get，post，put，delete方法
# 
# 怎么去修改get方法逻辑？
# 

from rest_framework.generics import ListCreateAPIView,ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
class StuAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class StuInfoAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    
    
    
    
    

########################################################################################################################
########################################################################################################################
########################################################################################################################



    
########################################################################################################################
#
# 6. ViewSet: 视图集
# 
########################################################################################################################

# 为什么上面要写两个类？
# 上面使用的视图类都是基于APIView实现的，而APIView基于View，而View中dispatch()限制了当前视图必须以请求作为方法名
# 其中有个问题，必然有2个get方法，一个类中不能存在同名的方法
# 另外，只有删除、更新、获取时需要地址栏需要传id，添加一条或获取多条数据时，不需要传入id，所以路由要我们分开写

# ViewSet解决了什么问题？可以在一个类中写所有接口了
# 关键点：重写了as_view()，不再限制方法名为get/post/put/delete，允许开发者自己定义方法名，经过路由将请求动作和视图方法名进行绑定映射调用


from rest_framework.viewsets import ViewSet

# ViewSet 是 APIView 的子类，是其他视图集的父类
class StudentViewSet(ViewSet):
    
    """获取多条数据"""
    def list(self, request):
        # 写法和APIView一样
        instance_list = Student.objects.all()
        serializers = StudentSerializer(instance=instance_list, many=True)
        return Response(serializers.data)

    def retrieve(self, request, pk):
        from django.http import Http404
        try:
            instance = Student.objects.get(pk=pk)
        except:
            raise NotFound("有错误拉")
        serializers = StudentSerializer(instance=instance)
        return Response(serializers.data)
    
    
########################################################################################################################
#
# 6. GenericViewSet: 通用视图集类
# 
########################################################################################################################

from rest_framework.viewsets import GenericViewSet

# GenericViewSet默认是不提供任何方法的

class StudentGenericViewSet(GenericViewSet):
    
    """GenericViewSet: 数据独立出去，方法自己实现"""
    # 和GenericAPIView差不多，提取公共部分
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def list(self, request):
        instance_list = self.get_queryset()
        serializer = self.get_serializer(instance_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


########################################################################################################################
#
# 6. GenericViewSet: 通用视图集类 + Mixins
# 
########################################################################################################################from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
class StuGenMixViewSet(GenericViewSet,ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    
    """GenericViewSet + Mixins: 数据独立出去，方法由Mixins来提供"""
    # 1. GenericViewSet和GenericAPIView差不多，会提取公共部分
    # 2. 通过Mixins提供方法
    # 3. 因为ViewSet可以将HTTP方法绑定到函数，不需要手动去实现get、post等方法了
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
######################################################################################################################
#
# 6. ModelViewSet: 模型视图集
# 
# ReadOnlyModelViewSet: 只读视图集
# 
########################################################################################################################from rest_framework.viewsets import GenericViewSet

from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
class StuMVS(ModelViewSet):
    
    """ModelViewSet: 提供所有方法"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    # action装饰器: 可以让开发者在视图中添加路由信息，这个和flask就很像了
    from rest_framework.decorators import action
    # url_path 默认是方法名
    
    @action(methods=["GET"], detail=False)
    # detail是否需要传入pk值
    def login(self, request):
        return Response("登录成功")
    
# Model + ModelSerializer + ModelViewSet
# 1. 使用哪个序列化器
# 2. 使用哪个模型类
# 3. 需要使用哪些方法？
class StuRMVS(ReadOnlyModelViewSet):
    
    """ReadOnlyModelViewSet: 只提供读方法"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    


        