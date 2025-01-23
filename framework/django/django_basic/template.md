# 模板
0. 和 vue.js 对比
    * django是将数据和页面一起返回
    * vue.js是通过js来生成页面、获取数据
1. 寻找模板
    * 优先去项目根目录下找 -> 每个app下的templates
        * 'DIRS': [os.path.join(BASE_DIR, 'templates')]
        * app_name/templates/app_name/index.html（用于解决文件重名的问题）
2. 模板处理本质
    * 通过render扩展response功能
    * 实现方式: 通过对字符串模板进行格式化
3. 模板常见语法
    * 关键就是如何动态生成HTML？
    * 为什么需要ajax？就是为了只修改部分页面，已经是个落后的技术了
```python
context = {
    "n1": "z"
    "n2": [1,2,3,4]
    "n3": {
        "name": "z"
        "age": 30
    }
}
```
```html
<ul>
    {% for e in n1 %}
    <li>{{ e }}</li>
    {% endfor %}
</ul>
<p>{{ n2.0 }}</p>
<p>{{ n3.name }}</p>
<ul>
    <!-- n3.items n3.values -->
    {% for key in n3.keys %} 
    <li>{{ e }}</li>
    {% endfor %}
</ul>
```
4. 内置模板函数 和 自定义模板功能
    * 内置模板函数
    ```html
    <!-- lower -->
    <p>{{ n1 | upper }}</p>    
    ```
    * 自定义模板功能 -> app/templatetags
    ```python
    # test.py
    from django import template

    register = template.Library()

    @register.filter  # 自定义filter: 参数1~2个，数据处理
    def myfunc(value):
        return value.upper()

    @register.simple_tag # 参数无限制 & 返回文本
    def mytag(x, y):
        return x + y

    @register.inclusion_tag("app/menu.html") # 参数无限制 & 返回HTML片段（其实就是组件）
    def menu(role):
        # 使用场景: 如果user、role不同，返回不同的HTML页面
        if role == "admin"
            return {"name": "z", "age": 30}
        else:
            return {"name": "y", "age": 3}
    ```
    ```html
    {% load test %}
    <p>{{ mytag 1 2 }}</p>
    <p>{{ n1 | myfunc }}</p>
    {% menu "admin" %}
    ```
    5. 模板的继承: 
    ```html
    <!-- 模板中的占位符 -->
    <head>
    <link rel="stylesheet" href="公共css文件">
    {% block css %}{% endblock%}
    </head>
    <body>
    <header>标题</header>
    {% block body %}{% endblock%}
    <script src="公共js文件"></script>
    {% block js %}{% endblock%}
    <div>尾部</div>
    </body>
    ```
    ```html
    <!-- 继承模板 -->
    {% extends 'app/layout.html' %}
    {% block body %}
        <div>主页</div>
        <!-- include -->
        {% include 'app/header.html' %} 
    {% endblock%}
    ```