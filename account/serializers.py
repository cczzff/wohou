# coding=utf8
from rest_framework import serializers

from account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('username', 'nick_name', 'birthday', 'city', 'head_img')


class AccountRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('username', 'password', 'nick_name', 'birthday', 'city', 'head_img')


class AccountLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, max_length=1024)
    password = serializers.CharField(required=False, max_length=1024)

    class Meta:
        model = Account
        fields = ('username', 'password')
