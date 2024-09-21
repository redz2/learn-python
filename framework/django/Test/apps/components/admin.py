from django.contrib import admin
from .models import Student

# Register your models here.

# Admin提供了一个管理员平台，用来管理各种数据

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    
    # 在页面中显示指定字段的数据信息
    list_display = ["name"]
    
    # 选择指定的字段作为条件过滤
    list_filter = ["name"]
    
    # 指定每一页有多少条数据
    # list_per_page = 10
    
    # 配置搜索条件
    search_fields = ("name")
    
    # 可以编辑
    list_editable = ("name")
    
    
    # 在数据详情页中允许修改的字段
    fields = ("name")
    
    
    # 设置只读字段
    readonly_fields = ("name",)
    
    



# 要使用Admin后台管理，需要先创建管理员
# python manage.py createsuperuser
# 用户认证机制: django.contrib.auth提供视图、模板、模型，实现了登录，登出，修改密码等
# 权限认证系统: django.contrib.auth完成了基于RBAC的权限认证机制

# 前台站点
# 所有用户访问的站点

# 后台站点
# 不懂代码的维护人员对数据库内容进行增删改查

# RBAC(基于角色分配的访问控制机制)
# 3表RBAC -> 用户表 + 角色表 + 权限表（每个字段不可拆分）
# 5表RBAC -> 用户表 + 角色表 + 权限表 + 用户角色表 + 角色权限表
# 6表RBAC -> 用户表 + 角色表 + 权限表 + 用户角色表 + 角色权限表 + 用户权限表
# auth_user
# auth_user_groups
# auth_user_user_permissions
# auth_group
# auth_group_permissions
# auth_permission