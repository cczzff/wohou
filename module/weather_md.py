# coding=utf-8
import requests
# 获取天气信息url
from logger import logger

QUERY_WEATHER_URL = 'http://jisutianqi.market.alicloudapi.com/weather/query'
# 获取城市信息url
QUERY_CITY_URL = 'http://jisutianqi.market.alicloudapi.com/weather/city'
APPCODE = '981573620df24ecb8a55495b02e96a48'


def get_weather_info(citycode):
    """
    天气查询
    """
    data = {'citycode': citycode}
    headers = {'Authorization': 'APPCODE {}'.format(APPCODE)}

    try:
        data = requests.get(QUERY_WEATHER_URL, params=data, headers=headers)
        data = data.json()
        return data

    except Exception, e:
        logger('weather').error('获取城市{}天气失败'.format(citycode))
        return {}


def get_city_info():
    """
    城市查询
    """
    headers = {'Authorization': 'APPCODE {}'.format(APPCODE)}

    try:
        data = requests.get(QUERY_CITY_URL, headers=headers)
        data = data.json()
        data = data['result']
        return data

    except Exception, e:
        logger('weather').error('获取城市资料失败')
        return []
