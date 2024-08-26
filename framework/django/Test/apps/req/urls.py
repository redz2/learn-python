from django.urls import path, re_path
from apps.req import views

app_name = "req"

# url和方法如何对应？

urlpatterns = [
    # 什么时候views中的类会实例化呢？没明白
    path('students/', views.StudentsView.as_view()), # django原生View
    
    # APIView使用drf提供的request和response
    path('stuapi/', views.StudentsAPIView.as_view()),  # APIView
    # 正则匹配字符串前面要加r，不然会报错，虽然没影响: SyntaxWarning: invalid escape sequence '\d'
    re_path(r'^stuapi/(?P<pk>\d+)/', views.StudentsInfoAPIView.as_view()),  # APIView
    
    # 通用视图类
    path('generic/', views.StudentsGenericAPIView.as_view()),  # GenericAPIView
    re_path(r'^generic/(?P<pk>\d+)/', views.StudentsInfoGenericAPIView.as_view()),  # GenericAPIView
    
    # 下面要开始封装功能了，本质上就是GenericAPIView
    # 自己写的代码能有大佬封装的好吗？
    
    # 通用视图类: GenericAPIView + Mixins（Mixins提供的方法和视图类中需要写的方法名称不一致，需要实现get、post等方法）
    path('mixins/', views.StudentListAPIView.as_view()),  # GenericAPIView + ListModelMixins + CreateModelMixin
    re_path(r'^mixins/(?P<pk>\d+)/', views.StudentRetrieveAPIView.as_view()),  # GenericAPIView + RetrieveModelMixin + UpdateModelMixin + DestroyModelMixin
    
    # 视图子类: 已经封装好get、post等方法了
    path('list/', views.StuAPIView.as_view()),  # ListCreateAPIView
    re_path(r'^list/(?P<pk>\d+)/', views.StuInfoAPIView.as_view()),  # RetrieveUpdateDestroyAPIView
    
    #######################################################################################################################
    #
    # 视图集: ViewSet
    #
    # View中as_view()方法，通过dispatch()根据请求方法，转发给对应的函数
    # ViewSet中的as_view()重写了，通过传入的字典把请求方法和调用函数做了绑定，然后再调用dispatch()
    path('viewset/', views.StudentViewSet.as_view({"get": "list"})),
    re_path(r'viewset/(?P<pk>\d+)/', views.StudentViewSet.as_view({"get": "retrieve"})),
    
    # 通用视图集: GenericViewSet + Mixins（ViewSet可以绑定请求方法和调用函数，直接使用Mixins提供的函数就行了）
    path('gmix/', views.StuGenMixViewSet.as_view({"get": "list", "post": "create"})),
    re_path(r'gmix/(?P<pk>\d+)/', views.StuGenMixViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    
    # ModelViewSet（就是继承了所有Mixins）
    path('mvs/', views.StuMVS.as_view({"get": "list", "post": "create"})),
    re_path(r'mvs/(?P<pk>\d+)/', views.StuMVS.as_view({"get": "retrieve", "put": "update", "delete": "destroy",})),  # 现在可以使用一个类了
    
    # ReadOnlyModelViewSet（只继承读相关的Mixins）
    path('rmvs/', views.StuRMVS.as_view({"get": "list"})),
    re_path(r'rmvs/(?P<pk>\d+)/', views.StuRMVS.as_view({"get": "retrieve",})),  # 现在可以使用一个类了
    
]

# 路由集
# 视图集可以使用路由集，自动生成路由
# SimpleRouter 上线使用
# DefaultRouter 开发使用
from rest_framework.routers import SimpleRouter,DefaultRouter
router = DefaultRouter()

# 视图集中的写的方法名称一定要标准
router.register("xxxx", views.StuMVS, basename="xxxx")
router.register("yyyy", views.StudentViewSet, basename="yyyy")

urlpatterns += router.urls

# 如何为自定义的路由方法生成路由信息


