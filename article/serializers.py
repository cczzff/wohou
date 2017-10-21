# coding=utf8
from __future__ import unicode_literals
from rest_framework import serializers

from article.models import Article
from constant import ARTICLE_LIKE
from wohou.settings import redis_cache


def is_article_id(article_id):

    article = Article.objects.filter(id=article_id)
    if not article:
        raise serializers.ValidationError('该用户信息不存在')


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
        赞
        """
        article_id = obj.id
        likes = redis_cache.smembers(ARTICLE_LIKE.format(article_id=article_id))
        return likes


class AriticleLikesSerializer(serializers.Serializer):
    article_id = serializers.IntegerField(validators=[is_article_id])

