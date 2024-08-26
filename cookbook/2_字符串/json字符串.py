import json

data = {
    "name": "zhouyi",
    "age": 18
}

# 序列化: dict -> json_str
json_str = json.dumps(d, indent=2)

# 反序列化: json_str -> dict
json_dict = json.loads(json_str)

# json模块的高级使用
class Person():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
# 自定义编码器 obj -> dict
def person_encoder(obj):
    if isinstance(obj, Person):
        return {"name": obj.name, "age": obj.age}
    else:
        raise TypeError("Object of type Person is not JSON serializable")

# 自定义解码器 dict -> obj 
def person_decoder(obj):
    if "name" in obj and "age" in obj:
        return Person(obj["name"], obj["age"])
    else:
        return obj
     
person = Person("zhouyi", 18)
# obj -> 字典 -> json_str
json_str = json.dumps(obj, default=person_encoder, indent=2)
        
# json_str -> 字典 -> obj
json.loads(json_str, object_hook=person_decoder)