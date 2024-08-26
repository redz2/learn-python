# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMedicalRecordsController(BaseTestCase):
    """MedicalRecordsController integration test stubs"""

    def test_medical_records_get(self):
        """Test case for medical_records_get

        就诊记录列表
        """
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/api/medical_records',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_medical_records_id_delete(self):
        """Test case for medical_records_id_delete

        删除就诊记录
        """
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/api/medical_records/{id}'.format(id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_medical_records_id_get(self):
        """Test case for medical_records_id_get

        就诊详情
        """
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/api/medical_records/{id}'.format(id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_medical_records_post(self):
        """Test case for medical_records_post

        新建就诊记录
        """
        body = Body()
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/api/medical_records',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
