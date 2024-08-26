# swagger_client.UserApi

All URIs are relative to *http://api.fuguang.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_change_active_put**](UserApi.md#user_change_active_put) | **PUT** /user/change_active | 修改账号状态
[**user_change_pwd_put**](UserApi.md#user_change_pwd_put) | **PUT** /user/change_pwd | 修改账号密码
[**user_get**](UserApi.md#user_get) | **GET** /user | 用户列表接口
[**user_id_delete**](UserApi.md#user_id_delete) | **DELETE** /user/{id} | 删除用户
[**user_id_get**](UserApi.md#user_id_get) | **GET** /user/{id} | 查询用户
[**user_id_put**](UserApi.md#user_id_put) | **PUT** /user/{id} | 修改用户
[**user_login_post**](UserApi.md#user_login_post) | **POST** /user/login | 用户登录
[**user_post**](UserApi.md#user_post) | **POST** /user | 新建用户


# **user_change_active_put**
> object user_change_active_put(authorization, body=body)

修改账号状态

修改账号状态

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
authorization = 'authorization_example' # str | 
body = swagger_client.Body() # Body |  (optional)

try:
    # 修改账号状态
    api_response = api_instance.user_change_active_put(authorization, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_change_active_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **body** | [**Body**](.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_change_pwd_put**
> object user_change_pwd_put(authorization, body=body)

修改账号密码

修改账号密码

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
authorization = 'authorization_example' # str | 
body = swagger_client.Body() # Body |  (optional)

try:
    # 修改账号密码
    api_response = api_instance.user_change_pwd_put(authorization, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_change_pwd_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **body** | [**Body**](.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get**
> object user_get(name, token)

用户列表接口

获取所有用户列表

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
name = 'name_example' # str | 
token = 'token_example' # str | 

try:
    # 用户列表接口
    api_response = api_instance.user_get(name, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **token** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_id_delete**
> object user_id_delete(id, authorization)

删除用户

通过id删除用户

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
id = 56 # int | 
authorization = 'authorization_example' # str | 

try:
    # 删除用户
    api_response = api_instance.user_id_delete(id, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **authorization** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_id_get**
> object user_id_get(id, authorization)

查询用户

通过id查询用户信息

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
id = 56 # int | 
authorization = 'authorization_example' # str | 

try:
    # 查询用户
    api_response = api_instance.user_id_get(id, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **authorization** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_id_put**
> object user_id_put(id, authorization, body=body)

修改用户

通过id修改用户信息

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
id = 56 # int | 
authorization = 'authorization_example' # str | 
body = swagger_client.Body() # Body |  (optional)

try:
    # 修改用户
    api_response = api_instance.user_id_put(id, authorization, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **authorization** | **str**|  | 
 **body** | [**Body**](.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_login_post**
> object user_login_post(body)

用户登录

用户登录

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
body = swagger_client.Body() # Body | 

try:
    # 用户登录
    api_response = api_instance.user_login_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_post**
> object user_post(body)

新建用户

新建用户

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
body = swagger_client.Body() # Body | 

try:
    # 新建用户
    api_response = api_instance.user_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

