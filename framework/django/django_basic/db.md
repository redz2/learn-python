# 数据操作
***
* 主要描述如何操作数据库数据，思考到底生成了怎样的SQL语句？需要执行多少次SQL？
***

* 单表操作
1. 增
```py
# 新增一条记录: user object
obj = models.UserInfo.objects.create(**{"name": "zz"}) 
obj.save() # 保存到数据库

# 批量创建: 生成一条SQL
models.UserInfo.object.bulk_create(
    objs = [
        models.UserInfo(**{"name": "zz"}), 
        models.UserInfo(**{"name": "yy"})
    ],
    batch_size = 20, # 一次最多创建20个记录
)
```
2. 删
```py
data = models.UserInfo.objects.filter(pk=2) # QuerySet: 记录集
# data.query: SQL语句
data.delete() # 返回受影响的行数，一般不用获取

models.UserInfo.objects.get(pk=2) # user object
```
3. 改
```py
# 通过save更新，先通过id查询出一个object，然后修改object，然后save
# 通过update更新
model.UserInfo.objects.filter(pk=1).update(name="zz")
```
4. 查
```py
models.UserInfo.objects.get(pk=1)    # 获取一条数据，Object
models.UserInfo.objects.all()        # 获取全部数据
models.UserInfo.objects.filter(pk=2) # 获取符合条件的数据
models.UserInfo.objects.filter(pk__gt=1).exclude(pk=10)
# gt、gte、lt、lte、in
# contains、startswith、endswith
# isnull
models.UserInfo.objects.filter(pk__gt=2)                        # QuerySet
models.UserInfo.objects.filter(pk=2).first()                    # Object or None
models.UserInfo.objects.filter(pk=2).exists()                   # True/False
models.UserInfo.objects.filter(pk=2).order_by("id")             # QuerySet
models.UserInfo.objects.filter(pk=2).order_by("-id", "name")    # QuerySet

# 默认QuerySet是一个包含obj的列表，可以变成包含字典或元组的列表，每一条记录使用什么来表示？对象、字典、元组
# data = models.UserInfo.objects.filter(id=99).values("id", "name")         -> QuerySet [{"字段名": "字段值"},{}]
# data = models.UserInfo.objects.filter(id=99).values_list("id", "name")    -> QuerySet [("字段名","字段值"),()]
```

* 一对多数据操作
    * 总结: filter实际上就是用来构造SQL，当过滤字段包含多张表，会自动进行联表查询
    * 注意: 只能更新自己表中的字段，不能更新别的表中的字段（跨表可以查询，但不能更新）
```py
# 更新数据
models.UserInfo.objects.filter(id=1).update(depart__id=2)           # 只能改自己的
# models.UserInfo.objects.filter(id=1).update(depart__title="xxx")  # 不能这么写
models.DepartInfo.objects.filter(id=1).update(title="xxx")          # 只能改自己的
```
```py
# 联表查询
# 1. 正向操作
# 通过部门id来删除: 实际开发没法用
# models.UserInfo.objects.filter(depart_id=3).delete()

# 通过部门名称来删除: 两次SQL查询
# depart_obj = models.DepartInfo.objects.filter(title="xxx").first()
# models.UserInfo.objects.filter(depart=depart_obj).delete()  # 删除xxx部门的所有员工

# 联表查询来删除: 一次SQL查询
# filter: 可以过滤当前表字段，也可以过滤跨表字段
models.UserInfo.objects.filter(depart__title="xxx").delete()

# 联表查询返回字典、元组
# 特点: values中存在联表查询的字段
models.UserInfo.objects.filter(id__gt=1).values("id", "name", "depart__title")
models.UserInfo.objects.filter(id__gt=1).values_list("id", "name", "depart__title")

users_obj = models.UserInfo.objects.all()
# users_obj = models.UserInfo.objects.all().select_related("depart") # 如何解决效率差的问题？查询时会自动添加inner join
for user in users_obj:
    print(user.depart_id, user.depart.title) # 否则会执行联表查询，效率很差

# 2. 反向操作: 一般用正向操作
models.Department.objects.filter(title="销售部").values("id", "title", "userinfo__name") # 通过表名进行联表查询，默认使用表名小写
# 如果有多个外键呢？比如depart_id，new_depart_id，就不知道是和表中哪个外键进行关联的
# 所以当有多个外键时，这么写就有问题，不知道是哪个字段
```

* 多对多数据操作
```py
# 增
models.B2G.objects.create(boy_id=1, gril_id=2)  # 通过字段创建
models.B2G.objects.create(boy=boy_object, girl=gril_object) # 通过对象创建
# 查
models.B2G.objects.filter(boy__name="zz").selected_related("girl") # 三张表做联表查询，是否联表，哪些表做了联表
```