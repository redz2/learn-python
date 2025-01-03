# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Archives(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, no: int=None, name: int=None, gender: int=None, birthday: str=None, father_height: float=None, mother_height: float=None, contacts: str=None, phone_num: str=None, address: str=None, establish_time: str=None, menarche: int=None, menarche_time: str=None, creator_id: object=None):  # noqa: E501
        """Archives - a model defined in Swagger

        :param id: The id of this Archives.  # noqa: E501
        :type id: int
        :param no: The no of this Archives.  # noqa: E501
        :type no: int
        :param name: The name of this Archives.  # noqa: E501
        :type name: int
        :param gender: The gender of this Archives.  # noqa: E501
        :type gender: int
        :param birthday: The birthday of this Archives.  # noqa: E501
        :type birthday: str
        :param father_height: The father_height of this Archives.  # noqa: E501
        :type father_height: float
        :param mother_height: The mother_height of this Archives.  # noqa: E501
        :type mother_height: float
        :param contacts: The contacts of this Archives.  # noqa: E501
        :type contacts: str
        :param phone_num: The phone_num of this Archives.  # noqa: E501
        :type phone_num: str
        :param address: The address of this Archives.  # noqa: E501
        :type address: str
        :param establish_time: The establish_time of this Archives.  # noqa: E501
        :type establish_time: str
        :param menarche: The menarche of this Archives.  # noqa: E501
        :type menarche: int
        :param menarche_time: The menarche_time of this Archives.  # noqa: E501
        :type menarche_time: str
        :param creator_id: The creator_id of this Archives.  # noqa: E501
        :type creator_id: object
        """
        self.swagger_types = {
            'id': int,
            'no': int,
            'name': int,
            'gender': int,
            'birthday': str,
            'father_height': float,
            'mother_height': float,
            'contacts': str,
            'phone_num': str,
            'address': str,
            'establish_time': str,
            'menarche': int,
            'menarche_time': str,
            'creator_id': object
        }

        self.attribute_map = {
            'id': 'id',
            'no': 'No',
            'name': 'name',
            'gender': 'gender',
            'birthday': 'birthday',
            'father_height': 'fatherHeight',
            'mother_height': 'motherHeight',
            'contacts': 'contacts',
            'phone_num': 'phoneNum',
            'address': 'address',
            'establish_time': 'establishTime',
            'menarche': 'menarche',
            'menarche_time': 'menarcheTime',
            'creator_id': 'creatorID'
        }

        self._id = id
        self._no = no
        self._name = name
        self._gender = gender
        self._birthday = birthday
        self._father_height = father_height
        self._mother_height = mother_height
        self._contacts = contacts
        self._phone_num = phone_num
        self._address = address
        self._establish_time = establish_time
        self._menarche = menarche
        self._menarche_time = menarche_time
        self._creator_id = creator_id

    @classmethod
    def from_dict(cls, dikt) -> 'Archives':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Archives of this Archives.  # noqa: E501
        :rtype: Archives
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Archives.

        档案ID  # noqa: E501

        :return: The id of this Archives.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Archives.

        档案ID  # noqa: E501

        :param id: The id of this Archives.
        :type id: int
        """

        self._id = id

    @property
    def no(self) -> int:
        """Gets the no of this Archives.

        档案编号  # noqa: E501

        :return: The no of this Archives.
        :rtype: int
        """
        return self._no

    @no.setter
    def no(self, no: int):
        """Sets the no of this Archives.

        档案编号  # noqa: E501

        :param no: The no of this Archives.
        :type no: int
        """

        self._no = no

    @property
    def name(self) -> int:
        """Gets the name of this Archives.

        姓名  # noqa: E501

        :return: The name of this Archives.
        :rtype: int
        """
        return self._name

    @name.setter
    def name(self, name: int):
        """Sets the name of this Archives.

        姓名  # noqa: E501

        :param name: The name of this Archives.
        :type name: int
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def gender(self) -> int:
        """Gets the gender of this Archives.

        0-男 1-女 如果为1 会额外多 menarche和menarcheTime 两个字段  # noqa: E501

        :return: The gender of this Archives.
        :rtype: int
        """
        return self._gender

    @gender.setter
    def gender(self, gender: int):
        """Sets the gender of this Archives.

        0-男 1-女 如果为1 会额外多 menarche和menarcheTime 两个字段  # noqa: E501

        :param gender: The gender of this Archives.
        :type gender: int
        """
        if gender is None:
            raise ValueError("Invalid value for `gender`, must not be `None`")  # noqa: E501

        self._gender = gender

    @property
    def birthday(self) -> str:
        """Gets the birthday of this Archives.

        出生日期  # noqa: E501

        :return: The birthday of this Archives.
        :rtype: str
        """
        return self._birthday

    @birthday.setter
    def birthday(self, birthday: str):
        """Sets the birthday of this Archives.

        出生日期  # noqa: E501

        :param birthday: The birthday of this Archives.
        :type birthday: str
        """
        if birthday is None:
            raise ValueError("Invalid value for `birthday`, must not be `None`")  # noqa: E501

        self._birthday = birthday

    @property
    def father_height(self) -> float:
        """Gets the father_height of this Archives.

        父亲身高  # noqa: E501

        :return: The father_height of this Archives.
        :rtype: float
        """
        return self._father_height

    @father_height.setter
    def father_height(self, father_height: float):
        """Sets the father_height of this Archives.

        父亲身高  # noqa: E501

        :param father_height: The father_height of this Archives.
        :type father_height: float
        """
        if father_height is None:
            raise ValueError("Invalid value for `father_height`, must not be `None`")  # noqa: E501

        self._father_height = father_height

    @property
    def mother_height(self) -> float:
        """Gets the mother_height of this Archives.

        母亲身高  # noqa: E501

        :return: The mother_height of this Archives.
        :rtype: float
        """
        return self._mother_height

    @mother_height.setter
    def mother_height(self, mother_height: float):
        """Sets the mother_height of this Archives.

        母亲身高  # noqa: E501

        :param mother_height: The mother_height of this Archives.
        :type mother_height: float
        """
        if mother_height is None:
            raise ValueError("Invalid value for `mother_height`, must not be `None`")  # noqa: E501

        self._mother_height = mother_height

    @property
    def contacts(self) -> str:
        """Gets the contacts of this Archives.

        联系人  # noqa: E501

        :return: The contacts of this Archives.
        :rtype: str
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts: str):
        """Sets the contacts of this Archives.

        联系人  # noqa: E501

        :param contacts: The contacts of this Archives.
        :type contacts: str
        """

        self._contacts = contacts

    @property
    def phone_num(self) -> str:
        """Gets the phone_num of this Archives.

        手机号码  # noqa: E501

        :return: The phone_num of this Archives.
        :rtype: str
        """
        return self._phone_num

    @phone_num.setter
    def phone_num(self, phone_num: str):
        """Sets the phone_num of this Archives.

        手机号码  # noqa: E501

        :param phone_num: The phone_num of this Archives.
        :type phone_num: str
        """

        self._phone_num = phone_num

    @property
    def address(self) -> str:
        """Gets the address of this Archives.

        联系地址  # noqa: E501

        :return: The address of this Archives.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str):
        """Sets the address of this Archives.

        联系地址  # noqa: E501

        :param address: The address of this Archives.
        :type address: str
        """

        self._address = address

    @property
    def establish_time(self) -> str:
        """Gets the establish_time of this Archives.

        建档时间  # noqa: E501

        :return: The establish_time of this Archives.
        :rtype: str
        """
        return self._establish_time

    @establish_time.setter
    def establish_time(self, establish_time: str):
        """Sets the establish_time of this Archives.

        建档时间  # noqa: E501

        :param establish_time: The establish_time of this Archives.
        :type establish_time: str
        """
        if establish_time is None:
            raise ValueError("Invalid value for `establish_time`, must not be `None`")  # noqa: E501

        self._establish_time = establish_time

    @property
    def menarche(self) -> int:
        """Gets the menarche of this Archives.

        是否初潮 0-无信息 1-否 2-是  # noqa: E501

        :return: The menarche of this Archives.
        :rtype: int
        """
        return self._menarche

    @menarche.setter
    def menarche(self, menarche: int):
        """Sets the menarche of this Archives.

        是否初潮 0-无信息 1-否 2-是  # noqa: E501

        :param menarche: The menarche of this Archives.
        :type menarche: int
        """
        if menarche is None:
            raise ValueError("Invalid value for `menarche`, must not be `None`")  # noqa: E501

        self._menarche = menarche

    @property
    def menarche_time(self) -> str:
        """Gets the menarche_time of this Archives.

        初潮时间  # noqa: E501

        :return: The menarche_time of this Archives.
        :rtype: str
        """
        return self._menarche_time

    @menarche_time.setter
    def menarche_time(self, menarche_time: str):
        """Sets the menarche_time of this Archives.

        初潮时间  # noqa: E501

        :param menarche_time: The menarche_time of this Archives.
        :type menarche_time: str
        """

        self._menarche_time = menarche_time

    @property
    def creator_id(self) -> object:
        """Gets the creator_id of this Archives.

        该档案关联的医生信息  # noqa: E501

        :return: The creator_id of this Archives.
        :rtype: object
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id: object):
        """Sets the creator_id of this Archives.

        该档案关联的医生信息  # noqa: E501

        :param creator_id: The creator_id of this Archives.
        :type creator_id: object
        """
        if creator_id is None:
            raise ValueError("Invalid value for `creator_id`, must not be `None`")  # noqa: E501

        self._creator_id = creator_id
