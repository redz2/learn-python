# Django
1. 安装django
```
pip3 install django
```

2. 创建django项目
```
django-admin startproject myproject  # 直接创建项目会生成如下目录结构

myproject
|-- manage.py [项目管理工具]
|-- myproject
    |-- __init__.py
    |-- settings.py [配置文件，先读取django源码内配置，再读取settings配置，会覆盖]
    |-- urls.py [主路由]
    |-- asgi.py [异步]
    |-- wsgi.py [同步]
```

3. 创建venv虚拟环境（不要随便改项目的名称和目录，虚拟环境activate会失效）
```
cd myproject
python -m venv .venv
source .venv/bin/activate
```

```
pip3 install django
django-admin startproject myproject . # 这样就可以在当前目录中创建项目了，项目名称和目录名称最好要一致！
```

4. 创建多app（建议这么放）
```
cd myproject
mkdir apps
cd apps
python3 ../manage.py startapp myapp
```

5. Http请求的生命周期
    * 路由 
    * 视图
    * 静态文件和媒体文件
        1. 静态文件: 根目录下static，注册app的static
        ```html
        {% load static %}
        <img src="{% static 'api/1.png'%}">
        ```
        2. 媒体文件: 用户上传的数据
        ```
        from django.conf.urls.static import static
        from django.conf import settings
        from apps.api import views
        urlpatterns = [
            path('api/', include('apps.api.urls')),
        ] + static(settings.MEDIA_URL, document_rootsettings.MEDIA_ROOT)

        ```
    * 模板
    * 中间件
    * ORM

6. 框架
    * 我们在django或fastapi框架中编写函数，只是去给关键对象添加属性而已
    * 为啥reverse能根据字符串反向生成url？
    * gin内部也维护了一个map来记录url和handler的对应关系




















1. 我妈为什么这么拼命
其实我们家条件虽然说不上大富大贵，但也算是吃喝不愁，我妈是典型的农村妇女，这一辈子目前大部分时间都是在乡下，极少数情况会去城里
    以前，我认为我是个地地道道的农村人，家里住着自建房，种着地。现在，已经拆迁了，不过不像网上传的那样，拆完