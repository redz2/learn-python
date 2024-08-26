# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_user_change_active_put(self):
        """Test case for user_change_active_put

        修改账号状态
        """
        body = Body()
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/api/user/change_active',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_change_pwd_put(self):
        """Test case for user_change_pwd_put

        修改账号密码
        """
        body = Body()
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/api/user/change_pwd',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_get(self):
        """Test case for user_get

        用户列表接口
        """
        headers = [('name', 'name_example'),
                   ('token', 'token_example')]
        response = self.client.open(
            '/api/user',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_id_delete(self):
        """Test case for user_id_delete

        删除用户
        """
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/api/user/{id}'.format(id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_id_get(self):
        """Test case for user_id_get

        查询用户
        """
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/api/user/{id}'.format(id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_id_put(self):
        """Test case for user_id_put

        修改用户
        """
        body = Body()
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/api/user/{id}'.format(id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_login_post(self):
        """Test case for user_login_post

        用户登录
        """
        body = Body()
        response = self.client.open(
            '/api/user/login',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_post(self):
        """Test case for user_post

        新建用户
        """
        body = Body()
        response = self.client.open(
            '/api/user',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
