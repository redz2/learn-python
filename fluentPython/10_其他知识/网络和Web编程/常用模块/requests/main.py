import requests

# 1. GET请求
response = requests.get('https://baidu.com')
print(response.status_code)
print(response.url)
print(response.headers)
print(response.cookies)

# 对响应结果进行utf-8编码
response.encoding = "utf-8"
print(response.text)

# 带参数的GET
# response = requests.get("http://httpbin.org/get?name=shaw&age=23")

# data = {
#     "name": "shaw",
#     "age": 23
# }
# response = requests.get("http://httpbin.org/get", params=data)


# 2. POST
# response = requests.post("http://httpbin.org/post", params=data)


"""复杂的网络请求

1. 添加网络请求头
headers = {'User-Agent': 'XXX'}
requests.get('http://www.baidu.com', headers=headers)

2. 验证cookies

"""





