# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your models here.
# coding=utf-8
import re
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class AccountManager(BaseUserManager):
    def create_user(self, username, password,
                    nick_name, birthday, head_img, city):
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
            nick_name=nick_name,
            birthday=birthday,
            head_img=head_img,
            city=city
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password, nick_name='admin', birthday='2012-2-2', head_img='', city='深圳')
        user.is_admin = True
        user.save(using=self._db)
        return user


def phone_validate(value):
    """
    手机号码校验
    """
    if not re.match(r'^0?(13[0-9]|15[3-9]|15[0-2]|18[0-9])[0-9]{8}$', value):
        raise ValidationError('手机号格式不对')


class Account(AbstractBaseUser):

    username = models.CharField('用户名', max_length=100, unique=True,
                                db_index=True, validators=[phone_validate])

    nick_name = models.CharField('用户昵称', max_length=100)
    birthday = models.DateField('生日')
    city = models.CharField('所在城市', max_length=100)
    head_img = models.CharField('头像地址', max_length=100)
    friends = models.ManyToManyField('self', symmetrical=False)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'username'

    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):              # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        db_table = 'account'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
