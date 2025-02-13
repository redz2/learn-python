# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class User(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, username: str=None, password: str=None, name: str=None, department: str=None, is_active: bool=None):  # noqa: E501
        """User - a model defined in Swagger

        :param id: The id of this User.  # noqa: E501
        :type id: int
        :param username: The username of this User.  # noqa: E501
        :type username: str
        :param password: The password of this User.  # noqa: E501
        :type password: str
        :param name: The name of this User.  # noqa: E501
        :type name: str
        :param department: The department of this User.  # noqa: E501
        :type department: str
        :param is_active: The is_active of this User.  # noqa: E501
        :type is_active: bool
        """
        self.swagger_types = {
            'id': int,
            'username': str,
            'password': str,
            'name': str,
            'department': str,
            'is_active': bool
        }

        self.attribute_map = {
            'id': 'id',
            'username': 'username',
            'password': 'password',
            'name': 'name',
            'department': 'department',
            'is_active': 'is_active'
        }

        self._id = id
        self._username = username
        self._password = password
        self._name = name
        self._department = department
        self._is_active = is_active

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this User.

        用户ID  # noqa: E501

        :return: The id of this User.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this User.

        用户ID  # noqa: E501

        :param id: The id of this User.
        :type id: int
        """

        self._id = id

    @property
    def username(self) -> str:
        """Gets the username of this User.

        账号  # noqa: E501

        :return: The username of this User.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this User.

        账号  # noqa: E501

        :param username: The username of this User.
        :type username: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def password(self) -> str:
        """Gets the password of this User.

        密码  # noqa: E501

        :return: The password of this User.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this User.

        密码  # noqa: E501

        :param password: The password of this User.
        :type password: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def name(self) -> str:
        """Gets the name of this User.

        姓名  # noqa: E501

        :return: The name of this User.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this User.

        姓名  # noqa: E501

        :param name: The name of this User.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def department(self) -> str:
        """Gets the department of this User.

        科室  # noqa: E501

        :return: The department of this User.
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department: str):
        """Sets the department of this User.

        科室  # noqa: E501

        :param department: The department of this User.
        :type department: str
        """
        if department is None:
            raise ValueError("Invalid value for `department`, must not be `None`")  # noqa: E501

        self._department = department

    @property
    def is_active(self) -> bool:
        """Gets the is_active of this User.

        用户状态 true-为启用 false-为禁用  # noqa: E501

        :return: The is_active of this User.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active: bool):
        """Sets the is_active of this User.

        用户状态 true-为启用 false-为禁用  # noqa: E501

        :param is_active: The is_active of this User.
        :type is_active: bool
        """

        self._is_active = is_active
