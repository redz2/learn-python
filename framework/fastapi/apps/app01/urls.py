from fastapi import APIRouter
from pydantic import BaseModel, Field, validator
from typing import List,Optional


# 子路由接口对象
user = APIRouter()

# Model
class Addr(BaseModel):
    province: str
    city: str

# 有默认值就是选填，没有默认值就是必填
class User(BaseModel):
    id: int
    name: Optional[str]
    age: Optional[int] = Field(default=None, gt=0, lt=100) # 通过Field进行校验
    friends: List[int] = []
    addr: Optional[Addr] = None

    # 通过校验装饰器进行字段校验
    @validator("name")
    def name_must_alpha(cls, value: str):
        # assert
        assert value.isalpha(), "name must be alpha"
        return value

class UserOut(BaseModel):
    name: str
    age: int
    
# 如何区分函数参数是什么？
# 路径参数？路径中定义的
# 查询参数？路径中未定义的
# 请求体？参数是BaseModel
# form表单？参数是Form
@user.get("/login")
def user_login():
    return {"user": "login"}


# 请求体数据
# content: application/json
# 客户端 -> json字符串 -> 字节序列 -> 服务器 
#                                  -> json字符串 -> 字典 -> User对象 -> 处理逻辑 
#                                                                     -> 序列化 -> 字典 -> json字符串 -> 字节序列 
#                                                                                                      -> 客户端

# @user.post("/reg", response_model=UserOut)
# @user.post("/reg", response_model=User, response_model_exclude_unset=True)
@user.post("/reg", response_model=User, response_model_exclude=["addr"])
def user_reg(user: User):
    """
    response_model 响应体的数据结构
    
    response_model_exclude_unset 排除没有设置的值
    response_model_exclude_none  排除结果为None的值
    response_model_exclude_default 排除默认值
    
    response_model_exclude 排除哪些字段
    response_model_include 包含哪些字段
    """
    # 存入数据库
    return user

# Form表单
# pip3 install python-multipart
from fastapi import Form
# content: application/x-www-form-urlencoded
# 通过form表单来解析传过来的参数
@user.post("/form")
def test_form(username: str = Form(max_length=16, min_length=1),
              password: str = Form(max_length=16, min_length=1)):
    # print(f"{username} {password}")
    return {
        "username": username,
        "password": password
    }
    
# 文件上传
from fastapi import File, UploadFile
# content: multipart/form-data
@user.post("/file")
def get_file(file: bytes = File()):
    # 适合小文件上传，字节流
    return {
        "file_name": "ok"
    }
    
@user.post("/files")
def get_files(files: List[bytes] = File()):
    # 上传多个文件
    return {
        "file_name": "ok"
    }

# 路径参数
@user.post("/upload_file")
# 路径函数
def upload_files(file: UploadFile):
    # 文件句柄
    return {
        "file_name": file.filename
    }



