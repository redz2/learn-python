import connexion
import six

from swagger_server.models.body import Body  # noqa: E501
from swagger_server import util


def user_change_active_put(Authorization, body=None):  # noqa: E501
    """修改账号状态

    修改账号状态 # noqa: E501

    :param Authorization: 
    :type Authorization: str
    :param body: 
    :type body: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        body = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def user_change_pwd_put(Authorization, body=None):  # noqa: E501
    """修改账号密码

    修改账号密码 # noqa: E501

    :param Authorization: 
    :type Authorization: str
    :param body: 
    :type body: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        body = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def user_get(name, token):  # noqa: E501
    """用户列表接口

    获取所有用户列表 # noqa: E501

    :param name: 
    :type name: str
    :param token: 
    :type token: str

    :rtype: object
    """
    return 'do some magic!'


def user_id_delete(id, Authorization):  # noqa: E501
    """删除用户

    通过id删除用户 # noqa: E501

    :param id: 
    :type id: int
    :param Authorization: 
    :type Authorization: str

    :rtype: object
    """
    return 'do some magic!'


def user_id_get(id, Authorization):  # noqa: E501
    """查询用户

    通过id查询用户信息 # noqa: E501

    :param id: 
    :type id: int
    :param Authorization: 
    :type Authorization: str

    :rtype: object
    """
    return 'do some magic!'


def user_id_put(id, Authorization, body=None):  # noqa: E501
    """修改用户

    通过id修改用户信息 # noqa: E501

    :param id: 
    :type id: int
    :param Authorization: 
    :type Authorization: str
    :param body: 
    :type body: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        body = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def user_login_post(body):  # noqa: E501
    """用户登录

    用户登录 # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        body = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def user_post(body):  # noqa: E501
    """新建用户

    新建用户 # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        body = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
