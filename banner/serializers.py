# coding=utf8
from rest_framework import serializers

from banner.models import Banner


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ('id', 'title', 'picture_url', 'is_use')

