import connexion
import six

from swagger_server import util


def testrecord_get(Authorization):  # noqa: E501
    """测试记录列表

    测试记录列表 # noqa: E501

    :param Authorization: 
    :type Authorization: str

    :rtype: object
    """
    return 'do some magic!'


def testrecord_id_delete(id, Authorization):  # noqa: E501
    """删除测试记录

    删除测试记录 # noqa: E501

    :param id: 
    :type id: int
    :param Authorization: 
    :type Authorization: str

    :rtype: object
    """
    return 'do some magic!'


def testrecord_id_get(id, Authorization):  # noqa: E501
    """查询测试详情

    查询测试详情 # noqa: E501

    :param id: 
    :type id: int
    :param Authorization: 
    :type Authorization: str

    :rtype: object
    """
    return 'do some magic!'
