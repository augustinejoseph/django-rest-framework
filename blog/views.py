from django.shortcuts import render
from rest_framework import generics
from blog.serializers import PostSerializer, CategorySerializer
from .models import Post, Category
from rest_framework.response import Response


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.filter()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class Category(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
