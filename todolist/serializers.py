# coding=utf8
from rest_framework import serializers

from todolist.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'todo_time', 'note', 'sms_remid')
