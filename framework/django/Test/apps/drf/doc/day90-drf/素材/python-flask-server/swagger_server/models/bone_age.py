# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class BoneAge(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, means: str=None, source: str=None, source_department: str=None, source_person: str=None, x_ray: str=None, boneage_data: str=None, boneage_report: str=None):  # noqa: E501
        """BoneAge - a model defined in Swagger

        :param id: The id of this BoneAge.  # noqa: E501
        :type id: int
        :param means: The means of this BoneAge.  # noqa: E501
        :type means: str
        :param source: The source of this BoneAge.  # noqa: E501
        :type source: str
        :param source_department: The source_department of this BoneAge.  # noqa: E501
        :type source_department: str
        :param source_person: The source_person of this BoneAge.  # noqa: E501
        :type source_person: str
        :param x_ray: The x_ray of this BoneAge.  # noqa: E501
        :type x_ray: str
        :param boneage_data: The boneage_data of this BoneAge.  # noqa: E501
        :type boneage_data: str
        :param boneage_report: The boneage_report of this BoneAge.  # noqa: E501
        :type boneage_report: str
        """
        self.swagger_types = {
            'id': int,
            'means': str,
            'source': str,
            'source_department': str,
            'source_person': str,
            'x_ray': str,
            'boneage_data': str,
            'boneage_report': str
        }

        self.attribute_map = {
            'id': 'id',
            'means': 'means',
            'source': 'source',
            'source_department': 'sourceDepartment',
            'source_person': 'sourcePerson',
            'x_ray': 'X_ray',
            'boneage_data': 'boneageData',
            'boneage_report': 'boneageReport'
        }

        self._id = id
        self._means = means
        self._source = source
        self._source_department = source_department
        self._source_person = source_person
        self._x_ray = x_ray
        self._boneage_data = boneage_data
        self._boneage_report = boneage_report

    @classmethod
    def from_dict(cls, dikt) -> 'BoneAge':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BoneAge of this BoneAge.  # noqa: E501
        :rtype: BoneAge
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this BoneAge.

        骨龄信息ID  # noqa: E501

        :return: The id of this BoneAge.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this BoneAge.

        骨龄信息ID  # noqa: E501

        :param id: The id of this BoneAge.
        :type id: int
        """

        self._id = id

    @property
    def means(self) -> str:
        """Gets the means of this BoneAge.

        检测方法  # noqa: E501

        :return: The means of this BoneAge.
        :rtype: str
        """
        return self._means

    @means.setter
    def means(self, means: str):
        """Sets the means of this BoneAge.

        检测方法  # noqa: E501

        :param means: The means of this BoneAge.
        :type means: str
        """
        if means is None:
            raise ValueError("Invalid value for `means`, must not be `None`")  # noqa: E501

        self._means = means

    @property
    def source(self) -> str:
        """Gets the source of this BoneAge.

        X光片来源  # noqa: E501

        :return: The source of this BoneAge.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source: str):
        """Sets the source of this BoneAge.

        X光片来源  # noqa: E501

        :param source: The source of this BoneAge.
        :type source: str
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def source_department(self) -> str:
        """Gets the source_department of this BoneAge.

        来源科室  # noqa: E501

        :return: The source_department of this BoneAge.
        :rtype: str
        """
        return self._source_department

    @source_department.setter
    def source_department(self, source_department: str):
        """Sets the source_department of this BoneAge.

        来源科室  # noqa: E501

        :param source_department: The source_department of this BoneAge.
        :type source_department: str
        """

        self._source_department = source_department

    @property
    def source_person(self) -> str:
        """Gets the source_person of this BoneAge.

        来源人  # noqa: E501

        :return: The source_person of this BoneAge.
        :rtype: str
        """
        return self._source_person

    @source_person.setter
    def source_person(self, source_person: str):
        """Sets the source_person of this BoneAge.

        来源人  # noqa: E501

        :param source_person: The source_person of this BoneAge.
        :type source_person: str
        """

        self._source_person = source_person

    @property
    def x_ray(self) -> str:
        """Gets the x_ray of this BoneAge.

        X光片  # noqa: E501

        :return: The x_ray of this BoneAge.
        :rtype: str
        """
        return self._x_ray

    @x_ray.setter
    def x_ray(self, x_ray: str):
        """Sets the x_ray of this BoneAge.

        X光片  # noqa: E501

        :param x_ray: The x_ray of this BoneAge.
        :type x_ray: str
        """
        if x_ray is None:
            raise ValueError("Invalid value for `x_ray`, must not be `None`")  # noqa: E501

        self._x_ray = x_ray

    @property
    def boneage_data(self) -> str:
        """Gets the boneage_data of this BoneAge.

        骨龄数据  # noqa: E501

        :return: The boneage_data of this BoneAge.
        :rtype: str
        """
        return self._boneage_data

    @boneage_data.setter
    def boneage_data(self, boneage_data: str):
        """Sets the boneage_data of this BoneAge.

        骨龄数据  # noqa: E501

        :param boneage_data: The boneage_data of this BoneAge.
        :type boneage_data: str
        """
        if boneage_data is None:
            raise ValueError("Invalid value for `boneage_data`, must not be `None`")  # noqa: E501

        self._boneage_data = boneage_data

    @property
    def boneage_report(self) -> str:
        """Gets the boneage_report of this BoneAge.

        骨龄报告  # noqa: E501

        :return: The boneage_report of this BoneAge.
        :rtype: str
        """
        return self._boneage_report

    @boneage_report.setter
    def boneage_report(self, boneage_report: str):
        """Sets the boneage_report of this BoneAge.

        骨龄报告  # noqa: E501

        :param boneage_report: The boneage_report of this BoneAge.
        :type boneage_report: str
        """
        if boneage_report is None:
            raise ValueError("Invalid value for `boneage_report`, must not be `None`")  # noqa: E501

        self._boneage_report = boneage_report
