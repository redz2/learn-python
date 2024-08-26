# swagger_client.ArchivesApi

All URIs are relative to *http://api.fuguang.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archives_get**](ArchivesApi.md#archives_get) | **GET** /archives | 档案列表
[**archives_id_delete**](ArchivesApi.md#archives_id_delete) | **DELETE** /archives/{id} | 删除档案
[**archives_id_get**](ArchivesApi.md#archives_id_get) | **GET** /archives/{id} | 查询用户档案
[**archives_id_put**](ArchivesApi.md#archives_id_put) | **PUT** /archives/{id} | 修改档案信息
[**archives_post**](ArchivesApi.md#archives_post) | **POST** /archives | 新建档案


# **archives_get**
> object archives_get(authorization)

档案列表

档案列表

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ArchivesApi()
authorization = 'authorization_example' # str | 

try:
    # 档案列表
    api_response = api_instance.archives_get(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchivesApi->archives_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archives_id_delete**
> object archives_id_delete(authorization, id)

删除档案

通过id删除档案

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ArchivesApi()
authorization = 'authorization_example' # str | 
id = 56 # int | 

try:
    # 删除档案
    api_response = api_instance.archives_id_delete(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchivesApi->archives_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archives_id_get**
> object archives_id_get(authorization, id)

查询用户档案

查询用户档案

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ArchivesApi()
authorization = 'authorization_example' # str | 
id = 56 # int | 

try:
    # 查询用户档案
    api_response = api_instance.archives_id_get(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchivesApi->archives_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archives_id_put**
> object archives_id_put(authorization, id, body=body)

修改档案信息

通过id修改档案信息息

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ArchivesApi()
authorization = 'authorization_example' # str | 
id = 56 # int | 
body = swagger_client.Body() # Body |  (optional)

try:
    # 修改档案信息
    api_response = api_instance.archives_id_put(authorization, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchivesApi->archives_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **id** | **int**|  | 
 **body** | [**Body**](.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archives_post**
> object archives_post(authorization, body)

新建档案

新建档案

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ArchivesApi()
authorization = 'authorization_example' # str | 
body = swagger_client.Body() # Body | 

try:
    # 新建档案
    api_response = api_instance.archives_post(authorization, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchivesApi->archives_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **body** | [**Body**](.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

