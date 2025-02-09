from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# Create your views here.
from .authentication import CustomAuthentication

class StudentsAPIView(APIView):
    
    # throttle_classes = "Students"

    # 为什么局部比全局优先？
    # authentication_classes = [SessionAuthentication] -> 获取当前登录用户 -> request.user（request.auth用来干啥的？）
    # 使用Session，django使用中间件获取了User，drf不需要重复获取
    # 如果使用Token，drf需要在认证过程中自己写逻辑，获取User
    authentication_classes = [CustomAuthentication, SessionAuthentication]
    
    # drf框架中: APIView -> as_view() -> dispatch() -> initial() -> 执行认证、鉴权、限流
    # 1. self.perform_authentication(request) -> 认证 
    # 2. self.check_permissions(request) -> 鉴权
    # 3. self.check_throttles(request) -> 限流

    def get(self, request):
        # request.user 怎么来的？django的session和authentication中间件从cookie中拿的
        # if request.user is not None:
            # drf 的前端只是拿了这个变量的值展示而已
            # request.user.username = "zhouyi"
        # print(request.user)
        raise Exception("hahahah")
        return Response({"message": "ok"})
    
from .models import Student,StudentSerializer
from .permission import VVIPPermission
from rest_framework.permissions import IsAdminUser,IsAuthenticatedOrReadOnly
from .pagination import CustomPagination
class PermissionViewSet(ModelViewSet):
    
    # permission_classes = [IsAdminUser] # APIView提供，局部配置权限
    permission_classes = [VVIPPermission]
    
    # 列表页
    # 1. 查询过滤
    # http://127.0.0.1:8000/components/permission/?name=zhouyi&age=&sex=
    filterset_fields = ['name', 'age', 'sex']
    # 如果要过滤大于等于怎么配置呢？
    
    # 2. 排序（分正序和倒序）
    # http://127.0.0.1:8000/components/permission/?ordering=-id
    ordering_fields = ['id', 'age']
    
    # 查询和排序问题
    # 不要在局部设置过滤排序，在全局配置中设置
    # filter_backends = [DjangoFilterBackend]
    # filter_backends = [OrderingFilter]
    
    # 3. 分页
    pagination_class = CustomPagination
    

    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    



