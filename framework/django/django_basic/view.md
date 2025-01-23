# 视图
1. 关于视图的一些注意事项
    * 文件 or 文件夹（当业务功能比较多时，删除views.py，创建一个文件夹）
    * 相对导入 or 绝对导入（python本质上就是单文件程序，golang也是）
        * 原则: 优先绝对导入
2. requests对象
    * 对象就是一个包裹，可以装很多东西
    * 根据HTTP头信息，会构造requests（和gin思想一致，先把东西准备好，最后要用的时候直接用）
        * 使用框架的感受: 框架帮你把菜都洗好，切好，你只需要炒一下（封装requests）
        * 不使用框架: 我还得洗菜，切菜，做很多麻烦事
        * 为什么fastapi更先进？更容易知道视图函数对应的路由是哪个
        * 前后端分离: vue.js本质上是通过js来渲染html页面，而render是django渲染html页面（本质就是字符串模板替换）
        * 编程和web的关系: 编程更偏向逻辑处理，web更偏向规范，提供一些对象，针对这些对象进行处理
            * 如果对象是飞书，是不是就
    ```python
    from django.shortcuts import render,HttpResponse,reverse

    def login(requests):
        # 1. 获取请求数据
        requests.path_info          # 当前URL
        requests.GET                # URL的参数
        requests.GET.get("xxx")
        requests.method             # 请求方式
        request.body                # 请求体（原始数据） -> 如果content-type符合条件，才会处理内容放到requests.POST中
        request.headers             # 请求头: 包含Cookie
        request.COOKIES

        # 2. 返回响应数据
        res = HttpResponse("login")
        res["xxx"] = "yyy"                          # 设置响应头
        res.set_cookie('xxx', "yyy")
        return HttpResponse("login")                # 响应体 -> HTML
        # return HttpResponse('<div style="color: red">Home</div>')
        # return JsonResponse({"name": "zhouyi"})   # 自动序列化 === HttpResponse(json.dumps(data_dict))
        # return redirect("www.baidu.com")          # 重定向，浏览器会重新发送请求
        # return render(request, "login.html")      # 渲染一个html页面
    ```
3. FBV和CBV