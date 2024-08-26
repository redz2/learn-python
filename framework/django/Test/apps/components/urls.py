from django.urls import path, re_path
from apps.components import views

app_name = "components" # 生成命名空间

urlpatterns = [
    path('auth/', views.StudentsAPIView.as_view()),
    path('permission/', views.PermissionViewSet.as_view({"get": "list", "post": "create"})),
    re_path(r'^permission/(?P<pk>\d+)/', views.PermissionViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
]