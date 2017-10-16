# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from rest_framework import generics

from todolist.models import Todo
from todolist.permissions import IsOwnerOrReadOnly
from todolist.serializers import TodoSerializer


class TodoList(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    # 针对用户进行过滤
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Todo.objects.filter(account=user)

    # 用户创建的时候加入account
    def perform_create(self, serializer):
        serializer.save(account=self.request.user)


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsOwnerOrReadOnly,)