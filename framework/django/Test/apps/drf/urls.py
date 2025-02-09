from django.urls import path
from apps.drf import views

app_name = "drf" # 生成命名空间

urlpatterns = [
    path('students/', views.StudentsView.as_view()),
]