# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from banner.models import Banner
from banner.serializers import BannerSerializer


class BannerList(generics.ListCreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class BannerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
