# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from article.models import Article
from article.serializers import ArticleSerializer, AriticleLikesSerializer
from constant import ARTICLE_LIKE
from todolist.permissions import IsOwnerOrReadOnly
from wohou.settings import redis_cache


class ArticleList(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    # 针对用户进行过滤
    def get_queryset(self):
        articles = Article.objects.all()
        # for article in articles:
        #     article.body = markdown(article.body)
        return articles

    # 用户创建的时候加入account
    def perform_create(self, serializer):
        serializer.save(account=self.request.user)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    # 针对用户进行过滤
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user

        articles = Article.objects.filter(account=user)
        # for article in articles:
        #     article.body = markdown(article.body)
        return articles


class ArticleLikesVIEW(APIView):
    serializer_class = AriticleLikesSerializer

    def post(self, request, format=None):
        data = request.data
        serializer = AriticleLikesSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user_id = request.user.id
            article_id = data['article_id']
            article_likes_key = ARTICLE_LIKE.format(article_id=article_id)

            if redis_cache.sismember(article_likes_key, user_id):
                redis_cache.srem(article_likes_key, user_id)
            else:
                redis_cache.sadd(article_likes_key, user_id)

            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
