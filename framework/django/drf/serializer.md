# 序列化器
* 序列化器有什么用？本来下面这两件事情都要我们自己来实现
    * 能够对表单提交的数据进行校验，并转换为obj
    * 能够将obj转换为字典，并返回给前端
        * 如何根据不同的请求方式返回不同字段？
          * 定义不同的序列化器
```py
# serializers.py
# 序列化: 将obj转换为字典
# 反序列化: 将字典转换为obj
class StudentSerializer(serializers.ModelSerializer):
    # 为什么数据要校验？
    # 1. 防止恶意数据入库
    # 2. 提升数据准确性
    # 3. 方便后续数据处理

    # 如果继承serializers.Serializer类，不能从模型中导入字段，只能自己定义字段
    # 而且，Serializer默认没有实现update()和create()方法，需要自己实现

    # 字段声明: 每个字段如何校验？
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=16, min_length=2, required=True, error_messages={
        'blank': '姓名不能为空',
        'null': '姓名不能为空',
        'max_length': '姓名长度不能超过16',
        'min_length': '姓名长度不能少于2',
    })
    # 常用字段选项参数: 用于数据写入时进行校验
    # required: 是否必填
    # max_length: 最大长度
    # min_length: 最小长度
    # allow_blank: 是否允许为空
    # trim_whitespace: 是否自动去除首尾空格
    # max_value: 最大值
    # min_value: 最小值
    # error_messages: 错误提示信息

    # 何时校验？提交表单数据，需要修改数据时
    # 1. 调用is_valid()方法时，才会进行校验: 执行run_validators()方法
    # 2. 调用save()方法时，才会保存数据

    # 数据校验顺序？最后会得到validated_data
    # 1. 字段内置选项
    # 2. validate_<字段名>
    # 3. validators属性
    # 4. 全局validate()方法

    # 校验单个字段
    # def validate_name(self, value):
    #     if value == 'admin' or value == 'root':
    #         raise serializers.ValidationError('不能使用admin或root作为姓名')
    #     return value

    # 全局校验
    # def validate_name(self, attrs):
    #     if attrs['name'] == 'admin' or attrs['name'] == 'root':
    #         raise serializers.ValidationError('不能使用admin或root作为姓名')
    #     del attrs["password"] # 需要校验，但是不需要存入数据库，所以删除password字段
    #     return attrs # 必须返回数据，validated_date会作为参数传入create()和update()方法

    # 默认实现了这两个方法
    # 更新数据: 此时数据已经校验完成
    # def update(self, instance, validated_data):
    #     # 不一定是更新数据库，也可以更新缓存，是独立于数据库的
    #     return super().update(instance, validated_data)
    
    # 添加数据
    # def create(self, validated_data):
    #     return super().create(validated_data)

    class Meta:
        model = models.Student
        fields = '__all__'  # 序列化所有字段
        # fields = ['id', 'name', 'age', 'classmate', 'description']  # 序列化指定字段

        exclude = ['password']  # 序列化时排除password字段
        read_only_fields = ['id']  # 只读字段
        # extra_kwargs = {
        #     'name': {'max_length': 16, 'error_messages': {'max_length': '姓名长度不能超过16'}},
        # }  # 额外参数，用于字段校验

# views.py
class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all() # 数据库查询集
    serializer_class = StudentSerializer # 序列化器

# urls.py
urlpatterns = [
    path('students/', StudentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('students/<int:pk>/', StudentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
```