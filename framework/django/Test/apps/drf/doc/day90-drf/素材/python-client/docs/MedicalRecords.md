# MedicalRecords

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 就诊id | [optional] 
**visit_time** | **str** | 就诊时间 | 
**height** | **float** | 就诊身高 | 
**weight** | **float** | 就诊体重 | 
**height_report** | **str** | 身高报告 json数据 | 
**weight_report** | **str** | BMI报告 json数据 | 
**has_boneage_info** | **bool** | 是否有骨龄信息 true-有 false-无 | [optional] 
**boneage** | **object** | 骨龄信息id,管理就诊人的骨龄信息 | 
**archive** | **object** | 档案id,关联就诊人的档案信息 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


