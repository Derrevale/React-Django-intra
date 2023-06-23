from .models import CategoryBlog
from .models import ArticleBlog

from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryBlog
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleBlog
        fields = '__all__'
