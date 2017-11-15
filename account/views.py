# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib

import os
import random

from django.core.cache import cache
from django.contrib.auth import logout
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

from account.models import Account
from account.serializers import AccountSerializer, AccountRegisterSerializer, \
    RestPasswordSerializer, RegisterCodeSerializer, FriendsSerializer
from celery_md.tasks import celery_send_verify_code
from constant import CACHE_REGISTER


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
        username = data['username']
        if Account.objects.filter(username__exact=username):
            return Response({'username': '用户名已存在'}, HTTP_400_BAD_REQUEST)
        serializer = AccountRegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            username = data['username']
            password = data['password']
            nick_name = data['nick_name']
            birthday = data['birthday']
            head_img = data['head_img']
            city = data['city']
            code = data['code']
            if code != cache.get(CACHE_REGISTER.format(username=username)):
                return Response({'code': '验证码错误'}, status=HTTP_400_BAD_REQUEST)

            Account.objects.create_user(username=username, password=password,
                                        nick_name=nick_name, birthday=birthday,
                                        head_img=head_img, city=city)

            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class RestPasswordView(APIView):
    """
    重置密码
    """
    permission_classes = (AllowAny,)
    serializer_class = RestPasswordSerializer

    def post(self, request, format=None):
        data = request.data
        username = data['username']

        if not Account.objects.filter(username__exact=username):
            return Response("用户名不存在", HTTP_400_BAD_REQUEST)

        serializer = RestPasswordSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            username = data['username']
            old_password = data['old_password']
            new_password = data['new_password']
            user = Account.objects.get(username__iexact=username)
            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()
                token_key = hashlib.sha1(os.urandom(24)).hexdigest()
                Token.objects.filter(user_id=request.user.id).update(key=token_key)
                logout(request)
                return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class RegisterCodeView(APIView):
    """
    发送短信验证码
    """
    permission_classes = (AllowAny,)
    serializer_class = RegisterCodeSerializer

    def post(self, request, format=None):
        data = request.data
        serializer = RegisterCodeSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            username = data['username']
            code = random.randint(1000, 9999)
            celery_send_verify_code.delay(username, code)
            cache.set(CACHE_REGISTER.format(username=username), code)
            cache.expire(CACHE_REGISTER.format(username=username), timeout=60)
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class FriendsView(APIView):
    """
    关注与取消关注
    """
    serializer_class = FriendsSerializer

    def post(self, request, format=None):
        data = request.data
        serializer = FriendsSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            username = data['username']
            friend = Account.objects.get(username=username)
            if data['attention'] and friend not in request.user.friends.all():
                request.user.friends.add(friend)

            if not data['attention'] and friend in request.user.friends.all():
                request.user.friends.delete(friend)

            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
