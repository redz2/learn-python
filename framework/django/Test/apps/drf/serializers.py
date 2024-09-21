# 字节序列 ---> 字符串 ---> 字典 ---> 对象

from rest_framework import serializers
from apps.drf.models import Student

# {} <---> 序列化器 <---> obj
# 1. 数据格式转换 ---> 需要定义数据格式
# 2. 数据校验 ---> 需要定义如何校验数据
# 3. 数据写入 ---> 需要定义如何写入
# 4. 序列化:  obj -> {} -> JSON
# 5. 反序列化: JSON -> {} -> obj (数据校验)

# serializer不是只能为数据库模型类转换数据格式,也可以为非数据库模型类的数据定义
# serializer是独立于数据库的


# 模型类序列化器类
# 1. 基于模型类自动生成序列化器字段
# 2. 默认实现update和create

class StudentSerializer(serializers.ModelSerializer):

    """学生信息模型类序列化器"""

    # 1. 字段声明（哪些字段需要转换？）
    # serializers.Serializer 需要自己声明，不能从模型中导入字段
    # Serializer默认没有实现update()和create()
    
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=16, min_length=4, error_messages={
    #     "max_length": "错误说明",
    #     "min_length": "错误说明",
    # })
    # sex = serializers.BooleanField()
    # classmate = serializers.CharField()
    # description = serializers.CharField()
    
    # serializer.errors() -> 关注校验过程中产生的错误及处理
    # serializer.error_messages() -> 关注为字段自定义错误信息
    
    # 字段声明可以覆盖从model导入的字段『没有必要重写，只需要extra_kwargs补充验证选项』（有时候导入的字段还需要进行限制怎么办？）

    # 2. 如果当前序列化器继承的是 ModelSerializer，可以简写
    class Meta:
        
        model = Student # 必填，指定当前序列化器类绑定的模型类
        fields = "__all__" # 必填，指定导入模型类的哪些字段作为序列化类的字段
        # fields = ["字段名称"]
        
        # 排除哪些字段不需要导入
        # exclude = []
        
        # 只读字段列表，只会在序列化过程使用，反序列化时不会用到
        # read_only_fields = []
        
        # 补充字段限制选项
        # extra_kwargs = {
        #   "name": { "min_length": 4}
        # }
        

    # 3. 验证对象字段
    # 何时执行？
    # 调用is_valid()时执行run_validators()
    
    # 执行顺序?
    # 1. 字段内置选项、validate_<字段名>、validators（和声明时的字段顺序有关）
    # 2. validate函数
    
    # 同时校验多个字段的方法
    # validate方法名称固定，attrs就是客户端发送过来的数据，是个字典
    def validate(self, attrs): # -> validated_date
        
        if attrs["name"] == "root" or attrs["age"] > 100:
            # ValidationError继承自APIException
            raise serializers.ValidationError("something wrong")

        # 有些字段需要校验，但是不需要存入数据库
        # del attrs["password"]
        
        # !!!必须返回数据!!!，不然序列化器对象会丢失数据
        return attrs
    
    # 校验单个字段的方法
    def validate_name(self, attr):
        
        if attr == "root":
            raise serializers.ValidationError(f"name的值不能是{attr}")
        
        # 必须返回数据
        return attr
        
    # 自定义验证函数，添加到字段选项中 validators=[check_passwd]
    # 内置字段选项，见下方
    # def check_passwd(data):
    #     print(data)
    #     return data

    # 4. 模型操作的扩展方法
    # API接口的幂等性
    # 客户端发起同样的请求，返回数据是否一致
    
    # 更新和创建时，才需要验证数据
    
    
    def update(self, instance, validated_data):
        # instance是obj
        instance.name = validated_data.get("name")
        instance.age = validated_data.get("age")
        instance.sex = validated_data.get("sex")
        instance.classmate = validated_data.get("classmate")
        instance.description = validated_data.get("description")
        instance.save()
        return instance

    from .models import Student
    def create(self, validated_data: dict):
        """
        添加操作代码
        """
        stu_object = Student.objects.create(**(validated_data))
        return stu_object
    
    
    # 常用字段类型
    # BooleanField
    # CharField
    # IntergerField
    # DecimalField
    # DateTimeField
    # IPAddressField
    # UUIDFeild
    
    # 常用的字段选项参数
    # max_length
    # min_length
    # allow_blank
    # trim_whitespace
    # max_value
    # min_value
    
    # 字段通用选项参数
    # read_only 仅用作序列化输出
    # write_only 仅用作反序列化输入
    # required 反序列化时必须
    # default 反序列化时默认值
    # miss 序列化时使用的默认值
    # allow_null 反序列化时是否可以为空
    # validators 反序列化时使用的验证函数
    # error_message 反序列化时验证错误报错



# 关于数据验证的思考？
# 前端做验证，请求之前验证
# 后端做验证，写入数据库前做验证


# test serializer
class TestSerializer(serializers.Serializer):
    x = serializers.IntegerField()
    y = serializers.IntegerField()
    z = serializers.IntegerField()

class Person():

    z = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y

if __name__ == "__main__":
    # 如何理解序列化？obj <---> {}
    # instance <---> data
    person = Person(1,2)
    ser = TestSerializer(instance=person, context={"message": "ok"})
    print(ser.data)
    print(ser.context)