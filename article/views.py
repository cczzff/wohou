# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from markdown import markdown
from rest_framework import generics

from article.models import Article
from article.serializers import ArticleSerializer
from todolist.permissions import IsOwnerOrReadOnly


class ArticleList(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    # 针对用户进行过滤
    def get_queryset(self):
        articles = Article.objects.all()
        for article in articles:
            article.body = markdown(article.body)
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
        for article in articles:
            article.body = markdown(article.body)
        return articles
