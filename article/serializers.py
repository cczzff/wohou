# coding=utf8
from __future__ import unicode_literals
from rest_framework import serializers

from article.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ('account', 'title', 'body', 'created', 'likes')

    # SerializerMethodFiel是一个read-only字段
    # 当不指定其method_name时，默认为get_<field_name>
    # 如果使用ModelSerializer并指定字段时，要包含此时定义的字段

    def get_likes(self, obj):
        """
        赞的数量
        """
        return '赞的数量！'