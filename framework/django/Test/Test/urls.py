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

# from rest_framework.documentation import include_docs_urls




urlpatterns = [
    # admin后台管理
    path('admin/', admin.site.urls),
    # coreapi文档接口
    # path('docs/', include_docs_urls(title="API DOC")),
    # swagger-openapi文档
    # path('swagger/', schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger"),
    # drf-yasg不支持django5.0 可以看下最新的项目: https://github.com/tfranzel/drf-spectacular

    # 传统路由 **
    path('home/', views.home),
    path('news/<str:nid>/edit/', views.news),
    # int
    # str
    # slug: 字母+数字+下划线
    # uuid
    # path: 路径，可以包含/
    path('article/', views.article),

    # 路由分发 ** 
    # 如何动态导入模块？importlib.import_module("apps.api.urls")
    # 什么是反射？getattr(x, "y", "default_value") ===> x.y
    # namespace需要设置app_name

    # partial(func, param="xxx")
    path("api/", include("apps.api.urls", namespace="api")),
    path("drf/", include("apps.drf.urls", namespace="drf")),
    path("nodrf/", include("apps.nodrf.urls", namespace="nodrf")),
    path("req/", include("apps.req.urls", namespace="req")),
    path("components/", include("apps.components.urls", namespace="components")),


    # 手动做路由分发
    # path("test/", (
    #     [], None, None
    # )),

    # 正则表达式（用的比较少）
    # re_path(r'users/(\d+)/(\w+)/', views.users) # 位置参数
    re_path(r'users/(?P<uid>\d+)/(?P<uname>\w+)/', views.users) # 将参数传递给函数
]
