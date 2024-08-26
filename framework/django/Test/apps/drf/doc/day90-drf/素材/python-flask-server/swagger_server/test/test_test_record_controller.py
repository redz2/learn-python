# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestTestRecordController(BaseTestCase):
    """TestRecordController integration test stubs"""

    def test_testrecord_get(self):
        """Test case for testrecord_get

        测试记录列表
        """
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/api/testrecord',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_testrecord_id_delete(self):
        """Test case for testrecord_id_delete

        删除测试记录
        """
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/api/testrecord/{id}'.format(id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_testrecord_id_get(self):
        """Test case for testrecord_id_get

        查询测试详情
        """
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/api/testrecord/{id}'.format(id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
