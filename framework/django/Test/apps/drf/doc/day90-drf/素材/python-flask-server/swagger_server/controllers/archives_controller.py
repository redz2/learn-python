import connexion
import six

from swagger_server.models.body import Body  # noqa: E501
from swagger_server import util


def archives_get(Authorization):  # noqa: E501
    """档案列表

    档案列表 # noqa: E501

    :param Authorization: 
    :type Authorization: str

    :rtype: object
    """
    return 'do some magic!'


def archives_id_delete(Authorization, id):  # noqa: E501
    """删除档案

    通过id删除档案 # noqa: E501

    :param Authorization: 
    :type Authorization: str
    :param id: 
    :type id: int

    :rtype: object
    """
    return 'do some magic!'


def archives_id_get(Authorization, id):  # noqa: E501
    """查询用户档案

    查询用户档案 # noqa: E501

    :param Authorization: 
    :type Authorization: str
    :param id: 
    :type id: int

    :rtype: object
    """
    return 'do some magic!'


def archives_id_put(Authorization, id, body=None):  # noqa: E501
    """修改档案信息

    通过id修改档案信息息 # noqa: E501

    :param Authorization: 
    :type Authorization: str
    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        body = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def archives_post(Authorization, body):  # noqa: E501
    """新建档案

    新建档案 # noqa: E501

    :param Authorization: 
    :type Authorization: str
    :param body: 
    :type body: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        body = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
