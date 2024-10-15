from django.urls import path, re_path
from . import views

app_name = "firststep" # 生成命名空间

urlpatterns = [
    path('test/', views.test),
    
    # url中最后的斜杠(slash)问题
    # 如果访问时不加slash，django会重定向到带slash的地址
    
    # 路由
    # 传统写法
    # http://127.0.0.1:8000/firststep/home/1/
    path('home/<int:nid>/', views.home),
    
    # 查询字符串
    # http://127.0.0.1:8000/firststep/home2/?nid=100
    path('home2/', views.home2)
    
    # int 整数
    # str 字符串
    # slug 字母+数字+下划线
    # uuid
    # path 路径
    
    # 正则写法
    
]
