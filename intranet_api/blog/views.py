from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Article_Blog
from .models import Category_Blog
from .serializers import ArticleSerializer
from .serializers import CategorySerializer


# Create a custom pagination class for blog articlesŒ
class BlogArticlePagination(PageNumberPagination):
    page_size = 12  # Or any number you prefer


class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category_Blog.objects.all()
    tags = ['Blog - Category']


class ArticlesViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article_Blog.objects.all()
    pagination_class = BlogArticlePagination  # Add this line
    tags = ['Blog - Article']
