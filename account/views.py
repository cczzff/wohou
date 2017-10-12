# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

from account.models import Account
from account.serializers import AccountSerializer, AccountRegisterSerializer


class AccountList(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetail(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


# 用于注册
class AccountRegisterAPIView(APIView):
    queryset = Account.objects.all()
    serializer_class = AccountRegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        data = request.data
        username = data
        if Account.objects.filter(username__exact=username):
            return Response("用户名已存在", HTTP_400_BAD_REQUEST)
        serializer = AccountRegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            print data
            username = data['username']
            password = data['password']
            nick_name = data['nick_name']
            birthday = data['birthday']
            head_img = data['head_img']
            city = data['city']
            Account.objects.create_user(username=username, password=password,
                                        nick_name=nick_name, birthday=birthday,
                                        head_img=head_img, city=city)

            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
