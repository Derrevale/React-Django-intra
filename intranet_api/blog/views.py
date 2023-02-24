from django.shortcuts import render
from .models import Category
from .models import Article
from .serializers import CategorySerializer
from .serializers import ArticleSerializer

from rest_framework import viewsets


# Create your views here.
class CategorysViewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ArticlesViewset(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
