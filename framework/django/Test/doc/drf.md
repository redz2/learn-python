## djangorestframework

思想：大量缩减编写api接口的代码
中文文档：q1mi.github.io/Django-REST-framework-documentation/#django-rest-framework

# drf框架

1. 序列化器: Serializer、ModelSerializer --> drf
2. 视图类: request、response --> req
    * View（django）
    * APIView
    * GenericAPIView
    * GenericAPIView + Mixins
    * 通用视图子类
3. 视图集: --> req
    * ViewSet
    * GenericViewSet
    * GenericViewSet + Mixins
    * ModelViewSet
    * ReadOnlyModelViewSet
4. 路由集: --> req
    * 只有视图集才能使用路由集
    * 使用Mixins中的视图方法
5. 组件: --> components
    * 认证
    * 权限
    * 限流
    * 查询
    * 排序
    * 分页
    * 错误处理 






