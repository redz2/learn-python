# 路由
0. 支持FBV、CBV
    * 如果是函数直接执行
    * 如果是类，执行哪个函数呢？会根据请求方法来执行对应的函数（这里就存在一个问题，类方法和请求方法必须一致）
1. 传统写法: int、str、slug(字母+数字+下划线)、uuid、path
```python
# _path 代码逻辑: path、re_path是通过partial(_path, Pattern=xxxPattern)实现的（先实现通用函数，然后生成特定场景的函数）
# 1. 是否可以调用 -> 函数
# 2. 是否是View类 -> 调用类方法 -> as_view() -> view() -> dispatch() -> handler = getatter(obj, "get") -> handler(request, *args, **kwargs)
# 3. 是否是list或tuple（include或手动分发） -> 调用URLResolver处理
# 4. 否则报错
path('/home', views.home) # 感觉 _path 源码的写法和go有点类似，关键问题在于场景区分
path('/news/<int:nid>/edit', views.news)

def news(request, nid):
    # get nid news
```
2. 正则写法(传统写法用的比较多)
```python
# 正则表达式分组
# re_path(r'users/(\d+)/(\w+)/', views.users) # 函数位置参数
re_path(r'users/(?P<uid>\d+)/(?P<uname>\w+)/', views.users) # 函数关键字参数

def users(request, uid, uname):
    return HttpResponse("Users {} {}".format(uid, uname))
```
3. 路由分发
    * include 代码逻辑 -> (urlconf_module, app_name, namespace)
        * 判断是不是二元组: include(([paths...], None))
        * 判断是不是字符串: include("xxx.app", app_name)
        * 获取urlconf_module
        * 导入模块获取urlpatterns
        * 返回一个tuple
```python
if isintance(arg, tuple):
    ...
else:
    urlconf_module = arg
if isintance(urlconfg_module, str):
    urlconf_module = import_module(urlconf_module) # 动态导入模块
patterns = getattr(urlconf_module, "urlpatterns", urlconf_module) # 反射

path("api/", include("apps.api.urls", namespace="api"))
```
4. 手动分发
* 如果有重复前缀，如何提取公共部分？
```python
path("user/", ([
    path('add/', views.login),
    path('delete/', views.login),
    ], None, None
)),
```
5. name: 给路由起一个名字
```python
path('/home', views.home, name="home") # 有啥用？
# 1. 在视图函数中生成url
def login(request):
    url = reverse("home")
    return redirect(url)
# 2. HTML模板a标签中生成url
<a href="{% url 'home' %}">home</a>
```
6. namespace: 用来辅助name
    * 多个app中使用相同的name，reverse就无法生成url
    * reverse("api:login")
    ```
    # 需要在模块中添加个属性app_name，否则include会报错
    path("api/", include("apps.api.urls", namespace="api"))
    ```
    * namespace: 多层嵌套
        * reverse("api:v1:login")
7. slash: 最后的斜杠问题
    * APPEND_SLASH = True（django会自动重定向到带slash的地址）
8. 当前路由匹配的对象
    * request.reslover_match