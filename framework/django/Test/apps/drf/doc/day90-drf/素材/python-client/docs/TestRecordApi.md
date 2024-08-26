# swagger_client.TestRecordApi

All URIs are relative to *http://api.fuguang.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**testrecord_get**](TestRecordApi.md#testrecord_get) | **GET** /testrecord | 测试记录列表
[**testrecord_id_delete**](TestRecordApi.md#testrecord_id_delete) | **DELETE** /testrecord/{id} | 删除测试记录
[**testrecord_id_get**](TestRecordApi.md#testrecord_id_get) | **GET** /testrecord/{id} | 查询测试详情


# **testrecord_get**
> object testrecord_get(authorization)

测试记录列表

测试记录列表

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TestRecordApi()
authorization = 'authorization_example' # str | 

try:
    # 测试记录列表
    api_response = api_instance.testrecord_get(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestRecordApi->testrecord_get: %s\n" % e)
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

# **testrecord_id_delete**
> object testrecord_id_delete(id, authorization)

删除测试记录

删除测试记录

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TestRecordApi()
id = 56 # int | 
authorization = 'authorization_example' # str | 

try:
    # 删除测试记录
    api_response = api_instance.testrecord_id_delete(id, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestRecordApi->testrecord_id_delete: %s\n" % e)
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

# **testrecord_id_get**
> object testrecord_id_get(id, authorization)

查询测试详情

查询测试详情

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TestRecordApi()
id = 56 # int | 
authorization = 'authorization_example' # str | 

try:
    # 查询测试详情
    api_response = api_instance.testrecord_id_get(id, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestRecordApi->testrecord_id_get: %s\n" % e)
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

