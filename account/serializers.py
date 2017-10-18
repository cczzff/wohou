# coding=utf8
import re

from rest_framework import serializers

from account.models import Account


def register_username_validate(username):
    if not re.match(r'^0?(13[0-9]|15[3-9]|15[0-2]|18[0-9])[0-9]{8}$', username):
        raise serializers.ValidationError('手机号格式不对')

    users = Account.objects.filter(username=username)
    if users:
        raise serializers.ValidationError('该用户信息已存在')


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


class RestPasswordSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, max_length=1024)
    old_password = serializers.CharField(required=False, max_length=1024)
    new_password = serializers.CharField(required=False, max_length=1024)


class RegisterCodeSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=1024, validators=[register_username_validate])


