# coding: utf-8

"""
    项目名

    项目描述  # noqa: E501

    OpenAPI spec version: 1.1.1
    Contact: 649641514@qq.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class Archives(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'no': 'int',
        'name': 'int',
        'gender': 'int',
        'birthday': 'str',
        'father_height': 'float',
        'mother_height': 'float',
        'contacts': 'str',
        'phone_num': 'str',
        'address': 'str',
        'establish_time': 'str',
        'menarche': 'int',
        'menarche_time': 'str',
        'creator_id': 'object'
    }

    attribute_map = {
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

    def __init__(self, id=None, no=None, name=None, gender=None, birthday=None, father_height=None, mother_height=None, contacts=None, phone_num=None, address=None, establish_time=None, menarche=None, menarche_time=None, creator_id=None, _configuration=None):  # noqa: E501
        """Archives - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._no = None
        self._name = None
        self._gender = None
        self._birthday = None
        self._father_height = None
        self._mother_height = None
        self._contacts = None
        self._phone_num = None
        self._address = None
        self._establish_time = None
        self._menarche = None
        self._menarche_time = None
        self._creator_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if no is not None:
            self.no = no
        self.name = name
        self.gender = gender
        self.birthday = birthday
        self.father_height = father_height
        self.mother_height = mother_height
        if contacts is not None:
            self.contacts = contacts
        if phone_num is not None:
            self.phone_num = phone_num
        if address is not None:
            self.address = address
        self.establish_time = establish_time
        self.menarche = menarche
        if menarche_time is not None:
            self.menarche_time = menarche_time
        self.creator_id = creator_id

    @property
    def id(self):
        """Gets the id of this Archives.  # noqa: E501

        档案ID  # noqa: E501

        :return: The id of this Archives.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Archives.

        档案ID  # noqa: E501

        :param id: The id of this Archives.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def no(self):
        """Gets the no of this Archives.  # noqa: E501

        档案编号  # noqa: E501

        :return: The no of this Archives.  # noqa: E501
        :rtype: int
        """
        return self._no

    @no.setter
    def no(self, no):
        """Sets the no of this Archives.

        档案编号  # noqa: E501

        :param no: The no of this Archives.  # noqa: E501
        :type: int
        """

        self._no = no

    @property
    def name(self):
        """Gets the name of this Archives.  # noqa: E501

        姓名  # noqa: E501

        :return: The name of this Archives.  # noqa: E501
        :rtype: int
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Archives.

        姓名  # noqa: E501

        :param name: The name of this Archives.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def gender(self):
        """Gets the gender of this Archives.  # noqa: E501

        0-男 1-女 如果为1 会额外多 menarche和menarcheTime 两个字段  # noqa: E501

        :return: The gender of this Archives.  # noqa: E501
        :rtype: int
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this Archives.

        0-男 1-女 如果为1 会额外多 menarche和menarcheTime 两个字段  # noqa: E501

        :param gender: The gender of this Archives.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and gender is None:
            raise ValueError("Invalid value for `gender`, must not be `None`")  # noqa: E501

        self._gender = gender

    @property
    def birthday(self):
        """Gets the birthday of this Archives.  # noqa: E501

        出生日期  # noqa: E501

        :return: The birthday of this Archives.  # noqa: E501
        :rtype: str
        """
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        """Sets the birthday of this Archives.

        出生日期  # noqa: E501

        :param birthday: The birthday of this Archives.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and birthday is None:
            raise ValueError("Invalid value for `birthday`, must not be `None`")  # noqa: E501

        self._birthday = birthday

    @property
    def father_height(self):
        """Gets the father_height of this Archives.  # noqa: E501

        父亲身高  # noqa: E501

        :return: The father_height of this Archives.  # noqa: E501
        :rtype: float
        """
        return self._father_height

    @father_height.setter
    def father_height(self, father_height):
        """Sets the father_height of this Archives.

        父亲身高  # noqa: E501

        :param father_height: The father_height of this Archives.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and father_height is None:
            raise ValueError("Invalid value for `father_height`, must not be `None`")  # noqa: E501

        self._father_height = father_height

    @property
    def mother_height(self):
        """Gets the mother_height of this Archives.  # noqa: E501

        母亲身高  # noqa: E501

        :return: The mother_height of this Archives.  # noqa: E501
        :rtype: float
        """
        return self._mother_height

    @mother_height.setter
    def mother_height(self, mother_height):
        """Sets the mother_height of this Archives.

        母亲身高  # noqa: E501

        :param mother_height: The mother_height of this Archives.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and mother_height is None:
            raise ValueError("Invalid value for `mother_height`, must not be `None`")  # noqa: E501

        self._mother_height = mother_height

    @property
    def contacts(self):
        """Gets the contacts of this Archives.  # noqa: E501

        联系人  # noqa: E501

        :return: The contacts of this Archives.  # noqa: E501
        :rtype: str
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this Archives.

        联系人  # noqa: E501

        :param contacts: The contacts of this Archives.  # noqa: E501
        :type: str
        """

        self._contacts = contacts

    @property
    def phone_num(self):
        """Gets the phone_num of this Archives.  # noqa: E501

        手机号码  # noqa: E501

        :return: The phone_num of this Archives.  # noqa: E501
        :rtype: str
        """
        return self._phone_num

    @phone_num.setter
    def phone_num(self, phone_num):
        """Sets the phone_num of this Archives.

        手机号码  # noqa: E501

        :param phone_num: The phone_num of this Archives.  # noqa: E501
        :type: str
        """

        self._phone_num = phone_num

    @property
    def address(self):
        """Gets the address of this Archives.  # noqa: E501

        联系地址  # noqa: E501

        :return: The address of this Archives.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Archives.

        联系地址  # noqa: E501

        :param address: The address of this Archives.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def establish_time(self):
        """Gets the establish_time of this Archives.  # noqa: E501

        建档时间  # noqa: E501

        :return: The establish_time of this Archives.  # noqa: E501
        :rtype: str
        """
        return self._establish_time

    @establish_time.setter
    def establish_time(self, establish_time):
        """Sets the establish_time of this Archives.

        建档时间  # noqa: E501

        :param establish_time: The establish_time of this Archives.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and establish_time is None:
            raise ValueError("Invalid value for `establish_time`, must not be `None`")  # noqa: E501

        self._establish_time = establish_time

    @property
    def menarche(self):
        """Gets the menarche of this Archives.  # noqa: E501

        是否初潮 0-无信息 1-否 2-是  # noqa: E501

        :return: The menarche of this Archives.  # noqa: E501
        :rtype: int
        """
        return self._menarche

    @menarche.setter
    def menarche(self, menarche):
        """Sets the menarche of this Archives.

        是否初潮 0-无信息 1-否 2-是  # noqa: E501

        :param menarche: The menarche of this Archives.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and menarche is None:
            raise ValueError("Invalid value for `menarche`, must not be `None`")  # noqa: E501

        self._menarche = menarche

    @property
    def menarche_time(self):
        """Gets the menarche_time of this Archives.  # noqa: E501

        初潮时间  # noqa: E501

        :return: The menarche_time of this Archives.  # noqa: E501
        :rtype: str
        """
        return self._menarche_time

    @menarche_time.setter
    def menarche_time(self, menarche_time):
        """Sets the menarche_time of this Archives.

        初潮时间  # noqa: E501

        :param menarche_time: The menarche_time of this Archives.  # noqa: E501
        :type: str
        """

        self._menarche_time = menarche_time

    @property
    def creator_id(self):
        """Gets the creator_id of this Archives.  # noqa: E501

        该档案关联的医生信息  # noqa: E501

        :return: The creator_id of this Archives.  # noqa: E501
        :rtype: object
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this Archives.

        该档案关联的医生信息  # noqa: E501

        :param creator_id: The creator_id of this Archives.  # noqa: E501
        :type: object
        """
        if self._configuration.client_side_validation and creator_id is None:
            raise ValueError("Invalid value for `creator_id`, must not be `None`")  # noqa: E501

        self._creator_id = creator_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Archives, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Archives):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Archives):
            return True

        return self.to_dict() != other.to_dict()
