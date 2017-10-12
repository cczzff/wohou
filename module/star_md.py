# coding=utf-8
import datetime

import requests

from logger import logger

QUERY_STAR_LUCK_URL = 'http://jisuastro.market.alicloudapi.com/astro/fortune'
QUERY_STAR_INFO_URL = 'http://jisuastro.market.alicloudapi.com/astro/all'
APPCODE = '981573620df24ecb8a55495b02e96a48'


Aries = 1  # 白羊座
Taurus = 2  # 金牛座
Gemini = 3  # 双子座
Cancer = 4  # 巨蟹座
Leo = 5  # 狮子座
Virgo = 6  # 处女座
Libra = 7  # 天平座
Scorpio = 8  # 天蝎座
Sagittarius = 9  # 射手座
Capricorn = 10  # 摩羯座
Aquarius = 11  # 水瓶座
Pisces = 12  # 双鱼座


def get_star_luck_info(astroid):
    """
    星座查询api
    """
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    data = {'astroid': astroid, 'date': today}
    headers = {'Authorization': 'APPCODE {}'.format(APPCODE)}

    try:
        data = requests.get(QUERY_STAR_LUCK_URL, params=data, headers=headers)
        data = data.json()
        return data

    except Exception, e:
        logger('star').error('获取星座运势失败')
        return {}


def get_star_info():
    """
    星座查询api
    """
    headers = {'Authorization': 'APPCODE {}'.format(APPCODE)}

    try:
        data = requests.get(QUERY_STAR_INFO_URL, headers=headers)
        data = data.json()
        data = data['result']
        return data

    except Exception, e:
        logger('star').error('获取星座资料失败')
        return []
