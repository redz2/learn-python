from django.urls import path

# 建议使用绝对导入
from apps.api import views

app_name = "api" # 生成命名空间

urlpatterns = [
    # FBV
    path('home/', views.home, name="home"),
    path('news/<str:nid>/edit/', views.news, name="news"),
    path('article/', views.article, name="article"),
    # CBV
    path('users/', views.UsersView.as_view()) 
]

