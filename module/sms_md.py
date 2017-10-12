# coding=utf8
import requests

from logger import logger

ACCESS_KEY = 'sjMqYMLv53Yo48mw'
SECRET = 'maxZeFpbjOKnQMB7q4rR1aPXT0hi4bqI'
SIGN = '【我猴】'
TODOLIST_TEMPLATEID = 968
VERIFY_CODE_TEMPLATEID = 969
SMS_URL = 'http://api.1cloudsp.com/api/v2/send'


def send_todolist_msg(mobile, content):
    """
    发送待办事项通知
    """

    data = {
        'accesskey': ACCESS_KEY,
        'secret': SECRET,
        'sign': SIGN,
        'templateId': TODOLIST_TEMPLATEID,
        'mobile': mobile,
        'content': content,
    }

    # 仅记录下错误, 不然程序就停止了
    try:
        requests.get(SMS_URL, params=data, timeout=1)
        logger('sms').info(data)

    except Exception, e:
        logger('sms').error(e)
        logger('sms').error(data)


def send_verify_code_msg(mobile, verify_code):
    """
    验证码短信
    """
    data = {
        'accesskey': ACCESS_KEY,
        'secret': SECRET,
        'sign': SIGN,
        'templateId': VERIFY_CODE_TEMPLATEID,
        'mobile': mobile,
        'content': verify_code,
    }

    try:
        requests.get(SMS_URL, params=data, timeout=1)
        logger('sms').info(data)

    except Exception, e:
        logger('sms').error(e)
        logger('sms').error(data)