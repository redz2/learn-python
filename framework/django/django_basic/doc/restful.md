## RESTfulAPI
1. 域名: `https://api.example.com/api/`
2. 版本: `https://api.example.com/api/v1/`
3. 路径: 使用名词
```
GET /zoos:列出所有动物园
POST /zoos:新建一个动物园(上传文件)
GET /zoos/ID:获取某个指定动物园的信息
PUT /zoos/ID:更新某个指定动物园的信息
PATCH /zoos/ID:更新某个指定动物园的信息
DELETE /zoos/ID:删除某个动物园
GET /zoos/ID/animals:列出某个指定动物园的所有动物
DELETE /zoos/ID/animals/ID:删除某个指定动物园的指定物
```
4. 过滤信息: 如果记录过多，服务器不可能一次性返回所有数据(API需要提供过滤参数)
```
?limit=10
?offset=10
?page=20&per_page=100
?sortby=name&order=desc
?animal_type_id=1
```
5. 状态码
6. 错误处理: 4xx or 5xx
```json
{
    error: "InValid API key"
}
```
7. 返回结果
```
GET /collections:返回资源对象的列表(数组)
GET /collections/ID:返回单个资源字典(json)
POST /collections:返回新生成的资源字典(json)
PUT /collections/ID:返回修改后的资源字典(json)
DELETE /collections/ID:返回一个空文档(空字符串,空字典)
```
8. 序列化
json、pickle、base64
序列化：obj ---> json
反序列化：json ---> obj


