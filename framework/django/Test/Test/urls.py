"""
URL configuration for Test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
# 导入app中的子路由和视图函数
from apps.api import views, urls

urlpatterns = [
    # admin后台管理
    path('admin/', admin.site.urls),
    path("api/", include("apps.api.urls", namespace="api")),
    path("drf/", include("apps.drf.urls", namespace="drf")),
    path("nodrf/", include("apps.nodrf.urls", namespace="nodrf")),
    path("req/", include("apps.req.urls", namespace="req")),
    path("components/", include("apps.components.urls", namespace="components")),

    # 正则表达式（用的比较少）
    # re_path(r'users/(\d+)/(\w+)/', views.users) # 位置参数
    re_path(r'users/(?P<uid>\d+)/(?P<uname>\w+)/', views.users) # 将参数传递给函数
]
