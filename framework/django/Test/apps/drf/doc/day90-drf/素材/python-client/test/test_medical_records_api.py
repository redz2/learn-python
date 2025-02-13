# coding: utf-8

"""
    项目名

    项目描述  # noqa: E501

    OpenAPI spec version: 1.1.1
    Contact: 649641514@qq.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.medical_records_api import MedicalRecordsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMedicalRecordsApi(unittest.TestCase):
    """MedicalRecordsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.medical_records_api.MedicalRecordsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_medical_records_get(self):
        """Test case for medical_records_get

        就诊记录列表  # noqa: E501
        """
        pass

    def test_medical_records_id_delete(self):
        """Test case for medical_records_id_delete

        删除就诊记录  # noqa: E501
        """
        pass

    def test_medical_records_id_get(self):
        """Test case for medical_records_id_get

        就诊详情  # noqa: E501
        """
        pass

    def test_medical_records_post(self):
        """Test case for medical_records_post

        新建就诊记录  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
