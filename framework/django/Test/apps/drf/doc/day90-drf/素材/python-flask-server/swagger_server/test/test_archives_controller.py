# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.test import BaseTestCase


class TestArchivesController(BaseTestCase):
    """ArchivesController integration test stubs"""

    def test_archives_get(self):
        """Test case for archives_get

        档案列表
        """
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/api/archives',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_archives_id_delete(self):
        """Test case for archives_id_delete

        删除档案
        """
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/api/archives/{id}'.format(id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_archives_id_get(self):
        """Test case for archives_id_get

        查询用户档案
        """
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/api/archives/{id}'.format(id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_archives_id_put(self):
        """Test case for archives_id_put

        修改档案信息
        """
        body = Body()
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/api/archives/{id}'.format(id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_archives_post(self):
        """Test case for archives_post

        新建档案
        """
        body = Body()
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/api/archives',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
