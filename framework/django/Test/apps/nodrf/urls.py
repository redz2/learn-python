from django.urls import path,re_path
from apps.nodrf import views

app_name = "nodrf" # 生成命名空间

# 路由
urlpatterns = [
    path('students/', views.Students.as_view()),
    # path('students/<str:pk>/', views.StudentsInfoView.as_view()),
    re_path(r'^students/(?P<pk>\d+)/', views.StudentsInfoView.as_view())
]

