from django.shortcuts import render,HttpResponse,reverse

from django.contrib.auth.decorators import login_required

# 该视图需要用户登录才能访问
@login_required(login_url="/admin/login")
def home(request):

    # 1. HttpResponse
    res = HttpResponse('<div style="color: red">Home</div>')
    return res

from django.views import View
from apps.api import models

class UsersView(View):

    def get(self, request):

        # 数据操作

        # 1. 增删改查（单表操作）
        # 增
        # obj = models.UserInfo.objects.create(**{"name": "zhouyi"}) -> obj
        # obj.pk 是主键，一般是id
        
        # obj = models.UserInfo(**{"name": "zhouyi"}) -> obj
        # obj.save() # 保存到数据库
        
        # 批量创建
        # models.UserInfo.objects.bulk_create(
        #     objs = [models.UserInfo(**{"name": "zhouyi"})],
        #     batch_size = 2,
        # ) -> ???

        # 删
        # data = models.UserInfo.objects.filter(pk=2).delete() # 删除QuerySet
        # data = models.UserInfo.objects.get(pk=2) # 删除obj

        # 改
        # 通过save更新
        # 通过update更新
        # data = models.UserInfo.objects.filter(id=1).update(name="zsy")

        # 查
        # data = models.UserInfo.objects.get(pk=99) -> obj # 获取一条数据
        # data = models.UserInfo.objects.all() -> QuerySet # 获取全部数据
        # data = models.UserInfo.objects.all()[0:3] -> QuerySet # 获取前三条数据
        
        # ***QuerySet*** 通过神奇的双下划线来构造查询条件
        # data = models.UserInfo.objects.filter(id=99)  # where id = 99 -> QuerySet
        # data = models.UserInfo.objects.filter(id__gt=1).exclude(id=99) # where id > 1 and id != 99 -> QuerySet
        # 数字supported: gt,gte,lt,lte,in
        # 字符串supported: contains,startswith,endswith
        # 其他: isnull

        # data = models.UserInfo.objects.filter(id__gt=2) -> QuerySet
        # data = models.UserInfo.objects.filter(id__gt=0).first() -> obj
        # data = models.UserInfo.objects.filter(id__gt=0).exists() -> True/False
        # data = models.UserInfo.objects.filter(id__gt=0).order_by("id") -> QuerySet
        # data = models.UserInfo.objects.filter(id__gt=0).order_by("-id", "name") -> QuerySet
        
        # QuerySet中不再是obj了
        # data = models.UserInfo.objects.filter(id=99).values("id", "name") -> QuerySet [{"字段名": "字段值"},{}]
        # data = models.UserInfo.objects.filter(id=99).values_list("id", "name") -> QuerySet [("字段名","字段值"),()]
    
        # 2. 一对多数据操作
        # 联表查询：depart是ForeignKey
        # 正向操作
        # models.UserInfo.objects.filter(depart__title="销售部").delete() 
        # models.UserInfo.objects.filter(id__gt=1) -> 只查自己数据库的字段
        # models.UserInfo.objects.filter(id__gt=1).values("id", "name", "depart__title") -> 执行一次SQL，联表查询 ￥￥￥
        # models.UserInfo.objects.filter(id__gt=1).values_list("id", "name", "depart__title") -> 执行一次SQL ￥￥￥

        # models.UserInfo.objects.filter(id=1).update(depart__id=2) -> 只能更新自己表中的字段
        # models.UserInfo.objects.filter(id=1).update(depart__title="xxx") -> 不能这么写

        # 反向操作（一般用正向操作）
        # models.Department.objects.filter(title="销售部").values("id", "title", "userinfo__name") -> 通过表名进行联表查询，默认使用表名小写
        # models.Department.objects.filter(title="销售部").values("id", "title", "d1__name") -> 如果有多个外键呢？就不知道是和表中哪个外键进行关联的
 
        # 3. 多对多数据操作
        # models.B2G.objects.create(boy__id=1,gril_id=2)
        # models.B2G.objects.create(boy=boy_object,girl=gril_object)
        
        # models.B2G.objects.filter(boy__name="zy").selected_related("girl")
        # models.B2G.objects.filter(boy__name="zy").values("id", "boy__name", "girl__name") ￥￥￥

        # 4. 一对一数据操作



        # 读写分离：
        # res = models.UserInfo.objects.all() # 还没有读数据
        # new_user = models.UserInfo.objects.create(name="zhouyi", age="18") # 已经写了

        return HttpResponse("users get")

    def post(self, request):
        return HttpResponse("users post")

# 127.0.0.1:8000/news/xyz/
def news(request, nid):
    return HttpResponse("News {}".format(nid))

# 127.0.0.1:8000/news/?nid=xyz
def article(request):
    nid = request.GET.get("nid")
    return HttpResponse("News {}".format(nid))

def users(request, uid, uname):
    return HttpResponse("Users {} {}".format(uid, uname))


