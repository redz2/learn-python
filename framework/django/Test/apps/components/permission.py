# 权限
# APIView中判断视图访问权限 -> check_permissions
# GenericAPIView通过get_object()获取具体模型时，会判断模型对象访问权限 -> check_object_permissions

# 认证的作用是识别客户端身份，但是不能拦截客户端的访问
# 权限是基于认证来实现的，针对不同身份的用户，拦截用户对视图、模型的访问

from rest_framework.permissions import BasePermission

class VVIPPermission(BasePermission):
    """自定义权限"""
    
    # 返回True表示可以访问该视图
    def has_permission(self, request, view):
        
        # 如何判断是否可以访问该视图函数？
        identity = request.query_params.get("identity")
        # return identity == "vvip"
        return True
    
    # 可以自定义报错格式吗？
    # {
    #     "detail": "您没有执行该操作的权限。"
    # }
    
    def has_object_permission(self, request, view, obj):
        # update、delete、destroy
        return True
    
        
        
