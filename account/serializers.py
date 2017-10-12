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

