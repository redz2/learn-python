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
from swagger_client.api.test_record_api import TestRecordApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTestRecordApi(unittest.TestCase):
    """TestRecordApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.test_record_api.TestRecordApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_testrecord_get(self):
        """Test case for testrecord_get

        测试记录列表  # noqa: E501
        """
        pass

    def test_testrecord_id_delete(self):
        """Test case for testrecord_id_delete

        删除测试记录  # noqa: E501
        """
        pass

    def test_testrecord_id_get(self):
        """Test case for testrecord_id_get

        查询测试详情  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
