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

# name 给路由起个名字 **

# 如何反向生成url？前后端不分离时才会用到
# url1 = reverse("home")
# url2 = reverse("news", kwargs={"nid": "xxx"})
# url3 = reverse("api:home") # 如果有namespace呢？

# slash url中最后的斜杠问题
# 如果访问时不加slash，django会重定向到带slash的地址