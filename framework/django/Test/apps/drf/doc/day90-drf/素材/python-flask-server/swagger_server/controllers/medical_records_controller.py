import connexion
import six

from swagger_server.models.body import Body  # noqa: E501
from swagger_server import util


def medical_records_get(Authorization):  # noqa: E501
    """就诊记录列表

    就诊记录列表 # noqa: E501

    :param Authorization: 
    :type Authorization: str

    :rtype: object
    """
    return 'do some magic!'


def medical_records_id_delete(Authorization, id):  # noqa: E501
    """删除就诊记录

    删除就诊记录 # noqa: E501

    :param Authorization: 
    :type Authorization: str
    :param id: 
    :type id: int

    :rtype: object
    """
    return 'do some magic!'


def medical_records_id_get(Authorization, id):  # noqa: E501
    """就诊详情

    就诊详情 # noqa: E501

    :param Authorization: 
    :type Authorization: str
    :param id: 
    :type id: int

    :rtype: object
    """
    return 'do some magic!'


def medical_records_post(Authorization, body=None):  # noqa: E501
    """新建就诊记录

    新建就诊记录 # noqa: E501

    :param Authorization: 
    :type Authorization: str
    :param body: 
    :type body: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        body = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
