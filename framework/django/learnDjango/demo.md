# 知识点
1. 发短信
    * 腾讯云: 注册账号，开通服务 + 缴费，API or SDK
    * 阿里云
```python
import requests

def send_sms(mobile, content):
    url = 'http://sms-api.luosimao.com/v1/send.json'
    data = {
       'mobile': mobile,
        'message': content,
        'apikey': 'your_api_key'
    }
    response = requests.post(url, data=data)
    return response.json()

if __name__ == '__main__':
    result = send_sms('your_mobile_number', 'your_message')
    print(result)
```

2. 菜单设计
    * 根据用户角色显示不同的菜单
    * 如何控制菜单是否显示？user - role - permission - menu
        * 用户是什么角色？
        * 角色拥有哪些权限？role - permission
        * 角色能查看哪些菜单？role - menu 
    * 是否需要存在数据库中（灵活带来的是复杂度，性能差）
        * 如果角色固定
        * 如果菜单固定