# coding=utf-8

from django.core.management.base import BaseCommand

from info.models import CityInfo, StarInfo
from module.star_md import get_star_info
from module.weather_md import get_city_info


class Command(BaseCommand):
    help = '重新抓取股票代码表'

    def handle(self, *args, **options):
        self.fill_city_info()
        self.fill_star_info()

    def fill_city_info(self):
        city_infos = get_city_info()
        CityInfo.objects.all().delete()

        for info in city_infos:
            cityid = int(info['cityid'])
            city = info['city']
            citycode = info['citycode']
            parentid = info['parentid']

            CityInfo.objects.create(cityid=cityid,
                                    city=city,
                                    citycode=citycode,
                                    parentid=parentid)

        self.stdout.write('data init success')

    def fill_star_info(self):
        star_infos = get_star_info()
        StarInfo.objects.all().delete()

        for info in star_infos:
            astroid = int(info['astroid'])

            StarInfo.objects.create(astroid=astroid,
                                    astroname=info['astroname'],
                                    date=info['date'],
                                    pic=info['pic'])

        self.stdout.write('data init success')
