from django.shortcuts import render
from .models import Category_Blog
from .models import Article_Blog
from .serializers import CategorySerializer
from .serializers import ArticleSerializer

from rest_framework import viewsets


# Create your views here.
class CategorysViewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category_Blog.objects.all()
    tags = ['Blog - Category']


class ArticlesViewset(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article_Blog.objects.all()
    tags = ['Blog - Article']
