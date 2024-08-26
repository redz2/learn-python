# swagger_client.MedicalRecordsApi

All URIs are relative to *http://api.fuguang.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**medical_records_get**](MedicalRecordsApi.md#medical_records_get) | **GET** /medical_records | 就诊记录列表
[**medical_records_id_delete**](MedicalRecordsApi.md#medical_records_id_delete) | **DELETE** /medical_records/{id} | 删除就诊记录
[**medical_records_id_get**](MedicalRecordsApi.md#medical_records_id_get) | **GET** /medical_records/{id} | 就诊详情
[**medical_records_post**](MedicalRecordsApi.md#medical_records_post) | **POST** /medical_records | 新建就诊记录


# **medical_records_get**
> object medical_records_get(authorization)

就诊记录列表

就诊记录列表

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MedicalRecordsApi()
authorization = 'authorization_example' # str | 

try:
    # 就诊记录列表
    api_response = api_instance.medical_records_get(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MedicalRecordsApi->medical_records_get: %s\n" % e)
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

# **medical_records_id_delete**
> object medical_records_id_delete(authorization, id)

删除就诊记录

删除就诊记录

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MedicalRecordsApi()
authorization = 'authorization_example' # str | 
id = 56 # int | 

try:
    # 删除就诊记录
    api_response = api_instance.medical_records_id_delete(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MedicalRecordsApi->medical_records_id_delete: %s\n" % e)
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

# **medical_records_id_get**
> object medical_records_id_get(authorization, id)

就诊详情

就诊详情

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MedicalRecordsApi()
authorization = 'authorization_example' # str | 
id = 56 # int | 

try:
    # 就诊详情
    api_response = api_instance.medical_records_id_get(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MedicalRecordsApi->medical_records_id_get: %s\n" % e)
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

# **medical_records_post**
> object medical_records_post(authorization, body=body)

新建就诊记录

新建就诊记录

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MedicalRecordsApi()
authorization = 'authorization_example' # str | 
body = swagger_client.Body() # Body |  (optional)

try:
    # 新建就诊记录
    api_response = api_instance.medical_records_post(authorization, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MedicalRecordsApi->medical_records_post: %s\n" % e)
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

