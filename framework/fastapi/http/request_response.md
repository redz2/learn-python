1. 请求(request)
* 请求首行
```
POST /api/v1/auth/password/login/?loginWay=password 
```
* 请求头
```
content-type: application/json
charset = utf-8
user-agent: xxx
```
* 请求体
```
{
    "username": "zsy",
    "password": 123
}
```
2. 响应(response)
* 响应首行
```
HTTP/1.1 200 OK
```
* 响应头
```
content-type: application/json
date: xxx
content-length: 73
```
* 响应体
```
{
    "code": 0,
    "msg": "validate error",
    "data": []
}
```