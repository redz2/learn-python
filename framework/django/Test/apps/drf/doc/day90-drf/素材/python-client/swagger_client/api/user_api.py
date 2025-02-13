# coding: utf-8

"""
    项目名

    项目描述  # noqa: E501

    OpenAPI spec version: 1.1.1
    Contact: 649641514@qq.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class UserApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def user_change_active_put(self, authorization, **kwargs):  # noqa: E501
        """修改账号状态  # noqa: E501

        修改账号状态  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_change_active_put(authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: (required)
        :param Body body:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_change_active_put_with_http_info(authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.user_change_active_put_with_http_info(authorization, **kwargs)  # noqa: E501
            return data

    def user_change_active_put_with_http_info(self, authorization, **kwargs):  # noqa: E501
        """修改账号状态  # noqa: E501

        修改账号状态  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_change_active_put_with_http_info(authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: (required)
        :param Body body:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_change_active_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if self.api_client.client_side_validation and ('authorization' not in params or
                                                       params['authorization'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authorization` when calling `user_change_active_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/user/change_active', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_change_pwd_put(self, authorization, **kwargs):  # noqa: E501
        """修改账号密码  # noqa: E501

        修改账号密码  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_change_pwd_put(authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: (required)
        :param Body body:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_change_pwd_put_with_http_info(authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.user_change_pwd_put_with_http_info(authorization, **kwargs)  # noqa: E501
            return data

    def user_change_pwd_put_with_http_info(self, authorization, **kwargs):  # noqa: E501
        """修改账号密码  # noqa: E501

        修改账号密码  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_change_pwd_put_with_http_info(authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: (required)
        :param Body body:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_change_pwd_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if self.api_client.client_side_validation and ('authorization' not in params or
                                                       params['authorization'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authorization` when calling `user_change_pwd_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/user/change_pwd', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_get(self, name, token, **kwargs):  # noqa: E501
        """用户列表接口  # noqa: E501

        获取所有用户列表  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_get(name, token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param str token: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_get_with_http_info(name, token, **kwargs)  # noqa: E501
        else:
            (data) = self.user_get_with_http_info(name, token, **kwargs)  # noqa: E501
            return data

    def user_get_with_http_info(self, name, token, **kwargs):  # noqa: E501
        """用户列表接口  # noqa: E501

        获取所有用户列表  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_get_with_http_info(name, token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param str token: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if self.api_client.client_side_validation and ('name' not in params or
                                                       params['name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `name` when calling `user_get`")  # noqa: E501
        # verify the required parameter 'token' is set
        if self.api_client.client_side_validation and ('token' not in params or
                                                       params['token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `token` when calling `user_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'name' in params:
            header_params['name'] = params['name']  # noqa: E501
        if 'token' in params:
            header_params['token'] = params['token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/user', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_id_delete(self, id, authorization, **kwargs):  # noqa: E501
        """删除用户  # noqa: E501

        通过id删除用户  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_id_delete(id, authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param str authorization: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_id_delete_with_http_info(id, authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.user_id_delete_with_http_info(id, authorization, **kwargs)  # noqa: E501
            return data

    def user_id_delete_with_http_info(self, id, authorization, **kwargs):  # noqa: E501
        """删除用户  # noqa: E501

        通过id删除用户  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_id_delete_with_http_info(id, authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param str authorization: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `user_id_delete`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if self.api_client.client_side_validation and ('authorization' not in params or
                                                       params['authorization'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authorization` when calling `user_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/user/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_id_get(self, id, authorization, **kwargs):  # noqa: E501
        """查询用户  # noqa: E501

        通过id查询用户信息  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_id_get(id, authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param str authorization: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_id_get_with_http_info(id, authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.user_id_get_with_http_info(id, authorization, **kwargs)  # noqa: E501
            return data

    def user_id_get_with_http_info(self, id, authorization, **kwargs):  # noqa: E501
        """查询用户  # noqa: E501

        通过id查询用户信息  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_id_get_with_http_info(id, authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param str authorization: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `user_id_get`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if self.api_client.client_side_validation and ('authorization' not in params or
                                                       params['authorization'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authorization` when calling `user_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/user/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_id_put(self, id, authorization, **kwargs):  # noqa: E501
        """修改用户  # noqa: E501

        通过id修改用户信息  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_id_put(id, authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param str authorization: (required)
        :param Body body:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_id_put_with_http_info(id, authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.user_id_put_with_http_info(id, authorization, **kwargs)  # noqa: E501
            return data

    def user_id_put_with_http_info(self, id, authorization, **kwargs):  # noqa: E501
        """修改用户  # noqa: E501

        通过id修改用户信息  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_id_put_with_http_info(id, authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param str authorization: (required)
        :param Body body:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'authorization', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `user_id_put`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if self.api_client.client_side_validation and ('authorization' not in params or
                                                       params['authorization'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authorization` when calling `user_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/user/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_login_post(self, body, **kwargs):  # noqa: E501
        """用户登录  # noqa: E501

        用户登录  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_login_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_login_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.user_login_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def user_login_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """用户登录  # noqa: E501

        用户登录  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_login_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_login_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `user_login_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/user/login', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_post(self, body, **kwargs):  # noqa: E501
        """新建用户  # noqa: E501

        新建用户  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.user_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def user_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """新建用户  # noqa: E501

        新建用户  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `user_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/user', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
